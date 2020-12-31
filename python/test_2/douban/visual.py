import pandas as pd
import matplotlib.pyplot as plt

# 项目
project = '电影'
# 显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 这两行需要手动设置
plt.rcParams['axes.unicode_minus'] = False
# 文件全路径+文件名
csv_file_name = '{}.csv'.format(project)
# 获取文件中的内容
data = pd.read_csv(csv_file_name, encoding='utf-8')


# 添加数据标签
def add_labels(rects):
    index = 0
    for rect in rects:
        # 打印电影名称
        plt.text(4.5,
                 8.8 - index * 1,
                 sort_list['title'].array[9 - index],
                 ha='center',
                 va='bottom',
                 color='#ffffff')
        # 打印评分
        height = sort_list['rate'].array[9 - index]
        plt.text(height + 0.25,
                 8.8 - index * 1,
                 '%.2f' % height,
                 ha='center',
                 va='bottom',
                 color='#00BFBF')
        rect.set_edgecolor('white')
        index += 1


# 清洗出排行前十
def data_cleansing():
    sort_data = data.sort_values('rate', ascending=True)
    return sort_data.tail(10)


# 前十榜单柱状图可视化
def sort_10_bar():
    # 生成颜色
    color = [[0.8, 0.7, index * 0.1] for index, color in enumerate(sort_list['rate'])]
    # 画图
    bar = plt.barh(sort_list['title'], width=sort_list['rate'], linewidth=2, color=color)
    # 添加片名和评分
    add_labels(bar)
    # 设置图标标题，并给坐标轴加上标签
    plt.title("豆瓣年度{}前十榜单".format(project), fontsize=24)
    plt.xlabel("评分", fontsize=14)

    frame = plt.gca()
    # y 轴不可见
    frame.axes.get_yaxis().set_visible(False)

    # 保存图表，最后结果
    plt.savefig('豆瓣年度{}前十榜单柱状图.png'.format(project), bbox_inches='tight')
    # 显示图片，调试时使用
    plt.show()


if __name__ == '__main__':
    # 清洗数据
    sort_list = data_cleansing()
    # 柱状图
    sort_10_bar()
