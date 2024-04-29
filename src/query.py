import mysql.connector
import streamlit as st

#connection

conn = mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    passwd = "", 
    db = "mydb"
)

c = conn.cursor()

# fetching the data

def view_my_data():
    c.execute('select * from insurance order by id asc')
    data = c.fetchall()
    return data