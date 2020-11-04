import numpy as np
import matplotlib.pyplot as plt
from pylab import *
# define tree node
class TreeNode:
    def __init__(self, feature, thresh):
        self.feature = feature  # 特征：密度 or 含糖率
        self.thresh = thresh  # 基于某个特征分类时的划分值
        self.label = -1  # 类别：只在叶子节点上不为-1，为0或1代表好瓜的否和是。
        self.data = []  # 用来保存该节点上的数据
        self.left = None  # 左右结点
        self.right = None
    def numOfGood(self):
        return self.data[self.data == 1].sum()
    def numOfBad(self):
        return self.data[self.data == 0].sum()
def getDataSet():
    """
    get watermelon data set 3.0 alpha.
    :return: (feature array, label array)
    """
    dataSet = np.array([
        [0.697, 0.460, 1],
        [0.774, 0.376, 1],
        [0.634, 0.264, 1],
        [0.608, 0.318, 1],
        [0.556, 0.215, 1],
        [0.403, 0.237, 1],
        [0.481, 0.149, 1],
        [0.437, 0.211, 1],
        [0.666, 0.091, 0],
        [0.243, 0.267, 0],
        [0.245, 0.057, 0],
        [0.343, 0.099, 0],
        [0.639, 0.161, 0],
        [0.657, 0.198, 0],
        [0.360, 0.370, 0],
        [0.593, 0.042, 0],
        [0.719, 0.103, 0]
    ])
    return dataSet
def calEntropy(dataArr, labelArr):
    """
    calculate information entropy.
    :param dataArr:
    :return: entropy
    """
    n = dataArr.size
    data0 = dataArr[labelArr == 0]
    data1 = dataArr[labelArr == 1]
    p0 = data0.size / float(n)
    p1 = data1.size / float(n)
    # 约定：p=0, p*log_2(p) = 0
    if p0 == 0:
        entropy = -(p1 * np.log(p1))
    elif p1 == 0:
        entropy = -(p0 * np.log(p0))
    else:
        entropy = -(p0 * np.log(p0) + p1 * np.log(p1))
    return entropy
# # test calEntropy()
# dataSet = getDataSet()
# print(calEntropy(dataSet[:, :-1], dataSet[:, -1],))
def calInfoGain(dataSet, feature, thresh):
    """
    calculate information gain
    :param dataSet: 数据集，最后一列为类别。
    :param feature: 选择用来计算信息增益的特征。0表示第一个特征，1表示第二个特征
    :param thresh: 用来划分数据的值
    :return: 信息增益
    """
    entD = calEntropy(dataSet[:, :-1], dataSet[:, -1])  # 计算D的原始信息熵
    # 数据集划分为两份
    dataL = dataSet[dataSet[:, feature] <= thresh]
    dataR = dataSet[dataSet[:, feature] > thresh]
    # 计算两数据集的信息熵
    entL = calEntropy(dataL[:, :-1], dataL[:, -1])
    entR = calEntropy(dataR[:, :-1], dataR[:, -1])
    # 计算划分完总数据集的信息熵
    entDS = (dataL.size * entL + dataR.size * entR) / float(dataSet.size)
    # 计算信息增益
    gain = entD - entDS
    return gain
# # test calInfoGain(dataSet, feature, thresh)
# data = getDataSet()
# print(calInfoGain(data, 0, 0.6))
def chooseBestSplit(dataSet):
    """
    计算信息增益增大的划分数据集的方式
    :param dataSet:
    :return: 信息增益最大的划分方式的 特征 和 划分值。
    """
    maxGain = 0.0
    bestFeature = -1
    bestThresh = -1
    m, n = dataSet.shape
    # 对每一个特征
    for i in range(n - 1):
        feat = dataSet[:, i]  # 得到第i个特征的所有值
        sortedFeat = np.sort(feat)  # 按照从小到大的顺序排列第i个特征的所有值
        T = []
        # 计算划分点
        for j in range(m - 1):
            t = (sortedFeat[j] + sortedFeat[j + 1]) / 2.0
            T.append(t)
        # 对每一个划分值,计算增益熵
        for val in T:
            gain = calInfoGain(dataSet, i, val)
            if gain > maxGain:
                bestFeature = i
                bestThresh = val
                maxGain = gain
    return bestFeature, bestThresh, maxGain
# # test chooseBestSplit
# data = getDataSet()
# f, tv, g = chooseBestSplit(data)
# print(f"best feature is {f}\n"
#       f"best thresh value is {tv}\n"
#       f"max information gain is {g}")
def createTree(dataSet):
    """
    通过信息增益创造一颗决策树
    :param dataSet:
    :return: 返回一颗树的根结点
    """
    # 到叶子节点时返回。
    # 若只剩k个相同类的数据，信息熵 = -(0*log_2(0) + k*log_2(k) = 0
    # 即信息熵为0时返回叶子结点
    if calEntropy(dataSet[:, :-1], dataSet[:, -1]) == 0:
        leaf = TreeNode(-1, -1)  # 构造叶子结点
        leaf.label = dataSet[0][-1]
        return leaf
    feature, thresh, gain = chooseBestSplit(dataSet)
    dataL = dataSet[dataSet[:, feature] <= thresh]
    dataR = dataSet[dataSet[:, feature] > thresh]
    Node = TreeNode(feature, thresh)
    Node.data = dataSet
    Node.left = createTree(dataL)
    Node.right = createTree(dataR)
    return Node
# # test createTree()
# data = getDataSet()
# Tree = createTree(data)
# ***********************画图***********************
# **********************start***********************
def getNumLeafs(myTree):
    """
    得到叶子结点的数量
    :param myTree:
    :return:
    """
    if myTree.feature == -1:
        return 1
    if myTree is None:
        return 0
    return getNumLeafs(myTree.left) + getNumLeafs(myTree.right)
# # test getNumLeafs()
# data = getDataSet()
# Tree = createTree(data)
# print(getNumLeafs(Tree))  # 5个叶子
def getTreeDepth(myTree):
    """
    得到树的深度
    :param myTree:
    :return:
    """
    if myTree is None:
        return 0
    # 1表示加上当前节点
    depth = max(1 + getTreeDepth(myTree.left),
                1 + getTreeDepth(myTree.right))
    return depth
# # test getTreeDepth()
# data = getDataSet()
# Tree = createTree(data)
# print(getTreeDepth(Tree))  # 深度为5
# 没有这句的话画出的图上面汉字会显示成口口
mpl.rcParams['font.sans-serif'] = ['SimHei']
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")
fList = ["密度", "含糖率"]  # 后面画节点时用到
melon = ["坏瓜", "好瓜"]
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    """
    绘制一个结点以及指向这个减点的箭头
    :param nodeTxt: 结点上的文字
    :param centerPt: 箭头终止坐标
    :param parentPt: 箭头起始坐标，即对应树中父结点坐标。即从parentPt指向centerPt
    :param nodeType: 结点类型。实际上是一个字典，里面保存着绘制结点的参数，
                     decisionNode：表示非叶子结点。leafNode表示叶子结点、
    :return:
    """
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,
                            xycoords='axes fraction',
                            xytext=centerPt,
                            textcoords='axes fraction',
                            va="center", ha="center",
                            bbox=nodeType,
                            arrowprops=arrow_args,
                            fontsize=15)  # 结点字的大小
# def createPlot():
#     fig = plt.figure(1, facecolor='white')
#     fig.clf()
#     createPlot.ax1 = plt.subplot(111, frameon=False)
#     plotNode('决策节点', (0.5, 0.1), (0.1, 0.5), decisionNode)
#     plotNode('叶节点', (0.8, 0.1), (0.3, 0.8), leafNode)
#     plt.show()
# createPlot()
def plotMidText(cntrPt, parentPt, txtString):
    """
    计算父节点和子节点中间的位置，即箭头中间的位置上画上文本，比如"是"和"否"
    :param cntrPt: 子节点的坐标
    :param parentPt:父节点的坐标
    :param txtString: 要画的字符
    :return:
    """
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString,
                        va="center", ha="center", rotation=30,
                        fontsize=15)
def plotTree(myTree, parentPt, nodeTxt):  # if the first key tells you what feat was split on
    """
    递归画树
    :param myTree: 树节点
    :param parentPt: 父节点坐标
    :param nodeTxt: 节点字符
    :return:
    """
    numLeafs = getNumLeafs(myTree)  # this determines the x width of this tree
    depth = getTreeDepth(myTree)
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)
    if myTree.thresh != -1:
        plotMidText(cntrPt, parentPt, nodeTxt)
        plotNode(str(fList[myTree.feature])  # fList = ["密度", "含糖率"]
                 + "<=" + str(myTree.thresh) + "?",
                 cntrPt, parentPt, decisionNode)
        plotTree.yOff = plotTree.yOff - 1 / plotTree.totalD
    else:
        plotTree.xOff = plotTree.xOff + 1 / plotTree.totalW
        plotMidText(cntrPt, parentPt, nodeTxt)
        plotNode(melon[int(myTree.label)], cntrPt, parentPt, decisionNode)  # melon = ["坏瓜", "好瓜"]
        plotTree.yOff = plotTree.yOff - 1 / plotTree.totalD
    if myTree.left is not None:
        plotTree(myTree.left, cntrPt, "是")
    if myTree.right is not None:
        plotTree(myTree.right, cntrPt, "否")
    plotTree.yOff = plotTree.yOff + 1 / plotTree.totalD
def createPlot(inTree):
    """
    设置画图的基本信息，如树的宽度和深度，初始坐标等。调用plotTree()画图
    :param inTree:
    :return:
    """
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)  # no ticks
    # createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()
# ***********************画图***********************
# ***********************end************************
def main():
    data = getDataSet()
    Tree = createTree(data)
    createPlot(Tree)
if __name__ == '__main__':
    main()