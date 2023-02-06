from pytube import YouTube

link = input("Youtube video link:")

quality = input("Quality video: (High/Low)")

video = YouTube(link)
result = None

if quality == "High":
    result = video.streams.get_highest_resolution()
elif quality == "Low":
    result = video.streams.get_lowest_resolution()

result.download()