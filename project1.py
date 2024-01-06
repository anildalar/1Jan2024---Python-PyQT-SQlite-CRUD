import sqlite3
import sys

from PyQt6.QtWidgets import QTableWidget,QTableWidgetItem, QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout,QHBoxLayout, QPushButton, QMessageBox # * means all module

#         ceo = ClassName()
#         ceo = module.ClassName()
   # = module.method()
conn = sqlite3.connect("./mydatabase.sqlite")
cursor = conn.cursor()

query = '''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                salary REAL NOT NULL
            );
        '''
cursor.execute(query) # query is an actual argument
conn.commit()
app = QApplication([])# [] is a list in python

# Create widgets
rowid = QLineEdit()
rowid.setHidden(True) 

name_label = QLabel('Name:')
name = QLineEdit()

position_label = QLabel('Position:')
position = QLineEdit()

salary_label = QLabel('Salary:')
salary = QLineEdit()

submit_button = QPushButton('Submit')

view_button = QPushButton('View')

showemployees = QPushButton('Show Employees')
# x=10 Global Variable
#ceo = ClassName()
table = QTableWidget()
def deleteEmployee(row):
    # Create a confirmation QMessageBox
    confirmation_box = QMessageBox()
    confirmation_box.setIcon(QMessageBox.Icon.Question)
    confirmation_box.setText("Do you want to proceed?")
    confirmation_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    confirmation_box.setDefaultButton(QMessageBox.StandardButton.No)

    # Execute the confirmation dialog and get the result
    result = confirmation_box.exec()

    # Check the result
    if result == QMessageBox.StandardButton.Yes:
        print("User clicked Yes, proceed with the action.")
        # Add your action here
        print(row)
        print(table.item(row,0).text())
        delid = table.item(row,0).text()
        print("Before Typecasting")
        print(delid)
        print(type(delid))
        #typecasting
        delid = int(delid)
        print("After Typecasting")
        print(delid)
        print(type(delid))
        
        print(f"DELETE FROM employees WHERE id={delid}")
        #1. Build the query
        query = f"DELETE FROM employees WHERE id={delid}"
        #2. Execute the query
        cursor.execute(query)
        #3. Commit the query
        conn.commit()
        table.removeRow(row)
        
    else:
        print("User clicked No, cancel the action.")
#global Variablw
def editEmployee(row):
    print(row)
    print(table.item(row,0).text())
    print(table.item(row,1).text())
    print(table.item(row,2).text())
    print(table.item(row,3).text())
    submit_button.setText('Update')
    rowid.setText(table.item(row,0).text())
    name.setText(table.item(row,1).text())
    position.setText(table.item(row,2).text())
    salary.setText(table.item(row,3).text())
    print(rowid.text())
    
    
    pass           
def showEmployeesSlotFunction():
    # We can use global variable inside function defination
    print("Hello")
    # Fetch data from the database
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()
    #ceo  = ClassName()
   
    column_names = ['ID', 'Name', 'Position','Salary','Actions']
    table.setColumnCount(len(column_names))
    table.setHorizontalHeaderLabels(column_names)
    # Set row count
    table.setRowCount(len(data))

    print(enumerate(data))
    # Populate the table with data
    for row_num, row_data in enumerate(data):
        delid=''
        for col_num, col_data in enumerate(row_data):
            item = QTableWidgetItem(str(col_data))
            table.setItem(row_num, col_num, item)
        print()
        # Add buttons for each row
        #view_button = QPushButton('View')
        edit_button = QPushButton('Edit')
        delete_button = QPushButton('Delete')
        
        button_layout = QHBoxLayout()
        #button_layout.addWidget(view_button)
        button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)
        button_layout.setContentsMargins(0, 0, 0, 0)  # No margins

        buttons_widget = QWidget()
        buttons_widget.setLayout(button_layout)
        table.setCellWidget(row_num,len(column_names) - 1,buttons_widget)
        edit_button.clicked.connect(lambda _,row=row_num: editEmployee(row))#function(aa1,aa2,aa3)
        delete_button.clicked.connect(lambda _,row=row_num: deleteEmployee(row))#function(aa1,aa2,aa3)
    
    table.show()
    pass

#1. Function defination
def showMsg(msg):
    msgBox = QMessageBox()
    msgBox.setText(msg)
    msgBox.exec()
    showEmployeesSlotFunction()
def submit():
    #print('Submit')
    print("Hi Hello")
    print(f"name={name.text()} position={position.text()} salary={salary.text()}  ")
    #query = "DELETE FROM employees;"
    #  ceo.method(aa1,aa2)
    #  ceo.method(string,tuple)
    #cursor.execute(query)

    query = "INSERT INTO employees (name, position, salary) VALUES (?, ?, ?);"
    #  ceo.method(aa1,aa2)
    #  ceo.method(string,tuple)
    cursor.execute(query, (name.text(), position.text(), salary.text()))
    conn.commit()
    
    showMsg("Employee Saved Successfully")
    pass
def update(row):
    #print("Row >>>>"+row
    print("Update")
    """
    UPDATE table_name
    SET column1 = value1, column2 = value2, ...
    WHERE condition;
    """
    #1. Build the query
    #TypeCasting
    #row = int(row)
    n = name.text()
    p = position.text()
    s = salary.text()
    print(n)
    #p = table.item(row,2).text()
    #s = table.item(row,3).text()
    query = f"UPDATE employees SET name='{n}',position='{p}',salary={s} WHERE id={rowid.text()}"
    print(query)
    #2. Execute the query
    cursor.execute(query)
    #3. Commit the query
    conn.commit()
    showMsg("Employee Updated Successfully")
    # DRY Dont Repeate Yourself
    
    pass
def myFunction(): # myFunction is writter in camelCase
    # get the rowid
    #
    if submit_button.text() =='Submit':
        submit()
    else:
        #print("Rowid >>>>>>>>>>>>"+rowid.text())
        #r=rowid.text()
        #print(r)
        update(20)
        

showemployees.clicked.connect(showEmployeesSlotFunction)



submit_button.clicked.connect(myFunction)#2 i am calling/invoking the function



# Set up layout
layout = QVBoxLayout()
layout.addWidget(name_label)
layout.addWidget(name)
layout.addWidget(position_label)
layout.addWidget(position)
layout.addWidget(salary_label)
layout.addWidget(salary)
layout.addWidget(submit_button)
layout.addWidget(showemployees)
layout.addWidget(table)
layout.setStretchFactor(table, 1)

# Set up window
window = QWidget()
window.setLayout(layout)
window.setWindowTitle('Employee Form')
#window.setGeometry(X,    Y,   W, H  )
window.setGeometry(500, 300, 600, 400)
# Function to resize the table
def resizeTable(event):
    table.resize(event.size().width(), event.size().height())

# Connect resize event to the resizeTable function
window.resizeEvent = lambda event: resizeTable(event)

# Show the window
window.show()
# I am calling the function 3rd time
showEmployeesSlotFunction()
sys.exit(app.exec())





