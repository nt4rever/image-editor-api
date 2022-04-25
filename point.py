import cv2
import numpy as np


def read_image(path):
    return cv2.imread(path)


def convert_to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def export_image(img, path):
    cv2.imwrite(path, img)


def reverse_image(path):
    img = read_image(path)
    igray = convert_to_gray(img)
    return 255 - igray


def threshold(path, a, b):
    img = read_image(path)
    igray = convert_to_gray(img)
    _, thresh = cv2.threshold(igray, a, b, cv2.THRESH_BINARY)
    return thresh

def log_transformation(path,c):
    image = read_image(path)
    c = 255 / np.log(1 + np.max(image))
    log_image = c * (np.log(image + 1))
    log_image = np.array(log_image, dtype = np.uint8)
    return log_image

def hist(path):
    image = read_image(path)
    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    return img_output

