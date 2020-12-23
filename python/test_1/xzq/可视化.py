import matplotlib.pyplot as plt
import xlrd
from collections import Counter
data = []

class ExcelUtil():
    def __init__(self,excel_path):
        # 打开excel文档
        self.data_xsls = xlrd.open_workbook(excel_path)
    def read_excel(self):
        # 获取所有的工作表
        sheets = self.data_xsls.sheets()
        # 存储内容
        datas = []
        for sheet in sheets:
            datas.append(self.read_sheet(sheet))
        return self.dataHandle(datas)

    # 读取表中的所有内容并返回
    def read_sheet(self,sheet):
        tempArr = []
        # 前3行不要，保留后面所有
        for row in range(3,sheet.nrows):
            # 提取第6列数据, 并剔除脏数据
            score = str(sheet.row_values(row)[5]).strip()
            score = score if score != "" else "及格"
            tempArr.append(score)
        return tempArr
    # 对数据进行个数统计
    def dataHandle(self,datas):
        data_dis = {}
        for i in range(len(datas)):
            data_dis.setdefault(self.data_xsls.sheet_by_index(i).name,dict(Counter(datas[i])))
        return data_dis

# 添加数据标签 就是矩形上面的数值
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2,
                 height+0.01*height,
                 '%.2f' % height,
                 ha='center',
                 va='bottom',
                 color='red')
        rect.set_edgecolor('white')


if __name__ == '__main__':
    excelUtil = ExcelUtil("各班级计算机等级过级情况统计数据.xlsx")
    datas = excelUtil.read_excel()
    plt.rcParams["font.sans-serif"] = ["KaiTi"]
    plt.rcParams["axes.unicode_minus"] = False
    # 只保留了3个工作表，其余两个是空表剔除了
    name_list = list(list(datas.values())[0].keys())
    index = 0

    for key, data in datas.items():
        yx = data.get("优秀")
        jg = data.get("及格")
        hg = data.get("合格")
        lh = data.get("良好")
        y_list = [yx, lh, hg, jg]
        x = [item + index for item in list(range(len(name_list)))]
        total_width, n = 0.8, 3
        width = total_width / n
        bar = plt.bar(x, y_list, width=width, label=key, tick_label=name_list)
        add_labels(bar)
        if index < 0.52:
            index += 0.52
        else:
            index = 0.26
    plt.legend()
    plt.show()
