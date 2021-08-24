from tkinter import *
from PIL import Image, ImageTk


class new_windows:
    def __init__(self, root):
        self.root = root
        self.root.title("login logout")
        self.root.geometry("1550x1550+0+0")

        img1 = Image.open("loginphoto.jpg")
        img1 = img1.resize((1600, 1000), Image.ANTIALIAS)  # makes picture more clear
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label_img1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        label_img1.place(x=0, y=0, width=1600, height=1000)

        label = Label(self.root, text="Welcome", font=("Franklin Gothic Heavy", 30, "bold"))
        label.place(x=700, y =200)



if __name__ == '__main__':
    root = Tk()
    obj = new_windows(root)
    root.mainloop()