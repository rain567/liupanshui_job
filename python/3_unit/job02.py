# 编写Python程序：
#
#     饺子：想出至少三种你喜欢的饺子。将其名称存储在一个列表中，
#     再使用for循环将每种饺子的名称都打印出来。
#     （1）修改这个for循环，使其打印包含饺子名称的句子，而不仅仅是饺子的名称。
#       对于每种饺子，都显示一行输出，如“我喜欢肉馅饺子”。
#      (2）在程序末尾添加一行代码，它不在for循环中，指出你有多喜欢饺子。
#       输出应包含针对每种饺子的消息，还有一个总结性句子，如“我真的很喜欢饺子”。
#
# （说明：点开题目上方的“Python在线程序环境”或者在自己电脑上打开IDLE，
# 编写程序代码，调试通过后将代码与运行结果的截图，提交到题目下方的答题框里。）

dumplings = ['猪肉饺子', '牛肉饺子', '鸡肉饺子']
message = '我喜欢吃'
# (1)
for dumpling in dumplings:
    print(message + dumpling)
# (2)
print('我真的很喜欢饺子')
