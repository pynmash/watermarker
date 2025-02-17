import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageFont, ImageDraw

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.r, self.g, self.b = (255, 255, 255)
        self.filepath = ''
        pts = [num for num in range(1, 301)]

        # Set title heading
        self.title_label = tk.Label(text="Watermarker: A watermarking tool")
        self.title_label.grid(row=0, column=1, columnspan=3)


        # Set widgets
        self.file_label = tk.Label(text='Select a file:')
        self.selected_file_label = tk.Label(text="")
        self.open_file_button = tk.Button(text='Open File', command=self.open_file_dialog)
        self.watermark_text_label = tk.Label(text="Watermark text:")
        self.watermark_entry = tk.Entry()
        self.add_watermark_button = tk.Button(text='Go', command=self.add_watermark)
        self.pts_value = ttk.Combobox(values=pts, state='readonly', width=3, )
        self.pts_value.current(59)
        self.pts_label = tk.Label(text='Font size:')
        self.color_label = tk.Label(text='Text color:', fg='white')
        self.color_button = tk.Button(text='Choose color', command=self.choose_color)
        self.opacity_label = tk.Label(text='Opacity')
        self.opacity_slider = tk.Scale(from_=0, to=255)


        # Place widgets
        self.file_label.grid(row=1, column=0, sticky='E')
        self.selected_file_label.grid(row=1, column=1, columnspan=2)
        self.open_file_button.grid(row=1, column=3, sticky='E')
        self.watermark_text_label.grid(row=2, column=0, sticky='E')
        self.watermark_entry.grid(row=2, column=1, sticky='nsew')
        self.add_watermark_button.grid(row=2, column=3, sticky='E', padx=10)
        self.pts_label.grid(row=3, column=0, sticky='E')
        self.pts_value.grid(row=3, column=1, sticky='W')
        self.color_label.grid(row=3, column=2, sticky='E')
        self.color_button.grid(row=3, column=3, sticky='E')
        self.opacity_label.grid(row=0, column=4)
        self.opacity_slider.grid(row=2, column=4, rowspan=2, sticky='W')

    def open_file_dialog(self):
        file = filedialog.askopenfile()
        self.filepath = file.name
        self.selected_file_label.config(text=file.name)

    def choose_color(self):
        color_code = colorchooser.askcolor(title='Choose Color')
        self.color_label.config(fg=color_code[1])
        self.r, self.g, self.b = color_code[0]

    def add_watermark(self):
        text = self.watermark_entry.get()
        font_size = self.pts_value.get()
        image = Image.open(self.filepath).convert('RGBA')
        txt = Image.new('RGBA', image.size, (255,255,255,0))

        font = ImageFont.truetype('Arial', int(font_size))
        d = ImageDraw.Draw(txt)
        d.text((image.size[0]/2, image.size[1]/2), text, fill=(255,255,255,128), font=font)
        combined = Image.alpha_composite(image, txt)

        combined.show()


# Window stuff
window = App()
window.title("Watermarker")
window.minsize(width=500, height=100)
window.grid_columnconfigure(0, pad=20)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, pad=20)




# This keeps the window open. Make sure it stays at the bottom of the file
window.mainloop()