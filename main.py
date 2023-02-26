import pytube

video_link = input("video link -> ")

try:
    video = pytube.YouTube(video_link)

    print(f"downloading: {video.title}")

    downloaded_video = video.streams.get_highest_resolution()

    downloaded_video.download("videos")

    print("successful")

except:
    print("error")

print("done")
