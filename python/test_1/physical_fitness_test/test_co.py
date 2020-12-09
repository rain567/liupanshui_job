import matplotlib.pyplot as plt #导入安装好的可视化模块
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示符号

# 按行读取csv文件的所有数据，存在列表里，每一行为列表的一个值
with open('空气质量因素数据集_按月.csv') as file:
    reads = file.readlines()
    # reads：['Date,PM25,CO,NO2,SO2,O3,风速,降水量,温度\n', '2018-11,97.33,0.84,69.25,17.1,87.13,0.59,117.69,11.62\n',…]

# 创建一个空列表将列表值切割
new_reads = []

# 遍历reads列表，使用strip()函数去掉列表值前后的空字符串（包含空格、制表符、换行符），使用split(',')函数将列表值（这个值是字符串）按’,‘符号切割，并存在一个新的列表里，在把这个列表作为值添加到新列表new_reads
for i in reads:
    new_reads.append(i.strip().split(','))
    # new_reads：[['Date', 'PM25', 'CO', 'NO2', 'SO2', 'O3', '风速', '降水量', '温度'],['2018-11', '97.33', '0.84', '69.25', '17.1', '87.13', '0.59', '117.69', '11.62'],…]

# 将csv文件的第一列（时间列）存在time列表中
time = []
for i in new_reads:
    time.append(i[0])

# 将csv文件的每一列的值以float形式存在列表并返回（除第一列外）
def get_yinsu(label,num):
    # 传递两个实参：label：csv文件列名，num：列名在第几列
    yinsu = []
    for i in new_reads:
        # print(i[num])
        if i[num] != label:
            yinsu.append(float(i[num]))
        else:
            yinsu.append(i[num])
    return yinsu


# 画图表，pm25图默认画好
def get_huatu(y2,label):
    # y2：通过get_yinsu()得到的列表名称，label：影响因素名称
    pm25 = get_yinsu('PM25', 1)
    x_values = time[1:] # 横坐标值列表
    y1_values = pm25[1:] # PM2.5左纵坐标值列表

    fig = plt.figure() # figure()创建一个图形实例,相当于创建个画布
    ax1 = fig.add_subplot(111) # 画布上一个格子，相当于这个画布就装一个图

    ax1.plot(x_values, y1_values, linewidth=4) # 画折线图
    ax1.set_ylabel('PM2.5')  # 设置左边纵坐标标签
    plt.xlabel("时间") # 设置横坐标标签

    ax2 = ax1.twinx() # twinx()函数表示与ax1图像共享x轴
    y2_values = y2[1:] # 右纵坐标值列表
    ax2.set_ylabel('CO')  # 设置右边纵坐标标签
    ax2.plot(y2_values,c='yellow', linewidth=4) # 画折线图
    plt.title(label.upper()+"对PM2.5的影响", fontsize=20) # 设置图标标题
    plt.savefig(label + '对PM2.5的影响.jpg', bbox_inches='tight') # 保存图表并命名，bbox_inches='tight'表示将图表多余的空白区域裁减掉
    plt.show()

if __name__ == '__main__':
    co = get_yinsu('CO', 2)
    get_huatu(co, 'CO')