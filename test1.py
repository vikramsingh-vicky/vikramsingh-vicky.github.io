import pypyodbc as odbc
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'localhost\SQLEXPRESS'
DATABASE_NAME = 'Intranet'
# uid="intranet_ho";
# pwd="Vicky@#1989";
connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
    
"""
conn = odbc.connect(connection_string)
print(conn)
# query_string = '''CREATE TABLE employees (
#     id INT PRIMARY KEY,
#     name VARCHAR(50),
#     department VARCHAR(50),
#     salary DECIMAL(10,2)
#     );
# '''
cursor = conn.cursor()
# cursor.execute(query_string)
sql = '''
INSERT INTO employees (id, name, department, salary)
VALUES (?, ?, ?, ?);
'''

# Define the data to be inserted into the table
data = [(4, 'John Doe', 'Sales', 50000.00),
        (5, 'Jane Smith', 'Marketing', 60000.00),
        (6, 'Bob Johnson', 'IT', 70000.00)]

# Execute the SQL query and pass in the data to be inserted
cursor.executemany(sql, data)
conn.commit()
cursor.close()