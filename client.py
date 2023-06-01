import logging
import os
import re

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
        logging.error("Not found tokens.py with token")
        exit(-1)
    TOKEN = tokens.TOKEN
    client = yandex_music.Client(tokens.TOKEN).init()

def get_user_liked_track() -> list:
    return client.users_likes_tracks().fetch_tracks()

def download_track(id: int, title: str, authors: str) -> str:
    title_regex = re.sub("[/:]", "", title)
    client.tracks(id)[0].download(f"tracks/{title_regex} - {authors}.mp3", bitrate_in_kbps=320)