from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageDraw, ImageFont

class


def open_image():
    file = fd.askopenfilename(
        text="Choose file to watermark: ",
        filetypes=[('image files', '.png;.jpg'),  # nope,returns *.png;.jpg
                   ('image files!', '*.png;*.jpg')])
    file = file.replace('/', '\\\\')
    print(file)
    global img, img_for_changing, file_name
    img = ImageTk.PhotoImage(Image.open(file).resize((250, 250), Image.ANTIALIAS))
    img_for_changing = Image.open(file)
    file_name = file
    canvas.itemconfig(canvas_image, image=img)


def put_watermark():
    black = (3, 8, 12)
    pos = (10, 10)
    font = ImageFont.truetype("arial.ttf", 40)
    text = "wm"
    global img_for_changing, img, file_name
    img_for_changing = Image.open(file_name)
    drawing = ImageDraw.Draw(img_for_changing)
    drawing.text(pos, text, fill=black, font=font)
    save_name = fd.asksaveasfilename(
        text="Save file as: ",
        filetypes=[('image files', '.png;.jpg'),  # nope,returns *.png;.jpg
                   ('image files!', '*.png;*.jpg')]
    )
    save_name = save_name.replace('/', '\\\\')
    img_for_changing.save(save_name)
    img = ImageTk.PhotoImage(Image.open(save_name).resize((250, 250), Image.ANTIALIAS))
    canvas.itemconfig(canvas_image, image=img)


window = Tk()
file_button = Button(text="Open File",
                     command=open_image)
file_button.grid(column=0, row=0)

canvas = Canvas(highlightthickness=0, width=250)
img = ImageTk.PhotoImage(Image.open('fake_image.jpg').resize((250, 250), Image.ANTIALIAS))
img_for_changing = ImageTk.PhotoImage(Image.open('fake_image.jpg'))
file_name = 'fake_image.jpg'
canvas_image = canvas.create_image(125, 125, anchor=CENTER, image=img)
canvas.grid(column=0, row=1)

button = Button(text="Something", command=put_watermark)
button.grid(column=0, row=2)

window.mainloop()
