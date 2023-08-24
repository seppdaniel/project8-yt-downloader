from pytube import YouTube
from tqdm import tqdm
import re

def progress_bar(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    completed = int(current * 100 / stream.filesize)
    tqdm.write(f'Completed {completed}%')

def download_video(video_link):
    yt = YouTube(video_link, on_progress_callback=progress_bar)
    ys = yt.streams.get_highest_resolution()
    valid_title = re.sub(r'[<>:"/\\|?*]', '_', yt.title)
    download_path = f'C:/Users/Public/{valid_title}.mp4'
     
    with tqdm(total=ys.filesize, unit='B', unit_scale=True, ncols=100, bar_format='{l_bar}{bar}|') as t:
        ys.download(download_path)
        t.write(f'Download concluído: {yt.title}')

# Link direto para o vídeo que será baixado
# Sempre que atualizar o link, salvar o algoritmo
video_link = "https://www.youtube.com/watch?v=KmrNYmv6GHU&t=2058s"
download_video(video_link)
