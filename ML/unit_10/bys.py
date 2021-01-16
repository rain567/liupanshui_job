import math
import pandas as pd

D_keys = {
    '色泽': ['青绿', '乌黑', '浅白'],
    '根蒂': ['蜷缩', '硬挺', '稍蜷'],
    '敲声': ['清脆', '沉闷', '浊响'],
    '纹理': ['稍糊', '模糊', '清晰'],
    '脐部': ['凹陷', '稍凹', '平坦'],
    '触感': ['软粘', '硬滑'],
}
Class, labels = '好瓜', ['是', '否']


# 读取数据
def loadData(filename):
    dataSet = pd.read_csv(filename)
    dataSet.drop(columns=['编号'], inplace=True)
    return dataSet


# 配置测1数据
def load_data_test():
    array = ['青绿', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', 0.697, 0.460, '']
    dic = {a: b for a, b in zip(dataSet.columns, array)}
    return dic


def calculate_D(dataSet):
    D = []
    for label in labels:
        temp = dataSet.loc[dataSet[Class] == label]
        D.append(temp)
    return D


def calculate_Pc(Dc, D):
    D_size = D.shape[0]
    Dc_size = Dc.shape[0]
    N = len(labels)
    return (Dc_size + 1) / (D_size + N)


def calculate_Pcx_D(key, value, Dc):
    Dc_size = Dc.shape[0]
    Dcx_size = Dc[key].value_counts()[value]
    Ni = len(D_keys[key])
    return (Dcx_size + 1) / (Dc_size + Ni)


def calculate_Pcx_C(key, value, Dc):
    mean, var = Dc[key].mean(), Dc[key].var()
    exponent = math.exp(-(math.pow(value - mean, 2) / (2 * var)))
    return (1 / (math.sqrt(2 * math.pi * var)) * exponent)


def calculate_probability(label, Dc, dataSet, data_test):
    prob = calculate_Pc(Dc, dataSet)
    for key in Dc.columns[:-1]:
        value = data_test[key]
        if key in D_keys:
            prob *= calculate_Pcx_D(key, value, Dc)
        else:
            prob *= calculate_Pcx_C(key, value, Dc)
    return prob


def predict(dataSet, data_test):
    # mu, sigma = dataSet.mean(), dataSet.var()
    Dcs = calculate_D(dataSet)
    max_prob = -1
    for label, Dc in zip(labels, Dcs):
        prob = calculate_probability(label, Dc, dataSet, data_test)

        if prob > max_prob:
            best_label = label
            max_prob = prob
        print(label, prob)
    return best_label


if __name__ == '__main__':
    # 读取数据
    filename = r'data30.csv'
    dataSet = loadData(filename)
    data_test = load_data_test()
    label = predict(dataSet, data_test)
    print('预测结果：', label)