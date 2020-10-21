from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '22844737'
API_KEY = 'Gc4Vtsvw3dpjxjuEpCrFlq8d'
SECRET_KEY = 'mBbpvR3tA7wm561dtmchP5MMjPsVnGt4'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
resp = client.asr(get_file_content('test.wav'), 'pcm', 16000, {
    'dev_pid': 1537,
})

print(resp.get('result')[0])