import sqlite3
import sys

from PyQt6.QtWidgets import QTableWidget,QTableWidgetItem, QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox # * means all module

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
    else:
        print("User clicked No, cancel the action.")    
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
        for col_num, col_data in enumerate(row_data):
            item = QTableWidgetItem(str(col_data))
            table.setItem(row_num, col_num, item)
        # Add buttons for each row
        #view_button = QPushButton('View')
        #edit_button = QPushButton('Edit')
        delete_button = QPushButton('Delete')
        
        button_layout = QVBoxLayout()
        #button_layout.addWidget(view_button)
        #button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)
        button_layout.setContentsMargins(0, 0, 0, 0)  # No margins

        buttons_widget = QWidget()
        buttons_widget.setLayout(button_layout)
        table.setCellWidget(row_num,len(column_names) - 1,buttons_widget)
        delete_button.clicked.connect(lambda _, row=row_num: deleteEmployee(row))
    
    table.show()
    pass

#1. Function defination
def myFunction(): # myFunction is writter in camelCase
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
    
    msgBox = QMessageBox()
    msgBox.setText("Employee Saved Successfully")
    msgBox.exec()
    pass

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
sys.exit(app.exec())





