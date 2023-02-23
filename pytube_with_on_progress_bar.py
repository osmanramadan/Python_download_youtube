
from pytube import YouTube
from pytube.cli import on_progress 

link=input('enter url:')  
yt=YouTube(link,on_progress_callback=on_progress)
videos=yt.streams.first()
videos.download()