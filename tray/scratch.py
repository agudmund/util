from pytube import YouTube

url = r'https://www.youtube.com/watch?v=iG8fDmq7e6g&index=14&list=PLjke0dIPNiMYkRybVoqtFwWPnH9WuzEMc'
video  = YouTube( url )

video.streams.filter(subtype='mp4').all()[0].download()