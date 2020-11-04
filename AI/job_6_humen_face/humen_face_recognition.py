from aip import AipFace
import base64

""" 你的 APPID AK SK """
APP_ID = '22915690'
API_KEY = 'ye1oUCKPiYG1GprLD9YxrGku'
SECRET_KEY = '2iPrOq2RuPWaeHyb2wwlkTxloLGxxify'


client = AipFace(APP_ID, API_KEY, SECRET_KEY)
f = open('img.jpg', 'rb')
image = str(base64.b64encode(f.read()),'utf-8')
imageType = "BASE64"

""" 调用人脸检测 """
print('人脸检测结果1：', client.detect(image, imageType));


imageType = "BASE64"
groupIdList = "3,2"

""" 带参数调用人脸搜索 """
print('人脸搜索结果', client.search(image, imageType, groupIdList))