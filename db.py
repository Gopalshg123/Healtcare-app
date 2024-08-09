import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  
            user='root',  
            password='root',  
            database='HealthcareApp'  
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None