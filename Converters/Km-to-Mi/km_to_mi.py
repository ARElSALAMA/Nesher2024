#!/usr/bin/env python3
import tkinter as tk
import customtkinter as ctk


def convert():
    km_input = float(entry_int.get())
    mi_output = km_input * 0.62137
    output_string.set(str(mi_output))


# Theme
ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('green')

# Window
window = ctk.CTk()
window.title('KM to MI Converter')
window.geometry('400x200+700+100')
window.minsize(350, 150)

# title
title_label = ctk.CTkLabel(master=window,
                           text='Kilometers to Miles',
                           font=('', 20),
                           fg_color='transparent')
title_label.pack()

# input field
input_frame = ctk.CTkFrame(master=window, fg_color='transparent')
entry_int = tk.StringVar()
entry = ctk.CTkEntry(master=input_frame,
                     textvariable=entry_int,
                     placeholder_text='Enter a number',
                     width=175,
                     height=30)
button = ctk.CTkButton(master=input_frame,
                       text='Convert',
                       command=convert,
                       corner_radius=7,
                       height=30,
                       font=('', 20))
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ctk.CTkLabel(master=window,
                            text='Output',
                            font=('', 20),
                            textvariable=output_string)
output_label.pack(pady=5)

# Run
window.mainloop()
