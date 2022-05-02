import cv2
from utils import url_to_image

def gaussian_blur(path, x):
    image = url_to_image(path)
    dst = cv2.GaussianBlur(image, (x, x), cv2.BORDER_DEFAULT)
    return dst


def laplacian(filepathname, ksize=3):
    v = url_to_image(filepathname)
    s = cv2.cvtColor(v, cv2.COLOR_BGR2GRAY)
    s = cv2.Laplacian(s, cv2.CV_16S, ksize)
    s = cv2.convertScaleAbs(s)
    return s
