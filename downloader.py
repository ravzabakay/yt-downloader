import yt_dlp
import os
from datetime import datetime
import re

def is_valid_url(url):
    """
    Bu fonksiyon, girilen URL'nin geçerli bir YouTube URL'si olup olmadığını kontrol eder.
    Eğer geçerli değilse False döndürür.
    """
    pattern = re.compile(r"https?://(www\.)?youtube\.com/.+")
    return re.match(pattern, url) is not None

def download_video(url):
    """
    Bu fonksiyon, verilen YouTube URL'sini indirir ve videoyu belirtilen formatta kaydeder.
    """
    # URL geçerliliğini kontrol et
    if not is_valid_url(url):
        print("Geçersiz YouTube URL'si!")
        return

    # İndirme seçeneklerini belirle
    options = {
        'format': 'bestvideo+bestaudio/best',  # Video ve sesin en iyi kalitesini indir
        'outtmpl': f'ilham_kaynagim_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.%(ext)s',  # Dosya adı: ilham_kaynagim_2023-07-15_18-30-25.mp4
        'merge_output_format': 'mp4'  # Video ve sesi birleştirip mp4 formatında kaydet
    }

    try:
        # YoutubeDL ile video indir
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url)  # Video bilgilerini al
            filename = ydl.prepare_filename(info)  # Gerçek dosya adını belirle
            print(f"🎉 Video indirildi: {os.path.abspath(filename)}")  # İndirilen dosyanın tam yolunu yazdır
    except Exception as e:
        # Hata durumunda kullanıcıya bilgi ver
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    # Kullanıcıdan video URL'sini al
    video_url = input("Video URL'sini girin: ")  # Kullanıcıdan URL alıyoruz
    download_video(video_url)  # Videoyu indir




