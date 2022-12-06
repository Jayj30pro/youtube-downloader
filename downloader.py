from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0,)
root.title("Onusbs YouTube downloader")
Label(root,text = "YouTube downloader", font = 'arial 20 bold').pack()

link =  StringVar()

Label(root, text= "Paste Link Here:", font = 'arial 15 bold').place(x= 160 , y=60)
link_enter = Entry(root, width = 70)
link_enter.place(x =32, y = 90)

def clearRow():
    link_enter.delete(0, END)


def Downloader():
    url = YouTube(str(link_enter.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 20, y= 210)
    link_enter.delete(0, END)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' , bg = '#0AC', padx = 2, command = Downloader).place(x=220, y = 150)
Button(root,text = 'Clear', font = 'arial 15 bold' , bg = '#0AC', padx = 2, command = clearRow).place(x=80, y = 150)
Button(root,text = 'Quit', font = 'arial 15 bold' , bg='#0AC', command = root.destroy).place(x = 280, y = 200) 
root.mainloop()
