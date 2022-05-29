from tkinter import *
from pytube import YouTube

def download_text():
    title = "Downloading..."
    Label(root, text=title, font="arial 15").pack()
    Download()
def Download():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED!', font = 'arial 15', foreground="green").pack()

root = Tk()
root.title("YouTube Video Downloader")
root.geometry("600x400")

Label(root, text="Paste the URL here: ",font="arial 20").pack()
link = StringVar()
e1 = Entry(root, textvariable=link, width="30", font="arial 15")
e1.pack()
Button(root, text="Download", font="arial 15",command=download_text).pack()

root.mainloop()