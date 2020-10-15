# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 22:24:28 2020

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

melon = pd.read_csv('watermelon3a.csv')  # 读取西瓜数据集
# melon['Good'] = melon['Good'].map({'是':1,'否':0})          #将类别标签置换成0，1分类
label = np.array(melon['Good'])
labels = label.reshape(17, 1)  # 对标签reshape方便后续运算
data = np.array(melon[['density', 'Sugar']])  # data保存特征数据


def sigmoid(z):
    return 1.0 / (1 + np.exp(-z))  # 定义sigmoid函数


b = np.ones((len(melon), 1))
data = np.c_[b, data]  # 添加常数项

w = np.ones((3, 1))  # 初始化参数
n = 0.01  # 学习率
for i in range(500000):  # 迭代500000次
    y = sigmoid(data.dot(w))
    m = y - labels  # 计算误差值
    w = w - data.transpose().dot(m) * n  # 误差反传更新参数，梯度下降算法
print(np.abs(m).sum())  # 打印误差值

plt.scatter(data[:, 1], data[:, 2], c=label, cmap=plt.cm.Spectral)
x = np.linspace(0, 1, 100)
y = -(w[1] * x + w[0]) / w[2]
plt.plot(x, y)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel('density')
plt.ylabel('Sugar')
plt.show()  # 可视化，查看分类结果

