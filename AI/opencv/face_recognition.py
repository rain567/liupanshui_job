# 人脸识别

# coding=UTF-8
# 利用baidu-aip库进行人脸识别
import cv2
import base64
import matplotlib.pyplot as plt
from aip import AipFace

"""读取图片"""


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def detection(APP_ID, API_KEY, SECRET_KEY, filename, maxnum):
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)
    image = base64.b64encode(get_file_content(filename))
    image = str(image, 'utf-8')
    imageType = "BASE64"
    # 设置
    options = {}
    options['max_face_num'] = 10
    options["face_field"] = "age,beauty,expression,faceshape"
    result = client.detect(image, imageType, options)
    return result


def result_show(filename, result):
    img = cv2.imread(filename)
    face_num = result['result']['face_num']
    for i in range(face_num):
        data = result['result']['face_list'][i]
        age = "age:" + str(data['age'])
        beauty = "beauty:" + str(data['beauty'])
        location = data['location']
        left_top = (int(location['left']), int(location['top']))
        right_bottom = (left_top[0] + location['width'], left_top[1] + location['height'])
        cv2.rectangle(img, left_top, right_bottom, (226, 26, 25), 2)
        cv2.putText(img, beauty, (int(location['left']), (int(location['top'])) - 25), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (0, 200, 200), 1)
        cv2.putText(img, age, (int(location['left']), int(location['top'])), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 250, 50),
                    2)
    cv2.imshow("putText", img)
    cv2.waitKey(0)


if __name__ == '__main__':
    APP_ID = '22911430'
    API_KEY = 'kGehW01UFIUUHQf7ATMdPoFs'
    SECRET_KEY = 'aYBMR1TGxsymnoUe6PcYgnFIjc3tIZw2'
    filename = 'img.jpg'
    result = detection(APP_ID, API_KEY, SECRET_KEY, filename, 10)
    print(result)
    result_show(filename, result)

