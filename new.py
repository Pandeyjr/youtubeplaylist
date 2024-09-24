import yt_dlp

# URL of the playlist
playlist_url = 'https://www.youtube.com/watch?v=UHIQGTfWFto&list=PLGx_Bfz90WK1w6wT4jsLI_8i0v0bQnGph'

ydl_opts = {
    'format': 'best',
    'outtmpl': r'C:\Users\Kiran Pandey\Desktop\youtubeplaylist\%(title)s.%(ext)s',  # Save path
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
