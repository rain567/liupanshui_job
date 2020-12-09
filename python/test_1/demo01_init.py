import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 1]
# plt.bar(input_values, squares, linewidth=5)
#
# # 设置图标标题，并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel('Square of Value', fontsize=14)
#
# # 设置刻度标记大小
# plt.tick_params(axis='both', labelsize=14)
#
# # plt.show()

x = ['1', '2', '3', '4']
y = [4, 3, 5, 2]
plt.bar(x, y, linewidth=1)

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=10)
plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=10)

plt.show()