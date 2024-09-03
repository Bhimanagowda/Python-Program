import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="12345",database="student1")

mycursor=mydb.cursor()

mycursor.execute("select * from student1")

result=mycursor.fetchall()

for i in result:
  print(i)

print("Connected successfully")
