import youtube_dl
link = [input("Nhap Link: ")]
print(link)
format = input("nhap oke để tải nhạc từ youtube: ")
if format == 'oke':
    ydl = youtube_dl.YoutubeDL({'format':'bestaudio'})
    ydl.download(link)
    print("Xong")