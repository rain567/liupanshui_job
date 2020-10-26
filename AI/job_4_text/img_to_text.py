from aip import AipOcr
from docx import Document
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


for i in range(1, 5):
    image = get_file_content(str(i) + '.png')
    resp = client.basicGeneral(image);
    words = list(map(lambda record: record['words'], resp['words_result']))
    # print('words', words)
    print(','.join(words))
    with open("test.txt", "w", encoding='utf-8') as f:
        f.write(','.join(words) + '\n')



