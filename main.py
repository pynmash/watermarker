import tkinter as tk
from tkinter import filedialog

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set title heading
        self.title_label = tk.Label(text="Watermarker: A watermarking tool")
        self.title_label.grid(row=0, column=1)

        # Set widgets
        self.file_label = tk.Label(text='Select a file:')
        self.selected_file_label = tk.Label(text="")
        self.open_file_button = tk.Button(text='Open File', command=self.open_file_dialog)
        self.watermark_text_label = tk.Label(text="Watermark text:")
        self.watermark_entry = tk.Entry()
        self.add_watermark_button = tk.Button(text='Go', command=self.do_the_thing)

        # Place widgets
        self.file_label.grid(row=1, column=0, sticky='E')
        self.selected_file_label.grid(row=1, column=1, columnspan=1)
        self.open_file_button.grid(row=1, column=2)
        self.watermark_text_label.grid(row=2, column=0, sticky='E')
        self.watermark_entry.grid(row=2, column=1, sticky='nsew')
        self.add_watermark_button.grid(row=2, column=2, sticky='E', padx=10)

    def open_file_dialog(self):
        file = filedialog.askopenfile()
        self.selected_file_label.config(text=file.name)

    def do_the_thing(self):
        text = self.watermark_entry.get()

    def add_watermark(self):
        pass

# Window stuff
window = App()
window.title("Watermarker")
window.minsize(width=500, height=100)
window.grid_columnconfigure(0, pad=20)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, pad=20)




# This keeps the window open. Make sure it stays at the bottom of the file
window.mainloop()