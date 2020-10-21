from aip import AipOcr
# 图片文字识别
""" 你的 APPID AK SK """
APP_ID = '22855479'
API_KEY = 'dEbfdWGaDhu7yG4h07OMaSU3'
SECRET_KEY = 'V0hD45LqGugfCnZe9eNb6ih5cp5d7Xj4'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('../../ML/unit_5/wm20.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
resp = client.basicGeneral(image);
print('resp1', resp)
print('---------------------------------------------')

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image, options)

url = "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2844325179,1671562938&fm=26&gp=0.jpg"

""" 调用通用文字识别, 图片参数为远程url图片 """
client.basicGeneralUrl(url);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为远程url图片 """
resp = client.basicGeneralUrl(url, options)
print('resp2', resp)