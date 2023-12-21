import tkinter as tk
from PIL import Image, ImageTk



class CustomerDashboard:

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

    def Create_leftTop_frame(self):
        leftTop_frame = tk.Frame(self.root, bg="#DDF2FD", width=300, height=200)
        leftTop_frame.place(x=0, y=0)

        self.image1 = Image.open(r"C:\Users\USER\Desktop\default-avatar.png")
        self.photo1 = ImageTk.PhotoImage(self.image1)
        image_label = tk.Label(leftTop_frame, image=self.photo1, bg="#DDF2FD")
        image_label.place(x=80, y=10)

        label_1 = tk.Label(leftTop_frame, text="Hello", font=("Arial", 20, "bold"), bg="#DDF2FD")
        label_1.place(x=40, y=150)



    def Create_left_frame(self):
        left_frame = tk.Frame(self.root, bg="#9BBEC8", width=300, height=800)
        left_frame.place(x=0, y=200)



        booking_button = tk.Button(left_frame, text="Make Booking", bg="Black", fg="White")
        booking_button.place(x=15, y=350)

    #     self.creatDashboard()
    #
    # def creatDashboard(self):
    #     customer_label = tk.Label(self.root, text="Customer DashBoard", font=("Arial", 16, "bold"), fg='blue')
    #     customer_label.place(x=200, y=100)


if __name__ == "__main__":
    root = tk.Tk()
    app = CustomerDashboard(root)
    root.mainloop()
