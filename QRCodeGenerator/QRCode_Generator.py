import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode


# Functions
def generate_qr():
    # file dialogue
    input_path = filedialog.asksaveasfilename(title='Save Image', filetypes=(('PNG FILE', '.png'), ('All Files', '*.*')))
    if input_path:
        if not input_path.endswith('.png'):  # if .png is not added, add it
            input_path = f'{input_path}.png'
        # Create QR Code
        get_code = qrcode.make(entry.get())

        # Save as PNG using PIL's save method
        get_code.save(input_path, format="PNG", size=5)

        # Put QR code on screen
        global get_image
        get_image = ImageTk.PhotoImage(Image.open(input_path))
        # add image to label
        my_label.config(image=get_image)

        # delete entry box
        entry.delete(0, END)
        # finished msg
        entry.insert(0, 'Finished')


def clear():
    entry.delete(0, END)
    my_label.config(image='')


# window
window = tk.Tk()
window.title('QR Code Generator')
window.geometry('500x550')

# GUI
# entry box
entry = ttk.Entry(master=window, font=('Helvetica', 18))
entry.pack(pady=20)

# Buttons
button = ttk.Button(master=window, text='Generate', command=generate_qr)
button.pack()

button2 = ttk.Button(master=window, text='Clear', command=clear)
button2.pack()

# label
my_label = Label(master=window, text='')
my_label.pack(pady=20)

# run
window.mainloop()