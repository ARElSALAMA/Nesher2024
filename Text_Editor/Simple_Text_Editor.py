#!/usr/bin/env python3
from tkinter import filedialog
import customtkinter as ctk


def save():
    # 'Save as' interface
    input_path = filedialog.asksaveasfilename(title='Save Text File',
                                              filetypes=(('TXT FILE', '.txt'), ('All Files', '*.*')))
    if input_path:
        if not input_path.endswith('.txt'):  # if .txt is not added, add it
            input_path = f'{input_path}.txt'

        main_text = text.get(1.0, 'end-1c')

        # save_as = entry_str.get()

        file = open(input_path, 'w')
        file.write(main_text)
        file.close()


def clear():
    text.delete('0.0', 'end')


# themes
ctk.set_appearance_mode('dark')

# Window
window = ctk.CTk()
window.title('Text Editor')
window.geometry('800x500+600+100')

# Text entry
text = ctk.CTkTextbox(master=window, width=790, height=425)
text.pack(pady=5)

# frame
frame = ctk.CTkFrame(master=window, fg_color='transparent')
frame.pack(pady=10)

# Buttons
save_button = ctk.CTkButton(master=frame, text='Save', command=save, height=40, corner_radius=10, font=('', 20))
save_button.pack(side='left', padx=5)

clear_button = ctk.CTkButton(master=frame, text='Clear', command=clear, fg_color='#706f6f', hover_color='#595959',
                             height=40,
                             corner_radius=10,
                             font=('', 20))
clear_button.pack(padx=10)

# run
window.mainloop()
