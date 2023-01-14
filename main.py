from pytube import YouTube

while True:
    command = input("'help' > ")

    if command.lower() == "download" or command.lower() == "dl":
        video_link = input("Video Link > ")
<<<<<<< HEAD

    try:
        video = YouTube(command)
=======
>>>>>>> parent of 98a304d (Trash)

        print(f"Downloading: {video.title}")

            downloaded_video = video.streams.get_highest_resolution()

<<<<<<< HEAD
        downloaded_video.download("videos")
=======
            downloaded_video = video.streams.get_highest_resolution()

            downloaded_video.download("videos")
>>>>>>> parent of 98a304d (Trash)

            print("Successful")
        except:
            print("Unknown Link")

    if command.lower() == "help":
        print('''"download" to download a video.
"help" pulls up the help menu.
"quit" to exit the program.''')

    if command.lower() == "quit":
        break


print("Quit")
