import tkinter as tk
from tkinter import messagebox

from Backend.RegistrationBackend import Registration
from Middleware.RegistrationLiberary import CustomerLibs
from UserName_Password import UserName_Password


class RegistrationPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("800x700+200+30")
        self.root.resizable(False, False)
        self.root.configure(bg="#F8FFD2")

        self.create_widgets()

    def create_widgets(self):
        Registration_label = tk.Label(self.root, text="Registration Form", font=("Helvetica", 20, "bold"),
                                      bg="#F2FFE9")
        Registration_label.place(x=270, y=30)

        name_label = tk.Label(self.root, text="FullName:", font=("Arial", 11, "bold"), bg="#F2FFE9")
        name_label.place(x=160, y=150)
        name_entry = tk.Entry(self.root, width=25, font=("Arial", 11, "bold"))
        name_entry.place(x=350, y=150)

        email_label = tk.Label(self.root, text="Email:", font=("Arial", 11, "bold"), bg="#F2FFE9")
        email_label.place(x=160, y=210)
        email_entry = tk.Entry(self.root, width=25, font=("Arial", 11, "bold"))
        email_entry.place(x=350, y=210)

        contact_label = tk.Label(self.root, text="Contact Number:", font=("Arial", 11, "bold"), bg="#F2FFE9")
        contact_label.place(x=160, y=260)
        contact_entry = tk.Entry(self.root, width=25, font=("Arial", 11, "bold"))
        contact_entry.place(x=350, y=260)

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

        proceed_button = tk.Button(self.root, text='PROCEED', width=15, bg="black", fg='#F2FFE9', font=("Arial", 11, "bold"), command=self.proceed_action   )
        proceed_button.place(x=210, y=560)

        cancel_button = tk.Button(self.root, text='CANCEL', width=15, bg="black", fg='#F2FFE9',
                                   font=("Arial", 11, "bold"))
        cancel_button.place(x=410, y=560)

    def proceed_action(self):
        self.root.destroy()
        root = tk.Tk()
        UserName_Password(root)

    def proceed_action(self, name_entry, email_entry, contact_entry):
        # Collect data from the registration form
        full_name = name_entry.get()
        email = email_entry.get()
        contact_number = contact_entry.get()
        gender = self.vars.get()
        country = self.cv.get()
        payment_method = self.pi.get()

        # Assume you have a method in your Database module for registration
        result = Registration(full_name, email, contact_number, gender, country, payment_method, self.usertype.get())

        if result == "Success":
            messagebox.showinfo("Success", "Registration successful!")
        else:
            messagebox.showerror("Error", "Registration failed.")

        # Now you can proceed to the UserName_Password GUI
        self.root.destroy()
        root = tk.Tk()
        UserName_Password(root)


if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationPage(root)
    root.mainloop()
