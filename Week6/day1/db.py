import sqlite3
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()
print("Opened database successfully")

cursor.execute('''CREATE TABLE EMPLOYEE
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL);''')

      VALUES (1, 'Razi', 14')");
cursor.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,ADDRESS,MARKS) \
      VALUES (2, 'Jon', 19, 'Bangalore', 150 )");
cursor.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE) \
      VALUES (3, 'Martha', 35)");
conn.commit()


 