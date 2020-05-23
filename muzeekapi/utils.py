from utils import create_dir
from config import UPLOADS_FOLDER
import os


def organize_upload(album: str, artist: str, band: str) -> str:
    d = UPLOADS_FOLDER
    if band:
        d = os.path.join(UPLOADS_FOLDER, band, album)
    elif not band and artist:
        d = os.path.join(UPLOADS_FOLDER, artist, album)
    create_dir(d)
    return d
