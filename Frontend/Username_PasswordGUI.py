import tkinter as tk
from PIL import Image, ImageTk


class UserName_Password:
    def __init__(self, root):
        self.root = root
        self.root.title("User and Password")
        self.root.geometry("650x570+250+80")
        self.root.resizable(False, False)
        self.root.configure(bg="#F2F1EB")

        self.username()

    def username(self):
        self.root.image = Image.open(r"C:\Users\USER\Desktop\421648.png")
        self.root.photo = ImageTk.PhotoImage(self.root.image)
        image_label = tk.Label(self.root, image=self.root.photo)
        image_label.place(x=250, y=30)

        username_label = tk.Label(self.root, text="UserName:", font=("Arial", 12, "bold"), bg="#EEE7DA")
        username_label.place(x=100, y=250)
        username_entry = tk.Entry(self.root, width=25, font=("Arial", 11, "bold"))
        username_entry.place(x=300, y=250)

        password_label = tk.Label(self.root, text="New Password:", font=("Arial", 12, "bold"), bg="#EEE7DA")
        password_label.place(x=100, y=300)
        password_entry = tk.Entry(self.root, width=25, show="*", font=("Arial", 11, "bold"))
        password_entry.place(x=300, y=300)

        conformpass_label = tk.Label(self.root, text="Conform Password:", font=("Arial", 12, "bold"), bg="#EEE7DA")
        conformpass_label.place(x=100, y=350)
        conformpass_entry = tk.Entry(self.root, width=25,show="*", font=("Arial", 11, "bold"))
        conformpass_entry.place(x=300, y=350)

        signup_button = tk.Button(self.root, text='SignUp', width=15, bg="#61A3BA", fg='black',
                                  font=("Arial", 11, "bold"))
        signup_button.place(x=270, y=420)

        backlogin_button = tk.Button(self.root, text='Back To Login', width=25, bg="#61A3BA", fg='black',
                                     command=self.action_backlogin,
                                     font=("Arial", 11, "bold"))
        backlogin_button.place(x=220, y=465)

    def action_backlogin(self):
        self.root.destroy()
        root1 = tk.Tk()
        from Login import LoginPage
        LoginPage(root1)


if __name__ == "__main__":
    root = tk.Tk()
    app = UserName_Password(root)
    root.mainloop()
