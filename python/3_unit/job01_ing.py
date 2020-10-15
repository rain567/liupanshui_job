# 已知list_a = [1,2,3,4,5,6]，请通过两种方法实现，使list_a = [6,5,4,3,2,1]
list_a = [1,2,3,4,5,6]
print('原数组', list_a)
list_a.sort(reverse=True)
print('第一种修改', list_a)

list_a = [1,2,3,4,5,6]
print('第二种修改', sorted(list_a, reverse=True))

list_a = [1,2,3,4,5,6]
list_a.reverse()
print('第三种修改', list_a)
