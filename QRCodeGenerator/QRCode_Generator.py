#!/usr/bin/env python3
from tkinter import *
from tkinter import filedialog
from PIL import Image
import qrcode
import customtkinter as ctk


# Functions
def generate_qr():
    # file dialogue
    input_path = filedialog.asksaveasfilename(title='Save Image',
                                              filetypes=(('PNG FILE', '.png'), ('All Files', '*.*')))
    if input_path:
        if not input_path.endswith('.png'):  # if .png is not added, add it
            input_path = f'{input_path}.png'
        # Create QR Code
        get_code = qrcode.make(entry.get())

        # Save as PNG
        get_code.save(input_path, format="PNG", size=5)

        # Put QR code on screen
        global get_image
        get_image = ctk.CTkImage(light_image=Image.open(input_path),
                                 dark_image=Image.open(input_path),
                                 size=(350, 350))
        # add image to label
        my_label.configure(image=get_image)

        # delete entry box
        entry.delete(0, END)
        # finished msg
        entry.insert(0, 'Finished')


def clear():
    entry.delete(0, END)
    my_label.configure(image='')


# theme
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('/Users/asalama/Documents/Nesher_Proj/Everything/GUIs/Apps/Themes/red.json')

# window
window = ctk.CTk()
window.title('QR Code Generator')
window.geometry('500x550+445+100')

# GUI
# entry box
entry = ctk.CTkEntry(master=window, font=('Helvetica', 18), width=350)
entry.pack(pady=20)

# Buttons
button = ctk.CTkButton(master=window, text='Generate', command=generate_qr, font=('', 20), height=40)
button.pack(pady=20)

button2 = ctk.CTkButton(master=window, text='Clear', command=clear, font=('', 20), height=40)
button2.pack()

# label
my_label = ctk.CTkLabel(master=window, text='')
my_label.pack(pady=20)

# run
window.mainloop()