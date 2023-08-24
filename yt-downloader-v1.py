from pytube import YouTube
from link_mapping import video_links
from tqdm import tqdm

def progress_bar(stream, chunk, bytes_remaining):
    current = stream.filesize - bytes_remaining
    completed = int(current * 100 / stream.filesize)
    tqdm.write(f'Completed {completed}%')

def download_video(video_link):
    yt = YouTube('https://www.youtube.com/watch?v=' + video_link, on_progress_callback=progress_bar)
    ys = yt.streams.get_highest_resolution()
    download_path = 'C:/Users/Public/' + yt.title + '.mp4'
    #download_path = f'C:/Users/Public/{}.mp4'.format(yt.title)


    with tqdm(total=ys.filesize, unit='B', unit_scale=True, ncols=100, bar_format='{l_bar}{bar}|') as t:
        ys.download(download_path)
        t.write(f'Download concluído: {yt.title}')

for link in video_links:
    download_video(link)
