from pytube import YouTube

import os
from tkinter import *
from tkinter import filedialog

# Global Variable
PATH = ""
URL = ""


def download_video():
    global PATH
    global URL
    URL = url_text.get()
    try:
        yt = YouTube(URL)
    except Exception as e:
        message_label.delete(0)
        message_label.insert(0, "ERROR: Check if You entered valid URL")
        return

    stream = yt.streams.filter(
        progressive=True, file_extension='mp4').order_by('resolution')[-1]

    try:
        # downloading the video
        message_label.delete(0)
        stream.download(PATH)
        message_label.insert(0, "Download Completed Successfully")
    except Exception as e:
        print("Some Error!", e)
        message_label.delete(0)
        message_label.insert(
            0, "ERROR: Download FAILED! Check your internet connection")


def exit_application():
    app.destroy()


def choose_directory():
    global PATH
    currdir = os.getcwd()
    newdir = filedialog.askdirectory(
        parent=app, initialdir=currdir, title='Please select a directory')
    if len(newdir) > 0:
        pass
    PATH = newdir
    path_selected.config(text=PATH)


# Create a window
app = Tk()

app.title("YouTube Video Downloader")
app.geometry("900x500")


# Video Url
url_text = StringVar()
url_label = Label(app, text='Enter Video Url: ',
                  font=('bold', 14), pady=50, padx=40)
url_label.grid(row=3, column=0, sticky=W)
url_entry = Entry(app, textvariable=url_text, width=50)
url_entry.grid(row=3, column=1)


# Choose Path to save video
path_label = Label(app, text='Path to Save: ',
                   font=('bold', 14), pady=50, padx=40)
path_label.grid(row=4, column=0, sticky=W)

path_selected = Label(app, text="Choose Directory", pady=50)
path_selected.grid(row=4, column=1)

path_btn = Button(app, text="Select",
                  width=15, command=choose_directory)
path_btn.grid(row=4, column=2)


# Buttons
download_btn = Button(app, text="Download", width=12, command=download_video)
download_btn.grid(row=5, column=1, pady=20)

exit_btn = Button(app, text="Exit App", width=12, command=exit_application)
exit_btn.grid(row=5, column=2, pady=20)


# Message Box
message_label = Listbox(app, font=('bold', 10), height=8, width=50, border=0)
message_label.grid(row=6, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Start the program
app.mainloop()
