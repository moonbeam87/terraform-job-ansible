import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE logDB")
mycursor.execute("CREATE TABLE logs (time VARCHAR(255), data VARCHAR(255))")