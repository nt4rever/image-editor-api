import random
import string
import numpy as np
import urllib.request
import cv2

letters = string.ascii_lowercase


def str_id():
    return ''.join(random.choice(letters) for i in range(10))


def url_to_image(url):
    url_response = urllib.request.urlopen(url)
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)
    return img


def export_image(img, path):
    cv2.imwrite(path, img)
