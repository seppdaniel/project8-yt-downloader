# YouTube Video Downloader

Este projeto é um script em Python para baixar vídeos do YouTube utilizando a biblioteca `pytube`. O script itera através de uma lista de links de vídeos e os baixa na resolução mais alta disponível. Além disso, ele exibe uma barra de progresso para cada vídeo enquanto o download está em andamento.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas: `pytube`, `tqdm`

Você pode instalar as bibliotecas necessárias usando o seguinte comando:

pip install pytube tqdm

## Como usar

1. Clone ou baixe este repositório.

2. Crie um arquivo chamado `video_links.py` na mesma pasta do script e defina a variável `video_links` com a lista de links de vídeos do YouTube que você deseja baixar. Por exemplo:

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