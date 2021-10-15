import pytube
url=r'https://www.youtube.com/watch?v=QkdV2VV4PfY&t=1965s'
video=pytube.YouTube(url).streams.get_highest_resolution()
video.download()