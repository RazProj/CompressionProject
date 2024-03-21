import os.path
import zipfile
from tkinter import *
from TkinterDnD2 import *


def drop(event):
    file_path = event.data[1:-1]
    file_entry_sv.set(file_path)
    compress_button.configure(state="active")


def compress_file():
    compress_button.configure(state="disabled")
    file_path = file_entry_sv.get()
    desktop_path = os.path.join(os.path.expanduser("~"), 'OneDrive', 'Desktop')
    file_name = os.path.basename(file_path)
    file_name_no_ext, file_extension = os.path.splitext(file_name)
    zip_file_path = os.path.join(desktop_path, f"{file_name_no_ext}.zip")
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        zipf.write(file_path, file_name)
    result_label.config(text=f"File '{file_name}' compressed successfully to desktop.")


window = TkinterDnD.Tk()
window.title("Compression Program")


# File input
file_entry_sv = StringVar()
file_entry_sv.set('Drop .txt files Here...')
file_entry = Entry(window, textvariable=file_entry_sv)
file_entry.pack(fill=X, padx=10, pady=10)
file_entry.drop_target_register(DND_FILES)
file_entry.dnd_bind('<<Drop>>', drop)


# Compression button
button_state_sv = StringVar(value="disabled")
compress_button_sv = StringVar()
compress_button_sv.set('Compress')
compress_button = Button(window, text='Compress', command=compress_file, state="disabled")
compress_button.pack(padx=10, pady=10)

result_label = Label(window)
result_label.pack(pady=10)


window.mainloop()
