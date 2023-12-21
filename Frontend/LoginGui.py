import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from PIL import Image, ImageTk
from Backend.LoginBackend import Login
from Frontend.CustomerDashboard import CustomerDashboard
from Frontend.DriverDashboard import DriverDashboard
from RegistrationGui import RegistrationPage

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking System")
        self.root.geometry("1100x600+200+100")
        self.root.resizable(False, False)
        self.create_left_frame()
        self.create_right_frame()

    def create_left_frame(self):
        left_frame = tk.Frame(self.root, bg="lightblue", width=400, height=400)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        welcome_label = tk.Label(left_frame, text="Welcome to Taxi Booking System", font=("Helvetica", 20, "italic"), bg="lightblue")
        welcome_label.place(x=60, y=50)

        image = Image.open(r"C:\Users\USER\Desktop\Taxi3.Image.jpg")
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(left_frame, image=photo)
        image_label.image = photo
        image_label.place(x=22, y=130)

        today_date_label = tk.Label(left_frame, text="Today's Date:", font=("Arial", 16, "bold"), bg="#B1C381")
        today_date_label.place(x=50, y=490)

        date_str = datetime.now().strftime("%Y-%m-%d")
        date_label = tk.Label(left_frame, text=date_str, font=("Arial", 16, "bold"), bg="#B1C381")
        date_label.place(x=220, y=490)

        time_str = datetime.now().strftime("%H:%M:%S")
        time_label = tk.Label(left_frame, text="Time:", font=("Arial", 16, "bold"), bg="#B1C381")
        time_label.place(x=80, y=560)

        clock_label = tk.Label(left_frame, text=time_str, font=("Arial", 16, "bold"), bg="#B1C381")
        clock_label.place(x=220, y=560)

    def create_right_frame(self):
        right_frame = tk.Frame(self.root, bg="#F3EEEA", width=400, height=400)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        image1 = Image.open(r"C:\Users\USER\Desktop\images.jpg")
        photo1 = ImageTk.PhotoImage(image1)
        image_label = tk.Label(right_frame, image=photo1)
        image_label.image = photo1
        image_label.place(x=287, y=100)

        login_label = tk.Label(right_frame, text="LOGIN", font=("Arial", 20, "bold"), bg="white")
        login_label.place(x=280, y=190)

        user_label = tk.Label(right_frame, text="UserName:", font=("Arial", 12, "bold"), bg="white")
        user_label.place(x=100, y=300)

        self.user_entry = tk.Entry(right_frame, width=25, font=("Arial", 12, "bold"))
        self.user_entry.place(x=240, y=300)

        password_label = tk.Label(right_frame, text="Password:", font=("Arial", 12, "bold"), bg="white")
        password_label.place(x=100, y=360)

        self.password_entry = tk.Entry(right_frame, show="*", width=25, font=("Arial", 12, "bold"))
        self.password_entry.place(x=240, y=360)

        login_button = tk.Button(right_frame, text="Login", command=self.login_action, width=12, font=("Arial", 12),
                                 bg="blue", fg="white")
        login_button.place(x=220, y=450)

        signin_button = tk.Button(right_frame, text="Sign In", width=12, command=self.signin_action,
                                  font=("Arial", 12), bg="blue", fg="white")
        signin_button.place(x=360, y=450)

        forgot_label = tk.Label(right_frame, text="forgot your password??", font=("Arial", 12, "italic"), bg="white")
        forgot_label.place(x=300, y=500)

    def login_action(self):
        user_name = self.user_entry.get()
        password = self.password_entry.get()

        if not user_name or not password:
            messagebox.showinfo("Error", "Please enter both username and password.")
            return

        result, user_type = Login(UserName=user_name, Password=password)

        if result == "Login successful":
            messagebox.showinfo("Login Successful", "Welcome to our system, {}".format(user_name))
            self.root.destroy()

            if user_type == "Customer":
                root = tk.Tk()
                # Assuming CustomerDashboard is the dashboard for customers
                CustomerDashboard(root)
            elif user_type == "Driver":
                root = tk.Tk()
                DriverDashboard(root)
            else:
                messagebox.showinfo("Error", "Invalid UserType")
        else:
            messagebox.showinfo("Login Failed", "Incorrect UserName and Password")

    def signin_action(self):
        self.root.destroy()
        root = tk.Tk()
        RegistrationPage(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()
