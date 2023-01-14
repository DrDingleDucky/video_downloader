from pytube import YouTube

while True:
    command = input("Video Link > ")

    try:
        video = YouTube(command)

        print(f"Downloading: {video.title}")

        downloaded_video = video.streams.get_highest_resolution()

        downloaded_video.download("videos")

        print("Successful")
    except:
        pass


    if command.lower() == "quit":
        break


print("Done")
