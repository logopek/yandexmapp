import os

import yandex_music

import tokens
TOKEN = tokens.TOKEN
client = yandex_music.Client(tokens.TOKEN).init()

def get_user_liked_track() -> list:
    return client.users_likes_tracks().fetch_tracks()

def download_track(id: int, title: str, authors: str) -> str:
    client.tracks(id)[0].download(f"tracks/{title} - {authors}.mp3")