import sqlite3

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

query = "DELETE FROM employees;"
#  ceo.method(aa1,aa2)
#  ceo.method(string,tuple)
cursor.execute(query)

query = "INSERT INTO employees (name, position, salary) VALUES (?, ?, ?);"
#  ceo.method(aa1,aa2)
#  ceo.method(string,tuple)
cursor.execute(query, ("Anil", 'Director', 50000.00))
cursor.execute(query, ("Sunil", 'MD', 70000.50))
conn.commit()