from cProfile import label
from logging import root
import re
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube
from tkinter import filedialog


#########################################    backside   ####################################################

path=""
x=False

def openlocation():
    global x
    global path
    path=filedialog.askdirectory()
    if (len(path)>1):
        locationError.config(text=path,fg="green")
        x=True
        
    else:
        locationError.config(text="select your option again",fg="red")
        
def is_valid_url(url):
    
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if regex.search(url):
        return False
    else:
        return True
    

def download_youtube():
    choice=ytdchoices.get()
    url=ytdEntryvar.get()
    # valid fields
    if x==False:
        messagebox.showinfo("error","اختار مسار")
        return 
    if choice=='':
        messagebox.showinfo("error","اختار الجودة")
        return 
    if url=='' or is_valid_url(url):
        messagebox.showinfo("error","انسخ رابط صالح")
        return 
    yt=YouTube(url)
    if (choice==choices[0]):
        select=yt.streams.filter(progressive=True).first()
    elif (choice==choices[1]):
        select=yt.streams.filter(progressive=True,file_extension='mp4').first()
    else:
        select=yt.streams.filter(only_audio=True).first()
        
    if x==True and choice==choices[0] or choice==choices[1] or choice==choices[2]:
        select.download(path)
        ytdError.config(text="downloading finished",fg="green")
    return
    
    
        
#########################################    Frontside   ####################################################

root=Tk()
root.title("downloader")
root.resizable(False,False)
root.geometry("650x410+340+70")
root.columnconfigure(0,weight=1)
##############
f1=Frame(root,width="580",height="100",bg="whitesmoke",bd=3,relief=GROOVE)
f1.place(x=30,y=130)
###############
f2=Frame(root,width="580",height="55",bg="whitesmoke",bd=3,relief=GROOVE)
f2.place(x=30,y=250)
###############
label=Label(root,text="downloader from youtube",bg="red",fg="white",font=('Tajawal',15,font.BOLD))
label.pack(fill=X)
###############           ########### the partion of inserting url  #########################     ######################
ytlabel=Label(root,text="insert the url here",bg="blue",fg="white",font=('Tajawal',15,font.BOLD))
ytlabel.pack(fill=X)
ytdEntryvar=StringVar()
ytdEntry=Entry(root,width=70,state="normal",justify="center",font=('Tajawal',15,font.BOLD),fg="blue",textvariable=ytdEntryvar)
ytdEntry.pack()


ytdError=Label(root,text="notes of downloading",font=('Tajawal',15,font.BOLD),fg="blue")
ytdError.pack()

ytdsave=Label(root,text="select the location of downloading",font=('Tajawal',15,font.BOLD),fg="blue")
ytdsave.place(x=180,y=140)

#entry of save
saventry=Button(root,width=10,font=('Tajawal',11,font.BOLD),fg="white",bg="red",text="اختار المسار",command=openlocation)
saventry.place(x=490,y=180)

#error location
locationError=Label(root,text="لم يتم اختيار مسار النحميل",font=('Tajawal',12,font.BOLD),fg="red")
locationError.place(x=33,y=190)

#the quality of video
ytdQuality=Label(root,text="اختار الجودة",bg="whitesmoke",font=('Tajawal',15,font.BOLD))
ytdQuality.place(x=430,y=255)

#chobobox
choices=['740p','144p','sound only']
ytdchoices=ttk.Combobox(root,values=choices)
ytdchoices.place(x=260,y=265)


downloadbtn=Button(root,text="بدء التحميل",width=20,textvariable="osman",font=('Tajawal',12,font.BOLD),fg="white",bg="red",command=download_youtube)
downloadbtn.place(x=40,y=255)

downloadbtn=Button(root,text="الخروج من البرنامج",width=30,font=('Tajawal',17,font.BOLD),fg="white",bg="red",command=quit)
downloadbtn.place(x=110,y=360)

root.mainloop()