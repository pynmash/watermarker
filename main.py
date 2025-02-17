import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    file = filedialog.askopenfile()
    selected_file_label.config(text=file.name)

def do_the_thing():
    text = watermark_entry.get()
    selected_file_label.config(text=text)

# Window stuff
window = tk.Tk()
window.title("Watermarker")
window.minsize(width=500, height=100)


# Set title heading
title_label = tk.Label(text="Watermarker: A watermarking tool")
title_label.grid(row=0, column=1)

# Set widgets
file_label = tk.Label(text='Select a file:')
selected_file_label = tk.Label(text="")
open_file_button = tk.Button(window, text='Open File', command=open_file_dialog)
watermark_text_label = tk.Label(text="Watermark text:")
watermark_entry = tk.Entry()
add_watermark_button = tk.Button(window, text='Go', command=do_the_thing)

# Place widgets
file_label.grid(row=1, column=0, sticky='E')
selected_file_label.grid(row=1, column=1, columnspan=1)
open_file_button.grid(row=1, column=2)
watermark_text_label.grid(row=2, column=0, sticky='E')
watermark_entry.grid(row=2, column=1, sticky='nsew')
add_watermark_button.grid(row=2, column=2, sticky='E', padx=10)

# This keeps the window open. Make sure it stays at the bottom of the file
window.mainloop()