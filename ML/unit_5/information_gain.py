# -*- coding: utf-8 -*-
from pylab import *
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
# 特征字典，后面用到了好多次，干脆当全局变量了
featureDic = {
    '色泽': ['浅白', '青绿', '乌黑'],
    '根蒂': ['硬挺', '蜷缩', '稍蜷'],
    '敲声': ['沉闷', '浊响', '清脆'],
    '纹理': ['清晰', '模糊', '稍糊'],
    '脐部': ['凹陷', '平坦', '稍凹'],
    '触感': ['硬滑', '软粘']}


def getDataSet():
    """
    get watermelon data set 3.0 alpha.
    :return: 编码好的数据集以及特征的字典。
    """
    dataSet = [
        ['青绿', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', 0.697, 0.460, 1],
        ['乌黑', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', 0.774, 0.376, 1],
        ['乌黑', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', 0.634, 0.264, 1],
        ['青绿', '蜷缩', '沉闷', '清晰', '凹陷', '硬滑', 0.608, 0.318, 1],
        ['浅白', '蜷缩', '浊响', '清晰', '凹陷', '硬滑', 0.556, 0.215, 1],
        ['青绿', '稍蜷', '浊响', '清晰', '稍凹', '软粘', 0.403, 0.237, 1],
        ['乌黑', '稍蜷', '浊响', '稍糊', '稍凹', '软粘', 0.481, 0.149, 1],
        ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '硬滑', 0.437, 0.211, 1],
        ['乌黑', '稍蜷', '沉闷', '稍糊', '稍凹', '硬滑', 0.666, 0.091, 0],
        ['青绿', '硬挺', '清脆', '清晰', '平坦', '软粘', 0.243, 0.267, 0],
        ['浅白', '硬挺', '清脆', '模糊', '平坦', '硬滑', 0.245, 0.057, 0],
        ['浅白', '蜷缩', '浊响', '模糊', '平坦', '软粘', 0.343, 0.099, 0],
        ['青绿', '稍蜷', '浊响', '稍糊', '凹陷', '硬滑', 0.639, 0.161, 0],
        ['浅白', '稍蜷', '沉闷', '稍糊', '凹陷', '硬滑', 0.657, 0.198, 0],
        ['乌黑', '稍蜷', '浊响', '清晰', '稍凹', '软粘', 0.360, 0.370, 0],
        ['浅白', '蜷缩', '浊响', '模糊', '平坦', '硬滑', 0.593, 0.042, 0],
        ['青绿', '蜷缩', '沉闷', '稍糊', '稍凹', '硬滑', 0.719, 0.103, 0]
    ]

    features = ['色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '密度', '含糖量']

    # 每种特征的属性个数
    numList = []  # [3, 3, 3, 3, 3, 2]
    for i in range(len(features) - 2):
        numList.append(len(featureDic[features[i]]))
    
    # 编码，把文字替换成数字。用1、2、3表示同种特征的不同类型
    newDataSet = []
    for dataVec in dataSet:  # 第一每一个数据
        dataNum = dataVec[-3:]  # 保存数据中的数值部分
        newData = []
        for i in range(len(dataVec) - 3):  # 值为字符的每一列
            for j in range(numList[i]):  # 对应列的特征的每一类
                if dataVec[i] == featureDic[features[i]][j]:
                    newData.append(j+1)
        newData.extend(dataNum)  # 编码好的部分和原来的数值部分合并
        newDataSet.append(newData)
    return np.array(newDataSet), features


def calEntropy(dataArr, classArr):
    """
    calculate information entropy.
    :param dataArr:
    :param classArr:
    :return: entropy
    """

    n = dataArr.size
    data0 = dataArr[classArr == 0]
    data1 = dataArr[classArr == 1]
    p0 = data0.size / float(n)
    p1 = data1.size / float(n)
    # 约定：p=0, p*log_2(p) = 0
    if p0 == 0:
        ent = -(p1 * np.log(p1))
    elif p1 == 0:
        ent = -(p0 * np.log(p0))
    else:
        ent = -(p0 * np.log2(p0) + p1 * np.log2(p1))

    return ent


def splitDataSet(dataSet, ax, value):
    """
    按照给点的属性ax和其中一种取值value来划分数据。
    当属性类型为标称数据时，返回一个属性值都为value的数据集。
    当属性类型为数值型数据事，以与value的大小关系为基准返回两个数据集。
    input:
        dataSet: 输入数据集，形状为(m,n)表示m个数据，前n-1列个属性，最后一列为类型。
        ax：属性类型
        value: 标称型时为1、2、3等。数值型为形如0.123的数。

    return：
        1.标称型dataSet返回第ax个属性中值为value组成的集合
        2.数值型dataSet返回两个集合。其一中数据都小于等于value，另一都大于。
    """
    # 2个连续属性密度、含糖量+类型为后3列，其余为标称型
    if ax < dataSet.shape[1] - 3:
        dataS = np.delete(dataSet[dataSet[:, ax] == value], ax, axis=1)
        return dataS
    else:
        dataL = dataSet[dataSet[:, ax] <= value]
        dataR = dataSet[dataSet[:, ax] > value]
        return dataL, dataR


def calInfoGain(dataSet, labelList, ax, value=-1):
    """
    计算给定数据dataSet在属性ax上的香农熵增益。
    input：
        dataSet：输入数据集，形状为(m,n)表示m个数据，前n-1列个属性，最后一列为类型。
        labelList：属性列表，如['色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '密度', '含糖量']
        ax: 选择用来计算信息增益的属性。0表示第一个属性，1表示第二个属性等。
                    前六个特征是标称型，后两个特征是数值型。
        value: 用来划分数据的值。当标称型时默认为-1, 即不使用这个参数。

    return：
        gain:信息增益
    """
    baseEnt = calEntropy(dataSet[:, :-1], dataSet[:, -1])  # 计算D的原始信息熵

    newEnt = 0.0  # 划分完数据后的香农熵
    if ax < dataSet.shape[1] - 3:  # 计算标称型的香农熵
        num = len(featureDic[labelList[ax]])   # 每一个特征的类别数
        for j in range(num):
            subDataSet = splitDataSet(dataSet, ax, j+1)
            prob = len(subDataSet) / float(len(dataSet))
            if prob != 0:
                newEnt += prob * calEntropy(subDataSet[:, :-1], subDataSet[:, -1])
    else:
        # 数据集划分为两份
        dataL, dataR = splitDataSet(dataSet, ax, value)
        # 计算两数据集的信息熵
        entL = calEntropy(dataL[:, :-1], dataL[:, -1])
        entR = calEntropy(dataR[:, :-1], dataR[:, -1])
        # 计算划分完总数据集的信息熵
        newEnt = (dataL.size * entL + dataR.size * entR) / float(dataSet.size)

    # 计算信息增益
    gain = baseEnt - newEnt
    return gain


def chooseBestSplit(dataSet, labelList):
    """
    计算信息增益增大的划分数据集的方式. 当返回的不是数值型特征时， 划分值bestThresh = -1
    input:
        dataSet
        labelList
    return:
        bestFeature: 使得到最大增益划分的属性。
        bestThresh： 使得到最大增益划分的数值。标称型时无意义令其为-1。
        maxGain：    最大增益划分时的增益值。
    """
    maxGain = 0.0
    bestFeature = -1
    bestThresh = -1
    m, n = dataSet.shape
    # 对每一个特征
    for i in range(n - 1):
        if i < (n - 3):     # 标称型
            gain = calInfoGain(dataSet, labelList, i)
            if gain > maxGain:
                bestFeature = i
                maxGain = gain
        else:   # 数值型
            featVals = dataSet[:, i]  # 得到第i个特征的所有值
            sortedFeat = np.sort(featVals)  # 按照从小到大的顺序排列第i个特征的所有值
            T = []
            # 计算划分点
            for j in range(m - 1):
                t = (sortedFeat[j] + sortedFeat[j + 1]) / 2.0
                T.append(t)
            # 对每一个划分值,计算增益熵
            for t in T:
                gain = calInfoGain(dataSet, featureDic, i, t)
                if gain > maxGain:
                    bestFeature = i
                    bestThresh = t
                    maxGain = gain

    return bestFeature, bestThresh, maxGain


def majorityCnt(classList):
    """
    投票，0多返回"坏瓜",否则返回"坏瓜"。
    """
    cnt0 = len(classList[classList == 0])
    cnt1 = len(classList[classList == 1])
    if cnt0 > cnt1:
        return '坏瓜'
    else:
        return '好瓜'


def createTree(dataSet, labels):
    """
    通过信息增益递归创造一颗决策树。
    input:
        labels
        dataSet
    return:
        myTree: 返回一个存有树的字典
    """
    classList = dataSet[:, -1]
    # 如果剩余的类别全相同,则返回
    if len(classList[classList == classList[0]]) == len(classList):
        if classList[0] == 0:
            return '坏瓜'
        else:
            return '好瓜'
    # 如果只剩下类标签，投票返回
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    # 得到增益最大划分的属性、值
    bestFeat, bestVal, entGain = chooseBestSplit(dataSet, labels)
    bestFeatLabel = labels[bestFeat]

    if bestVal != -1:  # 如果是数值型
        txt = bestFeatLabel + "<=" + str(bestVal) + "?"
    else:   # 如果是标称型
        txt = bestFeatLabel + "=" + "?"

    myTree = {txt: {}}  # 创建字典，即树的节点。
    if bestVal != -1:   # 数值型的话就是左右两个子树。
        subDataL, subDataR = splitDataSet(dataSet, bestFeat, bestVal)
        myTree[txt]['是'] = createTree(subDataL, labels)
        myTree[txt]['否'] = createTree(subDataR, labels)
    else:
        i = 0
        # 生成子树的时候要将已遍历的属性删去。数值型不要删除。
        del (labels[bestFeat])
        uniqueVals = featureDic[bestFeatLabel]  # 最好的特征的类别列表
        for value in uniqueVals:    # 标称型的属性值有几种，就要几个子树。
            # Python中列表作为参数类型时，是按照引用传递的，要保证同一节点的子节点能有相同的参数。
            subLabels = labels[:]  # subLabels = 注意要用[:]，不然还是引用
            i += 1
            subDataSet = splitDataSet(dataSet, bestFeat, i)
            myTree[txt][value] = createTree(subDataSet, subLabels)
    
    return myTree


# 画图
# 详情参见机器学习实战决策树那一章

# 定义文本框和箭头格式
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 没有这句话汉字都是口口
# mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, fontsize=20)


def plotNode(nodeTxt, centerPt, parentPt, nodeType):  # 绘制带箭头的注解
    createPlot.ax1.annotate(nodeTxt,
                            xy=parentPt,
                            xycoords="axes fraction",
                            xytext=centerPt,
                            textcoords="axes fraction",
                            va="center",
                            ha="center",
                            bbox=nodeType,
                            arrowprops=arrow_args,
                            fontsize=20)


def getNumLeafs(myTree):  # 获取叶节点的数目
    numLeafs = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


def getTreeDepth(myTree):  # 获取树的层数
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth


def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)
    getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW,
              plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff),
                     cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


def createPlot(inTree):
    fig = plt.figure(1, figsize=(600, 30), facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()


def main():
    dataSet, labelList = getDataSet()
    myTree = createTree(dataSet, labelList)
    createPlot(myTree)


if __name__ == '__main__':
    main()
