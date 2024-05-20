#!/usr/bin/env python3
import customtkinter as ctk
from subprocess import call
import threading

# seth the button width
BUTTON_WIDTH = 200


def run_script(script_path):
    def target():
        call(['Python', script_path])

    thread = threading.Thread(target=target)
    thread.start()


def km_mi():
    run_script('Converters/Km-to-Mi/km_to_mi.py')


def mi_km():
    run_script('Converters/Mi-to-Km/mi_to_km.py')


def qrcode():
    run_script('QRCodeGenerator/QRCode_Generator.py')


def text_editor():
    run_script('Text_Editor/Simple_Text_Editor.py')


# Themes
ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('Themes/orange.json')

# Setting the Window
window = ctk.CTk()
window.title('Nesher 2024')
window.geometry('500x500+200+100')
# set minimum size
window.minsize(300, 200)
# attributes
window.attributes('-alpha', 0.99)

# Title
title = ctk.CTkLabel(master=window, text='Nesher 2024', font=('', 40))
title.pack(pady=10)

# buttons
km_mi_button = ctk.CTkButton(master=window,
                             text='Kilometers to Miles',
                             command=km_mi,
                             corner_radius=10,
                             height=50,
                             fg_color='#c99532',
                             hover_color='#a17627',
                             font=('', 20),
                             width=BUTTON_WIDTH)
km_mi_button.pack(pady=20)

mi_km_button = ctk.CTkButton(master=window,
                             text='Miles to Kilometers',
                             command=mi_km,
                             height=50,
                             font=('', 20),
                             width=BUTTON_WIDTH)
mi_km_button.pack(pady=20)

qrcode_button = ctk.CTkButton(master=window,
                              text='QR Code Generator',
                              command=qrcode,
                              height=50,
                              font=('', 20),
                              width=BUTTON_WIDTH)
qrcode_button.pack(pady=20)

text_editor_button = ctk.CTkButton(master=window,
                                   text='Text Editor',
                                   command=text_editor,
                                   height=50,
                                   font=('', 20),
                                   width=BUTTON_WIDTH)
text_editor_button.pack(pady=20)


# mainloop
window.mainloop()
