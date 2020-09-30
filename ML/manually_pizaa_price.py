# -*- coding: utf-8 -*-
#多元线性回归：手动实现通过分析披萨的直径、辅料数量与价格的线性关系，来预测披萨的价格
#导入必要模块
import numpy as np
import pandas as pd
#加载数据
pizza = pd.read_csv("pizza_multi.csv", index_col='Id')
#将前五行数据作为测试集，其他为测试集
X = pizza.iloc[:-5, :2].values
y = pizza.iloc[:-5, 2].values.reshape((-1, 1))
print(X)
print(y)
#计算系数，公式：p55-公式3.11
ones = np.ones(X.shape[0]).reshape(-1,1)
X = np.hstack((X,ones))
w_ = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)
b = w_[-1]
w = w_[:-1]
print(w)
print(b)
#预测
X_test = pizza.iloc[-5:, :2].values
y_test = pizza.iloc[-5:, 2].values.reshape((-1, 1))
print(X_test)
print(y_test)
y_pred = np.dot(X_test, w) + b
# y_pred = np.dot(np.hstack((X_test, ones)), w_)
print("目标值：\n", y_test)
print("预测值：\n", y_pred)