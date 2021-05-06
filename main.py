import tkinter
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
import eyed3
import configparser

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=400, height=0)
root.resizable(0,0)
audio_file = None
root.iconbitmap('src/icon32.ico')
root.title('GUID3')
file_chosen = False
settings = configparser.ConfigParser()
settings_file = settings.read('src/settings.ini')
window_color = settings['window_color']['window_hex']


def change_bg_color():
    color = askcolor(title="Tkinter Color Chooser")
    root.configure(bg=color[1])
    file_choose_label.config(bg=color[1])
    artist_label.config(bg=color[1])
    title_label.config(bg=color[1])
    album_label.config(bg=color[1])
    track_label.config(bg=color[1])
    color_string = ''.join(color[1])
    settings.set('window_color', 'window_hex', color_string)
    with open('src/settings.ini', 'w') as configfile:
        settings.write(configfile)
    return color


change_bg_color_button = tkinter.Button(root, text='Select a Color', command=change_bg_color)


def browse_files():
    global audio_file
    global file_chosen
    audio_file_path = askopenfilename(filetypes=(("Audio Files", "*.mp3"),))
    audio_file = eyed3.load(audio_file_path)
    file_chosen_label = tkinter.Label(root, text=audio_file_path)
    file_chosen_label.grid()
    file_chosen = True
    artist_entry.config(state='normal')
    title_entry.config(state='normal')
    album_entry.config(state='normal')
    track_entry.config(state='normal')
    return file_chosen, audio_file


def change_artist():
    if artist_name.get() == '':
        return
    else:
        audio_file.tag.artist = artist_name.get()
        audio_file.tag.save()


def change_title():
    if title_name.get() == '':
        return
    else:
        audio_file.tag.title = title_name.get()
        audio_file.tag.save()


def change_album():
    if album_name.get() == '':
        return
    else:
        audio_file.tag.album = album_name.get()
        audio_file.tag.save()


def change_track():
    try:
        if track_name.get() == '':
            return
        else:
            audio_file.tag.track_num = track_name.get()
            audio_file.tag.save()
    except ValueError as e:
        if str(e) == "invalid literal for int() with base 10: '" + track_name.get() + "'":
            messagebox.showerror(root, "You must enter a number for track number.")


def print_artist():
    try:
        messagebox.showinfo(root, 'Artist: ' + audio_file.tag.artist)
    except TypeError as t:
        if str(t) == 'can only concatenate str (not "NoneType") to str':
            messagebox.showerror(root, "This song is missing an artist tag.")
    except AttributeError as a:
        if str(a) == "'NoneType' object has no attribute 'tag'":
            messagebox.showerror(root, "Select a file before reading tags.")


def print_title():
    try:
        messagebox.showinfo(root, 'Title: ' + audio_file.tag.title)
    except TypeError as t:
        if str(t) == 'can only concatenate str (not "NoneType") to str':
            messagebox.showerror(root, "This song is missing a title tag.")
    except AttributeError as a:
        if str(a) == "'NoneType' object has no attribute 'tag'":
            messagebox.showerror(root, "Select a file before reading tags.")


def print_album():
    try:
        messagebox.showinfo(root, 'Album: ' + audio_file.tag.album)
    except TypeError as t:
        if str(t) == 'can only concatenate str (not "NoneType") to str':
            messagebox.showerror(root, "This song is missing a album tag.")
    except AttributeError as a:
        if str(a) == "'NoneType' object has no attribute 'tag'":
            messagebox.showerror(root, "Select a file before reading tags.")


def print_track():
    try:
        messagebox.showinfo(root, 'Track #: ' + audio_file.tag.track_num)
    except TypeError as t:
        if str(t) == 'can only concatenate str (not "NoneType") to str':
            messagebox.showerror(root, "This song is missing a track number tag.")
    except AttributeError as a:
        if str(a) == "'NoneType' object has no attribute 'tag'":
            messagebox.showerror(root, "Select a file before reading tags.")


def read_all():
    if file_chosen != True:
        messagebox.showerror(root, "Select a file before reading tags.")
        return
    else:
        print_artist()
        print_title()
        print_album()
        print_track()


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


def change_bg_color_startup():
    root.configure(bg=window_color)
    file_choose_label.config(bg=window_color)
    artist_label.config(bg=window_color)
    title_label.config(bg=window_color)
    album_label.config(bg=window_color)
    track_label.config(bg=window_color)
    settings['window_color']


if __name__ == "__main__":
    change_bg_color_startup()


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
read_tags = tkinter.Button(root, text="Read tags...", command=read_all)

with open('src/settings.ini', 'w') as configfile:
    settings.write(configfile)

change_bg_color_button.grid(sticky=tkinter.N+tkinter.E, row=2)
file_choose_label.grid(row=2)
file_choose.grid()
artist_label.grid()
artist_entry.grid()
title_label.grid()
title_entry.grid()
album_label.grid()
album_entry.grid()
track_label.grid()
track_entry.grid()
apply_button.grid()
read_tags.grid()
canvas.grid()
root.mainloop()
