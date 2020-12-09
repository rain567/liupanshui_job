import matplotlib as mpl
import matplotlib.pyplot as plt

# 1、单点圆
# plt.scatter(2, 4, s=200)

# 2、列表源
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 2, 3, 4, 5]
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# s：点的直径，c：颜色，edgecolors：边框的颜色，
# plt.scatter(x_values, y_values, c='red', edgecolors='blue',  s=200)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none',  s=200)

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# x坐标轴的取值范围为0~1100，y坐标轴的取值范围为0~1100000
plt.axis([0, 1100, 0, 1100000])

# 自动保存图标的时候不能实验show函数，否正会导致保存的图片为空白
# plt.show()

# 自动保存图表
plt.savefig('squares_plot.png', bbox_inches='tight')
