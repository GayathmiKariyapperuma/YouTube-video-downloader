from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Video Downloader")


Label(root,text = 'Youtube Video Downloader', font ='Ubuntu 20 bold').pack()




##enter link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'Ubuntu 15 ').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)



#function to download video


def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'Roboto 15').place(x= 180 , y = 210)  


Button(root,text = 'DOWNLOAD', font = 'Ubuntu 15 bold' ,bg = 'light blue', padx = 2, command = Downloader).place(x=180 ,y = 150)



root.mainloop()
