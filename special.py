import cv2
from matplotlib import image
from utils import readb64
import numpy as np
from scipy.interpolate import UnivariateSpline


def HDR(path):
    img = readb64(path)
    hdr = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)
    return hdr


def LookupTable(x, y):
    spline = UnivariateSpline(x, y)
    return spline(range(256))


def Summer(path):
    img = readb64(path)
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel, red_channel = cv2.split(img)
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    sum = cv2.merge((blue_channel, green_channel, red_channel))
    return sum


def Winter(path):
    img = readb64(path)
    increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    blue_channel, green_channel, red_channel = cv2.split(img)
    red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    win = cv2.merge((blue_channel, green_channel, red_channel))
    return win


def sharpen(path):
    img = readb64(path)
    kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    img_sharpen = cv2.filter2D(img, -1, kernel)
    return img_sharpen


def sepia(path):
    img = readb64(path)
    # converting to float to prevent loss
    img_sepia = np.array(img, dtype=np.float64)
    img_sepia = cv2.transform(img_sepia, np.matrix([[0.272, 0.534, 0.131],
                                                    [0.349, 0.686, 0.168],
                                                    [0.393, 0.769, 0.189]]))  # multipying image with special sepia matrix
    # normalizing values greater than 255 to 255
    img_sepia[np.where(img_sepia > 255)] = 255
    img_sepia = np.array(img_sepia, dtype=np.uint8)
    return img_sepia


def pencil_sketch_grey(path):
    img = readb64(path)
    # inbuilt function to create sketch effect in colour and greyscale
    sk_gray, sk_color = cv2.pencilSketch(
        img, sigma_s=60, sigma_r=0.07, shade_factor=0.1)
    return sk_color


def gotham(path):
    image = readb64(path)
    midtone_contrast_increase = UnivariateSpline(x=[0, 25, 51, 76, 102, 128, 153, 178, 204, 229, 255],
                                                 y=[0, 13, 25, 51, 76, 128, 178, 204, 229, 242, 255])(range(256))

    # Construct a lookuptable for increasing lowermid pixel values.
    lowermids_increase = UnivariateSpline(x=[0, 16, 32, 48, 64, 80, 96, 111, 128, 143, 159, 175, 191, 207, 223, 239, 255],
                                          y=[0, 18, 35, 64, 81, 99, 107, 112, 121, 143, 159, 175, 191, 207, 223, 239, 255])(range(256))

    # Construct a lookuptable for decreasing uppermid pixel values.
    uppermids_decrease = UnivariateSpline(x=[0, 16, 32, 48, 64, 80, 96, 111, 128, 143, 159, 175, 191, 207, 223, 239, 255],
                                          y=[0, 16, 32, 48, 64, 80, 96, 111, 128, 140, 148, 160, 171, 187, 216, 236, 255])(range(256))

    blue_channel, green_channel, red_channel = cv2.split(image)
    # Boost the mid-tone red channel contrast using the constructed lookuptable.
    red_channel = cv2.LUT(
        red_channel, midtone_contrast_increase).astype(np.uint8)

    # Boost the Blue channel in lower-mids using the constructed lookuptable.
    blue_channel = cv2.LUT(blue_channel, lowermids_increase).astype(np.uint8)

    # Decrease the Blue channel in upper-mids using the constructed lookuptable.
    blue_channel = cv2.LUT(blue_channel, uppermids_decrease).astype(np.uint8)

    # Merge the blue, green, and red channel.
    output_image = cv2.merge((blue_channel, green_channel, red_channel))
    return output_image

def Stylization(path):
    image = readb64(path)
    return cv2.stylization(image, sigma_s=15, sigma_r=0.55)