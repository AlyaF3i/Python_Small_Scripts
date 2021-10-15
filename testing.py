import pytube

url=r'https://youtu.be/WjoplqS1u18'

pytube.YouTube(url).streams.get_highest_resolution().download()
#get_by_resolution('2160p').download('Hello')
