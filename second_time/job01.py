# iList = [1, 2, 3]
# for i in iList:
#     print('hello world!')
#
# # while 1 < 2:
# #     print('hello world!')
#
# array = [2, 3, 5, 1]
# array.sort()
# print(array)
#
# list_a = [5,2,10,6,8,13,7]
#
# list_a.reverse()
#
# print(list_a[2])

# 编写Python程序：
#
# （说明：点开题目上方的“Python在线程序环境”或者在自己电脑上打开IDLE，编写程序代码，调试通过后将代码与运行结果的截图，提交到题目下方的答题框里。）

# 1、姓名：将一些朋友的姓名存储在一个列表中，并将其命名为names。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
print('\n1、姓名：将一些朋友的姓名存储在一个列表中，并将其命名为names。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。')
names = ['tom', 'jerry', 'spike']
for name in names:
    print(name)

# 2、问候语：继续使用题1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
print('\n2、问候语：继续使用题1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。')
message = '你好,'
for name in names:
    print(message + name)

# 3、自己的列表：想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，如“我想拥有一辆本田摩托车”。
print('\n3、自己的列表：想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，如“我想拥有一辆本田摩托车”。')
cars = ['林肯汽车', '本田摩托车']
str = '我想拥有一辆'
print(str + cars[0])
print(str + cars[1])


