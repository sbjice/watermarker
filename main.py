from tkinter import *
from tkinter import filedialog as fd
from tkinter import colorchooser
from PIL import Image, ImageTk, ImageDraw, ImageFont


class Watermarker:
    def __init__(self):
        self.img = None
        self.img_for_change = None
        self.filename = ''
        self.window = Tk()
        self.color = (3, 8, 12)
        self.window.title = "Watermarker App"

        self.file_button = Button(text="Open File",
                                  command=self.open_image)
        self.file_button.grid(column=0, row=0)

        self.canvas = Canvas(highlightthickness=0, width=250)
        self.img = ImageTk.PhotoImage(Image.open('fake_image.jpg').resize((250, 250), Image.ANTIALIAS))
        self.img_for_changing = ImageTk.PhotoImage(Image.open('fake_image.jpg'))
        self.file_name = 'fake_image.jpg'
        self.canvas_image = self.canvas.create_image(125, 125, anchor=CENTER, image=self.img)
        self.canvas.grid(column=0, row=1)

        self.watermark_input = StringVar()
        self.entry = Entry(textvariable=self.watermark_input)
        self.entry.grid(column=0, row=2)

        self.color_button = Button(
            text="Select color",
            command=self.choose_color)
        self.color_button.grid(column=0, row=3)

        self.button = Button(text="Save with watermark", command=self.put_watermark)
        self.button.grid(column=0, row=4)
        self.watermark_text = "WM"
        self.pos = (10, 10)
        self.font = ImageFont.truetype("arial.ttf", 40)

        self.window.mainloop()

    def open_image(self):
        file = fd.askopenfilename()
        file = file.replace('/', '\\\\')
        print(file)
        self.img = ImageTk.PhotoImage(Image.open(file).resize((250, 250), Image.ANTIALIAS))
        self.img_for_changing = Image.open(file)
        self.file_name = file
        self.canvas.itemconfig(self.canvas_image, image=self.img)

    def set_watermark_text(self):
        if self.watermark_input.get() == '':
            self.watermark_text = "WM"
        else:
            self.watermark_text = self.watermark_input.get()

    def put_watermark(self):
        self.set_watermark_text()
        self.img_for_changing = Image.open(self.file_name)
        drawing = ImageDraw.Draw(self.img_for_changing)
        drawing.text(self.pos, self.watermark_text, fill=self.color, font=self.font)
        save_name = fd.asksaveasfilename().replace('/', '\\\\')
        rgb_im = self.img_for_changing.convert('RGB')
        rgb_im.save(save_name)
        self.img = ImageTk.PhotoImage(Image.open(save_name).resize((250, 250), Image.ANTIALIAS))
        self.canvas.itemconfig(self.canvas_image, image=self.img)

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose color")[0]
        self.color = tuple([int(i) for i in color])


if __name__ == "__main__":
    wm = Watermarker()
