import mysql.connector

testDatabase = mysql.connector.connect(
    host = "localhost",
    user= "root",
    passwd = "",
    database = "ai stuff"
    )

interact = testDatabase.cursor()

