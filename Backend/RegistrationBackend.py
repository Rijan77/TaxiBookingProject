# Update the backend module
from Backend.Database import connect
import sys


def Registration(fullName, email, contactNumber, gender, country, paymentMethod, userType, userName, password):
    conn = None
    sql = """INSERT INTO Users (FullName, Email, ContactNumber, Gender, Country, PaymentMethod, UserType, UserName, Password)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    result = None

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, (fullName, email, contactNumber, gender, country, paymentMethod, userType, userName, password))
        conn.commit()
        cursor.close()
        conn.close()
        result = "Registration successful"  # Success message

    except Exception as e:
        print("Error:", e)
        result = "Registration failed"  # Failure message

    finally:
        return result
