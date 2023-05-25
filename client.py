import logging
import os

import yandex_music

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
def init():
    global client, TOKEN
    if os.path.isfile('tokens.py'):
        import tokens
    else:
        logging.log(1, "Not found tokens.py with token")
        exit(-1)
    TOKEN = tokens.TOKEN
    client = yandex_music.Client(tokens.TOKEN).init()

def get_user_liked_track() -> list:
    return client.users_likes_tracks().fetch_tracks()

def download_track(id: int, title: str, authors: str) -> str:
    client.tracks(id)[0].download(f"tracks/{title} - {authors}.mp3")