# -*- coding: UTF-8 -*-
import csv#导入csv库
from sklearn.feature_extraction import DictVectorizer#转换工具，将list转换成为一个数组
from sklearn import preprocessing
from sklearn import tree #创建决策树
import numpy as np
from IPython.display import Image
import pydotplus
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz 2.44.1\\bin'

from sklearn.datasets import load_iris
#csv的读取
file = csv.reader((open("西瓜数据集30.csv","rt")))#注意保存utf8
print(file)#获取文件信息
#file.decode("utf8","ignore")
headers = next(file)#获取并打印头信息
print(headers)
#将行信息转变成为list和Dict
featurelist = []#创建一个特征列表
labellist = []#创建一个标签列表

for row in file:
    #每一次获取最后一列值，添加到标签列表中
    labellist.append(row[len(row)-1])
    #每一次都创建一个字典接受列值
    rowDict ={}
    for i in range(1,len(row)-1):#从第二位置开始添加
       rowDict[headers[i]] = row[i]#添加字典的对应特征值
    featurelist.append(rowDict)#每次添加一行
print(labellist)#获取到的标签值
print(featurelist)#获取到的每一行的特征值，每一个字典相当于一个元素

"""
将获得特征值字典转变成为数组
字典特征提取器：
将字典数据结构抽和向量化
类别类型特征借助原型特征名称采用0 1 二值方式进行向量化
数值类型特征保持不变
"""
vec = DictVectorizer()  # 初始化字典特征抽取器
dummyX = vec.fit_transform(featurelist).toarray() #将特征值的list转变成为一个数组
print("dummyX:" + str(dummyX))
print(vec.get_feature_names())#获取特征所有的取值
#将获取的标签list转变,主要是将多类标签转化为二值标签，最终返回的是一个二值数组或稀疏矩阵
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labellist)
print("dummyY" + str(dummyY))

#创建分类器
clf = tree.DecisionTreeClassifier(criterion= "entropy") #使用Id3
clf = clf.fit(dummyX,dummyY)
print("clf:"+str(clf))
#创建出文件
with open("wm20.dot","w") as f:
  f = tree.export_graphviz(clf,feature_names = vec.get_feature_names(),out_file= f)#使用export_graphviz
  
#dot_data=tree.export_graphviz(clf,out_file=None)

dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=['敲声=沉闷', '敲声=浊响', '敲声=清脆', '根蒂=硬挺', '根蒂=稍蜷', '根蒂=蜷缩', '纹理=模糊', '纹理=清晰', '纹理=稍糊', '脐部=凹陷', '脐部=平坦', '脐部=稍凹', '色泽=乌黑', '色泽=浅白', '色泽=青绿', '触感=硬滑', '触感=软粘'] ,
                         class_names=['好瓜', '坏瓜'],
                         filled=True, rounded=True,  
                         special_characters=True) 

print(dot_data)

graph = pydotplus.graph_from_dot_data(dot_data)  
Image(graph.create_png()) 
graph.write_jpg("wm20.jpg")
#dot -Tjpg wm20.dot -o wm20.jpg