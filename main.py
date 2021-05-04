import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import eyed3

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=400, height=100)
audio_file = None
root.iconbitmap('src/icon32.ico')
root.title('GUID3')
file_chosen = False


def browse_files():
    global audio_file
    audio_file_path = askopenfilename(filetypes=(("Audio Files", "*.mp3"),))
    audio_file = eyed3.load(audio_file_path)
    file_chosen_label = tkinter.Label(root, text=audio_file_path)
    file_chosen_label.pack()
    file_chosen == True
    artist_entry.config(state='normal')
    title_entry.config(state='normal')
    album_entry.config(state='normal')
    track_entry.config(state='normal')
    return file_chosen, audio_file


def change_artist():
    audio_file.tag.artist = artist_name.get()
    audio_file.tag.save()

def change_title():
    audio_file.tag.title = title_name.get()
    audio_file.tag.save()

def change_album():
    audio_file.tag.album = album_name.get()
    audio_file.tag.save()

def change_track():
    try:
        audio_file.tag.track_num = track_name.get()
        audio_file.tag.save()
    except ValueError as e:
        if str(e) == "invalid literal for int() with base 10: '" + track_name.get() + "'":
            messagebox.showerror(root, "You must enter a number for track number.")


file_choose_label = tkinter.Label(root, text="Song file")
file_choose = tkinter.Button(root, text="Browse...", command=browse_files)

artist_label = tkinter.Label(root, text="Artist")
artist_name = tkinter.StringVar()
artist_entry = tkinter.Entry(root, textvariable=artist_name)

title_label = tkinter.Label(root, text="Title")
title_name = tkinter.StringVar()
title_entry = tkinter.Entry(root, textvariable=title_name)

album_label = tkinter.Label(root, text="Album")
album_name = tkinter.StringVar()
album_entry = tkinter.Entry(root, textvariable=album_name)

track_label = tkinter.Label(root, text="Track #")
track_name = tkinter.StringVar()
track_entry = tkinter.Entry(root, textvariable=track_name)

artist_entry.config(state='disabled')
title_entry.config(state='disabled')
album_entry.config(state='disabled')
track_entry.config(state='disabled')



def all_funcs():
    change_artist()
    change_title()
    change_album()
    change_track()

apply_button = tkinter.Button(root, text="Apply", command=all_funcs)

file_choose_label.pack()
file_choose.pack()
artist_label.pack()
artist_entry.pack()
title_label.pack()
title_entry.pack()
album_label.pack()
album_entry.pack()
track_label.pack()
track_entry.pack()
apply_button.pack()
canvas.pack()
root.mainloop()