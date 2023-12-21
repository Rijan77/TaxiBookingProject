# from tkinter import messagebox
#
# import mysql
#
#
# class CRUDOperation:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("CRUD Application")
#
#
#             self.db = mysql.connector.connect(
#                 host="localhost",
#                 port=3306,
#                 user="root",
#                 password="Rijan8314",
#                 database="taxibookingsystem" #Create a database named Hotel in your MySql Server
#             )
#             self.cursor = self.db.cursor()


import mysql.connector

class CRUDOperation:
    def __init__(self, root):
        self.root = root

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Rijan8314"
        )
        self.mycursor = self.mydb.cursor()

        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS taxibookingsystem")

        self.mycursor.execute("CREATE TABLE Users (userId int(50) PRIMARY KEY, FullName VARCHAR(255) NOT NULL, Email VARCHAR(255) NOT NULL , ContactNumber VARCHAR(255)NOT NULL , Gender VARCHAR(255), Country VARCHAR(255) NOT NULL , PaymentMethod VARCHAR(255), User VARCHAR(255))")

# crud_instance = CRUDOperation("example_root")


