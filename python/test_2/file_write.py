# 编写Python程序：
# 请将下面的内容按行写入文件“D:/file.txt”中。
# 春至华夏
# 作者：玮
# 暗水踏春来，
# 舟行巴蜀川。
# 江陵千里翠，
# 四海一家圆。
txt = [
    '春至华夏',
    '作者：玮',
    '暗水踏春来，',
    '舟行巴蜀川。',
    '江陵千里翠，',
    '四海一家圆。',
]
with open('D:/file.txt', 'w+') as file:
    [file.write('{}\n\n'.format(str)) for str in txt]
with open('D:/file.txt', 'r+') as file:
    print(file.read())