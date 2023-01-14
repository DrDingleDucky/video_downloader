from pytube import YouTube

while True:
    command = input("> ")

    if command.lower() == "download" or command.lower() == "dl":
        video_link = input("Video Link > ")
        video_resolution = input(
            "Video Resolution 'max', '720p', '480p', '360p', '144p' > ")

        print(video_resolution)

        try:
            video = YouTube(video_link)

            print(f"Downloading: {video.title}")

            if video_resolution.lower() == "max":
                downloaded_video = video.streams.get_highest_resolution().download("videos")
            else:
                downloaded_video = video.streams.filter(
                    res=video_resolution).first()

            print(downloaded_video)
            print(type(downloaded_video))

            downloaded_video.download("videos")

            print("Successful")
        except:
            print("Error")

    if command.lower() == "help":
        print('''"download" to download a video.
"help" pulls up the help menu.
"quit" to exit the program.''')

    if command.lower() == "quit":
        break


print("Done")
