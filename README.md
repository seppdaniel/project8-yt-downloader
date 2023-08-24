# YouTube Video Downloader

Este projeto é um script em Python para baixar vídeos do YouTube utilizando a biblioteca `pytube`. O script itera através de uma lista de links de vídeos e os baixa na resolução mais alta disponível. Além disso, ele exibe uma barra de progresso para cada vídeo enquanto o download está em andamento.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas: `pytube`, `tqdm`

Você pode instalar as bibliotecas necessárias usando o seguinte comando:

pip install pytube tqdm

## Como usar

1. Clone ou baixe este repositório.

2. Instale as dependências: pytube e tqdm

3. Modifique o link referente ao vídeo desejado para download neste trecho:
```python
    with tqdm(total=ys.filesize, unit='B', unit_scale=True, ncols=100, bar_format='{l_bar}{bar}|') as t:
        ys.download(download_path)
        t.write(f'Download concluído: {yt.title}')

# Link direto para o vídeo que será baixado
video_link = "https://www.youtube.com/watch?v=3VnGCVMMHQ4"
download_video(video_link)
```

```python
video_links = [
    'Fs3uBjTA70c',
    'ExemploDeLink2',
    'ExemploDeLink3',
    # ... adicione mais links conforme necessário
]
```
3. Execute o script youtube_downloader.py:
```
python youtube_downloader.py
```
Os vídeos serão baixados e salvos na pasta C:\Users\Public\Videos com o título do vídeo como nome do arquivo.

###Nota
Este script é apenas para fins educacionais. Por favor, respeite os direitos autorais e as políticas de conteúdo do YouTube ao utilizar este projeto.
