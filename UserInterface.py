from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("Compression Program")


def open_file_dialog():
    file_path_sv.set(filedialog.askopenfilename())
    if file_path_sv != "":
        compress_button.configure(state="active")


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
compress_button = Button(window, text='Compress', state="disabled")
compress_button.pack(padx=10, pady=10, side=LEFT)

result_label = Label(window)
result_label.pack(pady=10)


window.mainloop()
