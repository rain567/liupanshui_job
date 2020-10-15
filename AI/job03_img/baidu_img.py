from aip import AipImageClassify

APP_ID = '22790464'
API_KEY = '6CeW2kefahGVAl75VHiP2Ig5'
SECRET_KEY = 'xzvLAz6M4M7ZD3AY9flnEZMuHqLFoIe5 '

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('C:/Users/Rain/Pictures/01.jpg')

""" 调用通用物体识别 """
client.advancedGeneral(image);

""" 如果有可选参数 """
options = {}
options["baike_num"] = 5

""" 带参数调用通用物体识别 """
resp = client.advancedGeneral(image, options)
print(resp)