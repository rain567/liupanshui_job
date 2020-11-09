# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:11:57 2020

@author: Administrator
"""

import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
 
    

def getDataSet():
    """
    get watermelon data set 3.0 alpha.
    :return: 编码好的数据集以及特征的字典。
    """

    dataSet = np.array([
        [ 0.697, 0.460, 1],
        [ 0.774, 0.376, 1],
        [ 0.634, 0.264, 1],
        [ 0.608, 0.318, 1],
        [ 0.556, 0.215, 1],
        [ 0.403, 0.237, 1],
        [ 0.481, 0.149, 1],
        [ 0.437, 0.211, 1],
        [ 0.666, 0.091, 0],
#        [ 0.243, 0.267, 0],
        [ 0.245, 0.057, 0],
        [ 0.343, 0.099, 0],
        [ 0.639, 0.161, 0],
        [ 0.657, 0.198, 0],
#        [ 0.360, 0.370, 0],
        [ 0.593, 0.042, 0],
        [ 0.719, 0.103, 0]
    ])
    """
    dataSet =np.array([
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 0],
       ])
 """
   
    X = dataSet[:, :-1]
    Y = dataSet[:, -1]
    return X, Y
   
def fit(X,Y,max_iter=10, eta0=1):
    Y = Y.reshape(-1, 1)
    if X.shape[0]!=Y.shape[0] or Y.shape[1]!=1:
        raise ValueError
    w = np.ones((X.shape[1]))
    b = 0
    for i in range(max_iter):
        for j in range(X.shape[0]):
            x=np.array(X[j][:2])
            print(x)
            if np.dot(w,x)+b >0:
                y=1
            else:
                y=0
            d=np.array(Y[j][0])
            delta_b=eta0*(d-y)
            delta_w=eta0*(d-y)*x
            print('epoch {} sample [{} {} {} {} {} {} {} {}]'.format(
                i,j,w[0],w[1],b,y,delta_w[0],delta_w[1],delta_b
            ))
            #反向传播，更新权重
            w=w+delta_w
            b=b+delta_b
    return w,b

if __name__ == '__main__':
  X,Y = getDataSet()  
  positive_x1 = [X[i, 0] for i in range(X.shape[0]) if Y[i] == 1]
  positive_x2 = [X[i, 1] for i in range(X.shape[0]) if Y[i] == 1]
  negetive_x1 = [X[i, 0] for i in range(X.shape[0]) if Y[i] == 0]
  negetive_x2 = [X[i, 1] for i in range(X.shape[0]) if Y[i] == 0]
  coef = fit(X,Y,max_iter=10000,eta0=0.2)
  print(coef)
  plt.scatter(positive_x1, positive_x2, c='red')
  plt.scatter(negetive_x1, negetive_x2, c='blue')
  # 画出超平面（在本例中即是一条直线）
  line_x = np.arange(0, 2)
  #line_y =- line_x * (coef[0][0] / coef[0][1]) - coef[1]
  line_y =- (coef[0][0]*line_x+coef[1]) / coef[0][1] 
  plt.plot(line_x, line_y)
  plt.show();