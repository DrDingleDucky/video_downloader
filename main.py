from pytube import YouTube

while True:
    command = input("'help' > ")

    if command.lower() == "download" or command.lower() == "dl":
        video_link = input("Video Link > ")

    try:
        video = YouTube(command)

        print(f"Downloading: {video.title}")

            downloaded_video = video.streams.get_highest_resolution()

        downloaded_video.download("videos")

            print("Successful")
        except:
            print("Unknown Link")

    if command.lower() == "help":
        print('''"download" to download a video.
"help" pulls up the help menu.
"quit" to exit the program.''')

    if command.lower() == "quit":
        break


print("Done")
