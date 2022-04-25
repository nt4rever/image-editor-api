import os
import glob
import random
import shutil
import string

letters = string.ascii_lowercase


def remove_files(folder):
    files = glob.glob(folder)
    for f in files:
        os.remove(f)


def remove_file(path):
    if os.path.exists(path):
        os.remove(path)


def str_id():
    return ''.join(random.choice(letters) for i in range(10))


def uploads(file):
    with open(f'uploads/{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return "./uploads/"+file.filename
