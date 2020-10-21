# 语言合成
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '22844737'
API_KEY = 'Gc4Vtsvw3dpjxjuEpCrFlq8d'
SECRET_KEY = 'mBbpvR3tA7wm561dtmchP5MMjPsVnGt4'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis('你好百度', 'zh', 1, {
    'vol': 5,
})
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)