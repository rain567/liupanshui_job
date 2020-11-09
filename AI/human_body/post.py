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

image = get_file_content('post_img.jpg')

""" 调用人体检测与属性识别 """

resp = client.bodyAttr(image)
# print(resp)
if resp['person_info'] and resp['person_info'][0]:
    attributes = resp['person_info'][0]['attributes']
    print('识别成功: \n衣服：{}\n裤子：{} \n年纪：{} \n动作：{}'.format(attributes['upper_wear']['name'],
                                                  attributes['lower_wear']['name'],
                                                  attributes['age']['name'],
                                                  attributes['cellphone']['name']
                                                  ))
else:
    print('识别失败')