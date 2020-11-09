from aip import AipBodyAnalysis

""" 你的 APPID AK SK """
APP_ID = '22952720'
API_KEY = 'inMk4SrpYUxPmSUGmqGw89Ow'
SECRET_KEY = '7ecoXWQBLwwEjwp83Od0jV5EZM166oG7'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('ok_img.jpg')


""" 调用手势识别 """
resp = client.gesture(image)
if resp['result'] and resp['result'][0]['classname']:
    print('识别成功，收拾：{}'.format(resp['result'][0]['classname']))
else:
    print('识别失败')