import pytube
import os

pytube.YouTube("https://www.youtube.com/watch?app=desktop&v=COCjvUYGHNs").streams.get_lowest_resolution().download("downloadd")

