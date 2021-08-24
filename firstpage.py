from tkinter import *
from PIL import Image, ImageTk
from createaccount import create_account_page
from newwindow import new_windows
import mysql.connector
from tkinter import messagebox

class login_logout_page:
    def __init__(self, root):
        self.root = root
        self.root.title("login logout")
        self.root.geometry("1550x1550+0+0")

        self.username = StringVar()
        self.password = StringVar()

    # uploading Background image
        img1 = Image.open("loginphoto.jpg")
        img1 = img1.resize((1600, 1000), Image.ANTIALIAS)# makes picture more clear
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label_img1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        label_img1.place(x=0, y=0, width=1600, height=1000)


    # creating a login stuff frame
        frame_login = Frame(self.root, bd=4, bg="black", relief=RIDGE)
        frame_login.place(x=600, y=200, width=400, height=400)

        label_login = Label(frame_login, text="LOGIN", fg="gold", bg="black", padx=2, pady=6, font=("Franklin Gothic Heavy", 30, "bold"))
        label_login.place(x=120, y=0, width=170)

        label_username = Label(frame_login, text="USERNAME :", fg="gold", bg="black", padx=2, pady=6, font=("Franklin Gothic Heavy", 15, "bold"))
        label_username.place(x=40, y=100, width=200)
        Entry_usernmae = Entry(frame_login, textvariable=self.username,  width=300, font=("Franklin Gothic Heavy", 15, "bold"))
        Entry_usernmae.place(x=80, y=140, width=300)

        img2 = Image.open("userphoto.png")
        img2 = img2.resize((60, 60), Image.ANTIALIAS)  # makes picture more clear
        self.photoimg2 = ImageTk.PhotoImage(img2)

        label_img2 = Label(frame_login, image=self.photoimg2, bd=2)
        label_img2.place(x=5, y=110, width=60, height=60)


        label_passsword = Label(frame_login, text="PASSWORD :", fg="gold", bg="black", padx=2, pady=6, font=("Franklin Gothic Heavy", 15, "bold"))
        label_passsword.place(x=40, y=190, width=200)
        Entry_password = Entry(frame_login, width=23, textvariable=self.password, show="*", font=("Franklin Gothic Heavy", 15, "bold"))
        Entry_password.place(x=80, y=230, width=300)

        img3 = Image.open("password.png")
        img3 = img3.resize((60, 60), Image.ANTIALIAS)  # makes picture more clear
        self.photoimg3 = ImageTk.PhotoImage(img3)

        label_img3 = Label(frame_login, image=self.photoimg3, bd=4, relief=RIDGE)
        label_img3.place(x=5, y=200, width=60, height=60)


        #creating button for new user

        login_btn = Button(frame_login, text="Log in", command=self.log_in, font=("Franklin Gothic Heavy", 15, "bold"), bg="black", fg="gold", width=10)
        login_btn.place(x=120, y=290)

        newuser_btn = Button(frame_login, text="New User?", command=newuser, font=("Franklin Gothic Heavy", 12, "bold"), bg="black", fg="gold", width=10)
        newuser_btn.place(x=10, y=350)

        newuser_btn = Button(frame_login, text="forgot password?", font=("Franklin Gothic Heavy", 12, "bold"), bg="black", fg="gold", width=15)
        newuser_btn.place(x=210, y=350)

    def log_in(self):
        connection = mysql.connector.connect(host="localhost", username="root", password="yashprem", database="yash123")
        mycursor = connection.cursor()
        mycursor.execute("SELECT Username,Password FROM account_details")
        rows = mycursor.fetchall()
        #checking if the pasword is valid or not then opening new window else showing error
        for i in range(len(rows)):
            if rows[i][0] == self.username.get() and rows[i][1] == self.password.get():
                self.new_window = Toplevel(self.root)
                self.app = new_windows(self.new_window)
                break
            elif i == len(rows)-1 and (rows[i][0] != self.username.get() or rows[i][1] != self.password.get()):
                messagebox.showerror("Error", "Entered username and passsword is invalid")
        self.username.set("")
        self.password.set("")

def newuser():
    new_window = Toplevel(root)
    app = create_account_page(new_window)



if __name__ == '__main__':
    root = Tk()
    obj = login_logout_page(root)
    root.mainloop()