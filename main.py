from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageDraw, ImageFont

class Watermarker:
    def __init__(self):
        self.img = None
        self.img_for_change = None
        self.filename = ''
        self.window = Tk()

        self.file_button = Button(text="Open File",
                                  command=self.open_image)
        self.file_button.grid(column=0, row=0)

        self.canvas = Canvas(highlightthickness=0, width=250)
        self.img = ImageTk.PhotoImage(Image.open('fake_image.jpg').resize((250, 250), Image.ANTIALIAS))
        self.img_for_changing = ImageTk.PhotoImage(Image.open('fake_image.jpg'))
        self.file_name = 'fake_image.jpg'
        self.canvas_image = self.canvas.create_image(125, 125, anchor=CENTER, image=self.img)
        self.canvas.grid(column=0, row=1)

        self.button = Button(text="Save with watermark", command=self.put_watermark)
        self.button.grid(column=0, row=2)

        self.window.mainloop()

    def open_image(self):
        file = fd.askopenfilename()
        file = file.replace('/', '\\\\')
        print(file)
        self.img = ImageTk.PhotoImage(Image.open(file).resize((250, 250), Image.ANTIALIAS))
        self.img_for_changing = Image.open(file)
        self.file_name = file
        self.canvas.itemconfig(self.canvas_image, image=self.img)

    def put_watermark(self):
        black = (3, 8, 12)
        pos = (10, 10)
        font = ImageFont.truetype("arial.ttf", 40)
        text = "wm"
        self.img_for_changing = Image.open(self.file_name)
        drawing = ImageDraw.Draw(self.img_for_changing)
        drawing.text(pos, text, fill=black, font=font)
        save_name = fd.asksaveasfilename()
        save_name = save_name.replace('/', '\\\\')
        rgb_im = self.img_for_changing.convert('RGB')
        rgb_im.save(save_name)
        self.img = ImageTk.PhotoImage(Image.open(save_name).resize((250, 250), Image.ANTIALIAS))
        self.canvas.itemconfig(self.canvas_image, image=self.img)


if __name__ == "__main__":
    wm = Watermarker()
