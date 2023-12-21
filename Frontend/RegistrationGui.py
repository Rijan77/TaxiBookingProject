import tkinter as tk
from tkinter import messagebox

from PIL import ImageTk
from PIL.Image import Image

from Backend.RegistrationBackend import Registration



class RegistrationPage:
    def __init__(self, root):
        self.email_entry = None
        self.name_entry = None
        self.contact_entry=None
        self.password_entry=None
        self.username_entry=None
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("800x750+200+10")
        self.root.resizable(False, False)
        self.root.configure(bg="#F8FFD2")

        self.create_widgets()

    def create_widgets(self):
        Registration_label = tk.Label(self.root, text="Registration Form", font=("Helvetica", 20, "bold"),
                                      bg="#F2FFE9")
        Registration_label.place(x=270, y=30)

        name_label = tk.Label(self.root, text="FullName:", font=("Arial", 11, "bold"), bg="#F2FFE9")
        name_label.place(x=160, y=150)
        self.name_entry = tk.Entry(self.root, width=25, font=("Arial", 11, "bold"))
        self.name_entry.place(x=350, y=150)

        email_label = tk.Label(self.root, text="Email:", font=("Arial", 11, "bold"), bg="#F2FFE9")
        email_label.place(x=160, y=210)
        self.email_entry = tk.Entry(self.root, width=25, font=("Arial", 11, "bold"))
        self.email_entry.place(x=350, y=210)

        contact_label = tk.Label(self.root, text="Contact Number:", font=("Arial", 11, "bold"), bg="#F2FFE9")
        contact_label.place(x=160, y=260)
        self.contact_var = tk.StringVar()# Using StringVar to control and validate the entry
        self.contact_var.trace_add("write", self.validate_contact_number)
        self.contact_entry = tk.Entry(self.root, textvariable=self.contact_var, width=25, font=("Arial", 11, "bold"))
        self.contact_entry.place(x=350, y=260)

        gender_label = tk.Label(self.root, text="Gender:", font=("Arial", 11, "bold"), bg="#F2FFE9")
        gender_label.place(x=160, y=310)
        self.vars = tk.IntVar()
        tk.Radiobutton(self.root, text="Male", padx=5, variable=self.vars, font=("Arial", 11, "bold"), value=1).place(
            x=350, y=310)
        tk.Radiobutton(self.root, text="Female", padx=20, variable=self.vars, font=("Arial", 11, "bold"),
                       value=2).place(x=430, y=310)

        country_label = tk.Label(self.root, text="Country:", font=("Arial", 11, "bold"), bg="#F2FFE9")
        country_label.place(x=160, y=360)
        country_list = ["Australia", "Canada", "China", "India", "Nepal", "UK", "USA"]
        self.cv = tk.StringVar()
        cnt_list=tk.OptionMenu(self.root, self.cv, *country_list)
        cnt_list.config(width=20, font=("Arial", 11, "bold"))
        self.cv.set("Select Your Country")
        cnt_list.place(x=350, y=360)

        payment_label = tk.Label(self.root, text="Payment Method:", font=("Arial", 11, "bold"), bg="#F2FFE9")
        payment_label.place(x=160, y=410)

        payment_list = ["Card", "Cheque", "Cash"]
        self.pi = tk.StringVar()
        pay_list = tk.OptionMenu(self.root, self.pi, *payment_list)
        pay_list.config(width=20, font=("Arial", 11, "bold"), bg="#F2FFE9")
        self.pi.set("Select Payment Method")
        pay_list.place(x=350, y=410)

        user_label = tk.Label(self.root, text="User Type:", font=("Arial", 11, "bold"), bg="#F2FFE9")
        user_label.place(x=160, y=460)

        user_list = ["Driver", "Customer"]
        self.usertype = tk.StringVar()
        pay_list = tk.OptionMenu(self.root, self.usertype, *user_list)
        pay_list.config(width=20, font=("Arial", 11, "bold"), bg="#F2FFE9")
        self.usertype.set("Select Your Type")
        pay_list.place(x=350, y=460)


        username_label = tk.Label(self.root, text="UserName:", font=("Arial", 12, "bold"), bg="#EEE7DA")
        username_label.place(x=160, y=510)
        self.username_entry = tk.Entry(self.root, width=25, font=("Arial", 11, "bold"))
        self.username_entry.place(x=350, y=510)

        password_label = tk.Label(self.root, text="New Password:", font=("Arial", 12, "bold"), bg="#EEE7DA")
        password_label.place(x=160, y=560)
        self.password_entry = tk.Entry(self.root, width=25, show="*", font=("Arial", 11, "bold"))
        self.password_entry.place(x=350, y=560)

        proceed_button = tk.Button(self.root, text='PROCEED', width=15, bg="black", fg='#F2FFE9',
                                   font=("Arial", 11, "bold"), command=self.proceed_action)
        proceed_button.place(x=340, y=620)

        backlogin_button = tk.Button(self.root, text='Back To Login', width=25, bg="#61A3BA", fg='black',
                                     command=self.action_backlogin,
                                     font=("Arial", 11, "bold"))
        backlogin_button.place(x=295, y=655)


    def action_backlogin(self):
        self.root.destroy()
        root1 = tk.Tk()
        from LoginGui import LoginPage
        LoginPage(root1)

    def proceed_action(self):
        # Retrieve values from the GUI
        full_name = self.name_entry.get()
        email = self.email_entry.get()
        contact_number = self.contact_entry.get()
        gender = "Male" if self.vars.get() == 1 else "Female"
        country = self.cv.get()
        payment_method = self.pi.get()
        user_type = self.usertype.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if '@' not in password and '#' not in password:
            messagebox.showerror("Error", "Password must contain at least one '@' or '#' character.")
            return

        if not email.lower().endswith('@gmail.com'):
            messagebox.showerror("Error", "Email must be in the format '@gmail.com'.")
            return


        result = Registration(full_name, email, contact_number, gender, country, payment_method, user_type, username,
                              password)

        messagebox.showinfo("Registration Compleate", result)

    def validate_contact_number(self, *args):
        contact_number = self.contact_entry.get()
        if len(contact_number) > 10:
            self.contact_var.set(contact_number[:10])




if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationPage(root)
    root.mainloop()
