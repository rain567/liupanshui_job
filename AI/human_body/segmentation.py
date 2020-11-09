from aip import AipBodyAnalysis
import base64
import cv2
import numpy as np
import skimage.io
import matplotlib.pyplot as plt

""" 你的 APPID AK SK """
APP_ID = '22952720'
API_KEY = 'inMk4SrpYUxPmSUGmqGw89Ow'
SECRET_KEY = '7ecoXWQBLwwEjwp83Od0jV5EZM166oG7'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('post_img.jpg')

""" 调用人像分割 """
client.bodySeg(image);

""" 如果有可选参数 """
options = {}
options["type"] = "labelmap"


def base64_to_rgb(base64_str):
    if isinstance(base64_str, bytes):
        base64_str = base64_str.decode("utf-8")

    img_data = base64.b64decode(base64_str)
    return skimage.io.imread(img_data, plugin='imageio')


""" 带参数调用人像分割 """
resp = client.bodySeg(image, options)
base = resp['labelmap']

img = base64_to_rgb(base)
plt.imshow(img)
plt.show()