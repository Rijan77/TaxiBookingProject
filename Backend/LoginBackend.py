from Backend.Database import connect


def Login(UserName, Password):
    conn = None
    sql = """SELECT UserType FROM Users WHERE UserName=%s AND Password=%s"""
    result = None

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, (UserName, Password))
        user_type = cursor.fetchone()  # Fetch the UserType
        conn.commit()
        cursor.close()
        conn.close()

        if user_type:
            result = "Login successful", user_type[0]  # Return the result and UserType
        else:
            result = "Login failed", None

    except Exception as e:
        print("Error:", e)
        result = "Login failed", None

    finally:
        return result
