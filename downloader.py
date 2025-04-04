import yt_dlp
import os

def download_video(url):
    options = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'ilham_kaynagim.%(ext)s',
        'merge_output_format': 'mp4'
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url)
        filename = ydl.prepare_filename(info)
        print("🎉 Video indirildi:", os.path.abspath(filename))

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=DAOQFqVYY24"
    download_video(video_url)



