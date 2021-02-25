# < -- code by rompihitam404 -->
# pip3 install pytube

from pytube import YouTube
import time
import sys

logo = ("""
##################################################
##################################################
###                    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ###
###  ██  ██           ▄█      ████  ████████▄  ###
###  ██▄▄██           ████  ██████  █████████  ###
###  ▀████▀ ████ █  █ ████  █ ██ █ ▄▄ █  ▄▄██  ###
###    ██   █  █ █▄▄█ ████  █    █ ▀▀ █  ▄▄██  ###
###    ██   ▀▀▀▀ ▀▀▀▀ ▀███▄▄█▄▄▄▄█▄▄▄▄█▄▄▄▄█▀  ###
###                     ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀    ###
###                              Downloader!   ###
###          <-- code by: rompihitam.org -->   ###
##################################################
##################################################
""")
print(logo)
# <-- Menerima Masukan dari user -->
link = input("Enter url youtube here --> ")
yt   = YouTube(link)

# <-- Title of video
print("Title: ", yt.title)
# <-- Number of views of video -->
print("Number of views: ", yt.views)
# <-- Length of the video -->
print("Length of video: ", yt.length, "seconds")
# <-- Description of video -->
print("Description: ", yt.description)
# <-- Rating -->
print("Ratings: ", yt.rating)
# <-- Mendapatkan resolusi Terbaik -->
ys = yt.streams.get_highest_resolution()

# <-- Memulai Download -->
animation = ("|/-\\")
for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\rSedang memulai proses download --> " + animation[i % len(animation)])
    sys.stdout.flush()

ys.download()
# <-- Download selesai -->
print("\n\nDownload selesai!!")
