# coding=utf-8
import sys
import json
import base64
import time
from aip import AipNlp
import os
""" 你的 APPID AK SK """
APP_ID = '22890718'
API_KEY = 'XKDX55B8L0e1GpEGaACWjHRQ'
SECRET_KEY = 'y4d4IMoZiX9cISYMHGu8swjGXfMEUWRB'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'r', encoding='utf-8') as fp:
        return fp.readlines()


def title_content():
    tag = []
    title = []
    content = []
    path = os.getcwd() + '\\' + 'text'
    file_dir = os.listdir(path)
    for im in file_dir:
        file = get_file_content(path + '\\' +im)
        tag.append(im[:-4])
        title.append(file[0])
        content.append(file[1:])
    return tag,title,content

def data_process(title,content):
    result0 = []
    for line in range(len(title)):
        text_tile = title[line]
        for lines in range (len(content)):
            text_content = " ".join(content[lines])
            result = client.topic(text_tile, text_content);
            result = result['item']['lv1_tag_list'][0]['tag']
            result0.append(result)
        return result0


def classify_not(tag, result1):
    for line in range(len(result1)):
        if tag[line] == result1[line]:
            print("分类正确，你真厉害！")
        else:
            print("分类错误，你需要继续加油哦！")


if __name__ == '__main__':
    tag, title, content = title_content()
    predict = data_process(title, content)
    classify_not(tag, predict)


titile = '人工智能'
content = '人工智能，人工智能，人工智能，人工智能，人工智能，人工智能，'
client.topic(titile, content)