# -*- coding: utf-8 -*-
# 多元线性回归：使用sklear包通过分析披萨的直径、辅料数量与价格的线性关系，来预测披萨的价格
#导入必要模块
#import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
# 读取数据
pizza = pd.read_csv("/ML/unit_3/pizza_multi.csv", index_col='Id')
X = pizza.iloc[:-5, :2].values
y = pizza.iloc[:-5, 2].values.reshape((-1, 1))
X_test = pizza.iloc[-5:, :2].values
y_test = pizza.iloc[-5:, 2].values.reshape((-1, 1))
# 线性拟合
model = LinearRegression()
model.fit(X, y)
# 预测
predictions = model.predict(X_test)
for i, prediction in enumerate(predictions):
    print('Predicted: %s, Target: %s' % (prediction, y_test[i]))
 # 模型评估
"""
使用 score 方法可以计算 R方
R方的范围为 [0, 1]
R方越接近 1，说明拟合程度越好
"""
print('R-squared: %.2f' % model.score(X_test, y_test))