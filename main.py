import tkinter as tk

# Window stuff
window = tk.Tk()
window.title("Watermarker")
window.minsize(width=500, height=100)


# Set title heading
title_label = tk.Label(text="Watermarker: A watermarking tool")
title_label.grid(row=0, column=1)

# This keeps the window open. Make sure it stays at the bottom of the file
window.mainloop()