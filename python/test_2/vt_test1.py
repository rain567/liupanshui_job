# def m():
#     return lambda s:s*3
# 请补全代码：实现调用此函数，打印输出'hellohellohello'。

def m():
    return lambda s: s * 3


# 方案1
print(m()('hello'))

# 方案2
print(m().__call__('hello'))
