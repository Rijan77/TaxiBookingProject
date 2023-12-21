import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime



class DriverDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("Customer DashBoard")
        self.root.geometry("1200x800+130+2")
        self.root.resizable(False, False)

        self.Create_top_frame()
        self.Create_leftTop_frame()
        self.Create_left_frame()

    def Create_top_frame(self):
        top_frame = tk.Frame(self.root, bg="#96EFFF", width=1200, height=100)
        top_frame.place(x=0, y=0)

        today_date_label = tk.Label(top_frame, text="Today's Date:", font=("Arial", 15, "bold"), bg="#B1C381")
        today_date_label.place(x=320, y=15)

        date_str = datetime.now().strftime("%Y-%m-%d")
        date_label = tk.Label(top_frame, text=date_str, font=("Arial", 15, "bold"), bg="#B1C381")
        date_label.place(x=490, y=15)

        # Display current time
        time_str = datetime.now().strftime("%H:%M:%S")
        time_label = tk.Label(top_frame, text="Time:", font=("Arial", 14, "bold"), bg="#B1C381")
        time_label.place(x=1000, y=55)

        clock_label = tk.Label(top_frame, text=time_str, font=("Arial", 14, "bold"), bg="#B1C381")
        clock_label.place(x=1090, y=55)

    def Create_leftTop_frame(self):
        leftTop_frame = tk.Frame(self.root, bg="#DDF2FD", width=300, height=200)
        leftTop_frame.place(x=0, y=0)

        self.image1 = Image.open(r"C:\Users\USER\Desktop\default-avatar.png")
        self.photo1 = ImageTk.PhotoImage(self.image1)
        image_label = tk.Label(leftTop_frame, image=self.photo1, bg="#DDF2FD")
        image_label.place(x=80, y=10)

        label_1 = tk.Label(leftTop_frame, text="Hello Driver", font=("Arial", 20, "bold"), bg="#DDF2FD")
        label_1.place(x=40, y=150)





    def Create_left_frame(self):
        left_frame = tk.Frame(self.root, bg="#9BBEC8", width=300, height=800)
        left_frame.place(x=0, y=200)



        booking_button = tk.Button(left_frame, text="Make Booking", bg="#AFC8AD",width=16, fg="black", font=("Arila", 15, "bold"))
        booking_button.place(x=45, y=50)

        view_button = tk.Button(left_frame, text="View Booking", bg="#AFC8AD", width=16, fg="black",
                                   font=("Arila", 15, "bold"))
        view_button.place(x=45, y=130)

        update_button = tk.Button(left_frame, text="Update Booking", bg="#AFC8AD", width=16, fg="black",
                                   font=("Arila", 15, "bold"))
        update_button.place(x=45, y=210)

        cancel_button = tk.Button(left_frame, text="Cancel Booking", bg="#AFC8AD", width=16, fg="black",
                                   font=("Arila", 15, "bold"))
        cancel_button.place(x=45, y=290)

        logout_button = tk.Button(left_frame, text="LogOut", bg="#AFC8AD", width=13, fg="black",
                                  font=("Arila", 15, "bold"))
        logout_button.place(x=60, y=420)

if __name__ == "__main__":
    root = tk.Tk()
    app = DriverDashboard(root)
    root.mainloop()
