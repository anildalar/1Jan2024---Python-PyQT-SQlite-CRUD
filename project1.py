import sqlite3
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox # * means all module

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

# Set up window
window = QWidget()
window.setLayout(layout)
window.setWindowTitle('Employee Form')
#window.setGeometry(X,    Y,   W, H  )
window.setGeometry(500, 300, 300, 200)

# Show the window
window.show()
sys.exit(app.exec())





