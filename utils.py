import os


def create_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)
