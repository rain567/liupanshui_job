from aip import AipOcr
from aip import AipSpeech
# 图片文字识别
""" 你的 APPID AK SK """
APP_ID_OCR = '22855479'
APP_ID_SPEECH = '22844737'

API_KEY_OCR = 'dEbfdWGaDhu7yG4h07OMaSU3'
API_KEY_SPEECH = 'Gc4Vtsvw3dpjxjuEpCrFlq8d'

SECRET_KEY_OCR = 'V0hD45LqGugfCnZe9eNb6ih5cp5d7Xj4'
SECRET_KEY_SPEECH = 'mBbpvR3tA7wm561dtmchP5MMjPsVnGt4'

client_ocr = AipOcr(APP_ID_OCR, API_KEY_OCR, SECRET_KEY_OCR)
client_speech = AipSpeech(APP_ID_SPEECH, API_KEY_SPEECH, SECRET_KEY_SPEECH)

url = "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2844325179,1671562938&fm=26&gp=0.jpg"

""" 调用通用文字识别, 图片参数为远程url图片 """
client_ocr.basicGeneralUrl(url);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为远程url图片 """
resp = client_ocr.basicGeneralUrl(url, options)
words_result = resp['words_result']
words = list(map(lambda record: record['words'], words_result))

# 文本转音频
result = client_speech.synthesis(','.join(words), 'zh', 1, {
    'vol': 5,
})
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('img_to_text_to_speech.mp3', 'wb') as f:
        f.write(result)