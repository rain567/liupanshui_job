# 阿拉斯加2020年1月份的天气数据已保存在weather.csv文件中，
# 请用plot()方法绘制图表描述阿拉斯加一月份的最低气温。
# 要求：横坐标为日期，纵坐标为最低气温，图表效果参照下图。
import pandas as pd
import matplotlib.pyplot as plt

# 显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 这两行需要手动设置
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv('weather.csv', encoding='utf-8')
# 设置天气
dates = [date.replace('2020/1/', '') for date in data['阿拉斯加天气']]
plt.plot(dates, data['最低气温'], linewidth=2)
# 设置图标标题，并给坐标轴加上标签
plt.title("阿拉斯加天气一月份最低温度", fontsize=24)
plt.xlabel("日期", fontsize=14)
plt.ylabel('最低温度', fontsize=14)
# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=10)
# 显示图片，调试时使用
plt.show()