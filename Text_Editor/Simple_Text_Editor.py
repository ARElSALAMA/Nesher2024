#!/usr/bin/env python3
#
import tkinter as tk
from tkinter import ttk


def save():
    main_text = text.get(1.0, 'end-1c')
    save_as = entry_str.get()

    file = open(F'/Users/asalama/Documents/Nesher_Proj/Everything/GUIs/Apps/Text_Editor/Saved_TXT/{save_as}.txt', 'w')
    file.write(main_text)
    file.close()


# Window
window = tk.Tk()
window.title('Text Editor')
window.geometry('800x500')

# Text entry
text = tk.Text(master=window, width=800, height=33)
text.pack()

# Label and Entry
label = ttk.Label(master=window, text='Save as:')
label.pack(side='left')
input_frame = tk.Frame(master=window)
entry_str = tk.StringVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_str)
entry.pack()
input_frame.pack(side='left')

# Button
button = ttk.Button(master=window, text='Save', command=save)
button.pack(side='left', padx=5)

# run
window.mainloop()
