# Update the database connection code
import mysql.connector
import sys


def connect():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Rijan8314",
            database="TaxiBookingSystem"
        )
    except Exception as e:
        print("Error:", e)

    finally:
        return conn
