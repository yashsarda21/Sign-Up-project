from tkinter import *
from tkinter import messagebox
import mysql.connector

class create_account_page:
    def __init__(self, root):
        self.root = root
        self.root.title("login logout")
        self.root.geometry("400x380+600+220")

        self.username = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.phoneNo = StringVar()


        frame_create_account = Frame(self.root, bd=6, bg="black", relief=RIDGE)
        frame_create_account.place(x=0, y=0, width=400, height=380)

        label_new_account = Label(frame_create_account, text="CREATE NEW ACCOUNT", fg="gold", bg="black", padx=4, pady=6, font=("Franklin Gothic Heavy", 23, "bold"))
        label_new_account.place(x=0, y=0)

        label_username = Label(frame_create_account, text="Username:", fg="gold", bg="black", font=("Franklin Gothic Heavy", 15, "bold"))
        label_username.place(x=10, y=70)
        Entry_usernmae = Entry(frame_create_account, width=20, textvariable=self.username, font=("Franklin Gothic Heavy", 15, "bold"))
        Entry_usernmae.place(x=150, y=70)

        label_passsword = Label(frame_create_account, text="Password :", fg="gold", bg="black", font=("Franklin Gothic Heavy", 15, "bold"))
        label_passsword.place(x=10, y=120)
        Entry_password = Entry(frame_create_account, width=20, textvariable=self.password, show="*", font=("Franklin Gothic Heavy", 15, "bold"))
        Entry_password.place(x=150, y=120)

        label_email = Label(frame_create_account, text="Email:", fg="gold", bg="black", font=("Franklin Gothic Heavy", 15, "bold"))
        label_email.place(x=10, y=170)
        Entryemail = Entry(frame_create_account, width=20, textvariable=self.email, font=("Franklin Gothic Heavy", 15, "bold"))
        Entryemail.place(x=150, y=170)

        label_Phone_Number = Label(frame_create_account, text="PhoneNo:", fg="gold", bg="black", font=("Franklin Gothic Heavy", 15, "bold"))
        label_Phone_Number.place(x=10, y=220)
        EntryPhone_Number = Entry(frame_create_account, textvariable=self.phoneNo, width=20, font=("Franklin Gothic Heavy", 15, "bold"))
        EntryPhone_Number.place(x=150, y=220)

        sign_up_btn =  Button(frame_create_account, text="Sign Up", command=self.sign_up,  font=("Franklin Gothic Heavy", 12, "bold"), bg="black", fg="gold", width=10)
        sign_up_btn.place(x=150, y=280)

    def sign_up(self):
        if self.password.get() == "":
            messagebox.showerror("Error", "Please Enter the Details", parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host="localhost", username="root", password="yashprem", database="yash123")
                mycursor = connection.cursor()
                mycursor.execute(("INSERT INTO account_details values(%s,%s,%s,%s)"), (
                    self.username.get(),
                    self.password.get(),
                    self.email.get(),
                    self.phoneNo.get(),
                ))
                connection.commit()
                connection.close()
                messagebox.showinfo("Success", "account has been created")
                self.username.set("")
                self.password.set("")
                self.email.set("")
                self.phoneNo.set("")
            except Exception as es:
                messagebox.showerror(("Warning", f"something went Wrong {str(es)}"), parent=self.root)

if __name__ == '__main__':
    root = Tk()
    obj = create_account_page(root)
    root.mainloop()