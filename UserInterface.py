import ctypes
import subprocess
import os
from tkinter import *
from tkinter import filedialog


window = Tk()
window.title("Compression Program")

c_lib = ctypes.cdll.LoadLibrary('Cfiles/Clib.so')


def open_file_dialog():
    file_path_sv.set(filedialog.askopenfilename())
    if file_path_sv != "":
        compress_button.configure(state="active")


def compress_button_clicked():
    head = os.path.split(file_path_sv.get())
    dest_path = os.path.join(head[0], "HuffmanCodes.txt")
    if file_path_sv != "":
        c_lib.main(file_path_sv.get(), dest_path)


# File input
file_path_sv = StringVar()
open_file_button = Button(window, text="Choose a file", command=open_file_dialog)
open_file_button.pack(padx=10, pady=10, side=LEFT)


# File path display
file_path_display = Entry(textvariable=file_path_sv, width=50)
file_path_display.pack(padx=10, pady=10, side=LEFT)


# Compression button
button_state_sv = StringVar(value="disabled")
compress_button_sv = StringVar()
compress_button_sv.set('Compress')
compress_button = Button(window, text='Compress', command=compress_button_clicked, state="disabled")
compress_button.pack(padx=10, pady=10, side=LEFT)

result_label = Label(window)
result_label.pack(pady=10)


window.mainloop()
