import pandas as pd
import matplotlib.pyplot as plt

# 显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 这两行需要手动设置
plt.rcParams['axes.unicode_minus'] = False
# 文件全路径+文件名
csv_file_name = '体测整理-清理1.csv'
# 获取文件中的内容
data = pd.read_csv(csv_file_name, encoding='utf-8')

# 年级对应
grades = {
    44: '17级(入学三年)',
    43: '18级(入学两年)',
    42: '19级(入学一年)',
    41: '20级(刚入学)',
}
# 获取年级（set是为了去重
grade_set = list(set(data.loc[:, '年级编号']))
# 通过年级对应转成字符串
grade_list = [grades[grade] for grade in grade_set]


# 添加数据标签 就是矩形上面的数值
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2,
                 height+0.01*height,
                 '%.2f' % height,
                 ha='center',
                 va='bottom',
                 color='#1F77B4')
        rect.set_edgecolor('white')


# 体重及格率折线图分析
def weight_pass_rate_plot():
    scores = []
    for grade in grade_set:
        # 获取该年级的体重指数列表
        grade_students = data.loc[data['年级编号'] == grade, '体重得分']
        # 计算及格率，使用总数除及格人数计算比例
        score = grade_students.loc[data['体重得分'] >= 60].size / grade_students.size
        scores.append(score)

    plt.plot(grade_list, scores, linewidth=2)
    # 设置图标标题，并给坐标轴加上标签
    plt.title("各年级体重及格人数比例", fontsize=24)
    plt.xlabel("年级", fontsize=14)
    plt.ylabel('及格比例', fontsize=14)
    # 设置刻度标记大小
    plt.tick_params(axis='both', labelsize=10)
    # 保存图表，最后结果
    plt.savefig('各年级体重及格人数比例折线图.png', bbox_inches='tight')
    # 显示图片，调试时使用
    plt.show()


# 体重指数平均数柱状图分析
def weight_mean_bar():
    scores = []
    for grade in grade_set:
        # 获取体重指数列，使用mean函数计算平均数
        score = data.loc[data['年级编号'] == grade, '长跑成绩'].mean()
        scores.append(score)

    bar = plt.bar(grade_list, scores, linewidth=2)
    add_labels(bar)
    # 设置图标标题，并给坐标轴加上标签
    plt.title("各年级体重指数平均数", fontsize=24)
    plt.xlabel("年级", fontsize=14)
    plt.ylabel('体重指数平均数', fontsize=14)
    # 保存图表，最后结果
    plt.savefig('各年级体重指数平均数柱状图.png', bbox_inches='tight')
    # 显示图片，调试时使用
    plt.show()


if __name__ == '__main__':
    # 及格率折线图
    weight_pass_rate_plot()
    # 柱状图
    weight_mean_bar()
