# 一百万：创建一个列表，其中包含数字1~1000000，再使用一个for循环将这些数字打印出来
# （如果输出的时间太长，按Ctrl + C 停止输出，或关闭输出窗口）。

nums = range(1, 1000001)
for num in nums:
    print(num, end=',')