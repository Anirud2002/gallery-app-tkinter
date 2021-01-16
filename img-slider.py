from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images and Icons")
root.iconbitmap("apple.ico")

my_img1 = ImageTk.PhotoImage(Image.open("images/pic1.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/pic2.jpeg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/pic3.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/pic4.jpeg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/pic5.jpeg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label, button_forward, button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3)
    if image_number < 5:
        button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
        button_forward.grid(row=1, column=2)

        button_back = Button(root, text="<<", command=lambda: back(image_number))
        button_back.grid(row=1, column=0)
    else:
        image_number = 5
        button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1), state=DISABLED)
        button_forward.grid(row=1, column=2)

        button_back = Button(root, text="<<", command=lambda: back(image_number))
        button_back.grid(row=1, column=0)


def back(image_number):
    global my_label, button_forward, button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 2])
    my_label.grid(row=0, column=0, columnspan=3)
    if image_number == 2:
        image_number = 2
        button_forward = Button(root, text=">>", command=lambda: forward(image_number))
        button_forward.grid(row=1, column=2)

        button_back = Button(root, text="<<", command=lambda: back(image_number), state=DISABLED)
        button_back.grid(row=1, column=0)
    else:
        button_forward = Button(root, text=">>", command=lambda: forward(image_number))
        button_forward.grid(row=1, column=2)

        button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
        button_back.grid(row=1, column=0)


# buttons

button_back = Button(root, text="<<", command=back)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
