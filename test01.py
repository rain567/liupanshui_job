import numpy
import random
from matplotlib import pyplot as plt
from keras.datasets import mnist # 从keras的datasets中导入mnist数据集
from keras.models import Sequential # 导入Sequential模型
from keras.layers import Dense # 全连接层用Dense类
from keras.layers import Dropout # 为输入数据施加Dropout。Dropout将在训练过程中每次更新参数时按一定概率（rate）随机断开输入神经元，Dropout层用于防止过拟合
from keras.utils import np_utils # 导入np_utils是为了用one hot encoding方法将输出标签的向量（vector）转化为只在出

# 获取数据集MNIST
# 将随机数产生器初始化为一个常量能让最终的结果是固定的。
seed = 7 # 设置随机种子
numpy.random.seed(seed)
(X_train, y_train), (X_test, y_test) = mnist.load_data() # 加载数据
"""
matplotlib
subplot(numRows, numCols, plotNum)
图表的整个绘图区域被分成 numRows 行和 numCols 列
然后按照从左到右，从上到下的顺序对每个子区域进行编号，左上的子区域的编号为1
plotNum 参数指定创建的 Axes 对象所在的区域
如果 numRows ＝ 2, numCols ＝ 3, 那整个绘制图表样式为 2X3 的图片区域, 用坐标表示为
(1, 1), (1, 2), (1, 3)
(2, 1), (2, 2), (2, 3)
这时, 当 plotNum ＝ 3 时, 表示的坐标为(1, 3), 即第一行第三列的子图
如果 numRows, numCols 和 plotNum 这三个数都小于 10 的话, 可以把它们缩写为一个整数, 例如 subplot(323) 和 subplot(3,2,3) 是相同的.
"""
# plt.imshow()
plt.imshow
# 获取可视化数据
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.imshow(X_train[i], cmap='gray', interpolation='none')
    plt.title("Class {}".format(y_train[i]))
# MNIST数据标准化
# 数据集是3维的向量（instance length,width,height)
# 为了完成后期的归一化处理，所以必须将X_trian、X_test数据转换成浮点型数据
num_pixels = X_train.shape[1] * X_train.shape[2] #784
X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32')
X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32')
# 给定的像素的灰度值在0-255，为了使模型的训练效果更好，通常将数值归一化映射到0-1
# 图像数据本身是 0-255 的 uint8 型数据，所以需要归一化，转换到 0-1之间。
X_train = X_train / 255
X_test = X_test / 255
# print(X_train[57])
# one hot encoding
# one-hot编码，又称“独热编码”。其实就是用N位状态寄存器编码N个状态，每个状态都有独立的寄存器位，且这些寄存器位中只有一位有效，说白了就是只能有一个状态。
# print(y_train[6780])
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_test.shape[1]

# 多层感知机的搭建
def baseline_model():
    model = Sequential() # 建立一个Sequential模型,然后一层一层加入神经元
    # 第一步是确定输入层的数目正确：在创建模型时用input_dim参数确定。例如，有784个个输入变量，就设成num_pixels。
    # 全连接层用Dense类定义：第一个参数是本层神经元个数，然后是初始化方式和激活函数。这里的初始化方法是0到0.05的连续型均匀分布（uniform），Keras的默认方法也是这个。也可以用高斯分布进行初始化（normal）。
    # 具体定义参考：https://cnbeining.github.io/deep-learning-with-python-cn/3-multi-layer-perceptrons/ch7-develop-your-first-neural-network-with-keras.html
    model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal', activation='relu'))
    model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

model = baseline_model()
# 函数每个参数的意义参考：https://blog.csdn.net/a1111h/article/details/82148497
# model.fit()
model_log = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200, verbose=2)
# 1、模型概括打印
model.summary()
# model.evaluate 返回计算误差和准确率
scores = model.evaluate(X_test, y_test, verbose=0)
print(scores)
print("Base Error:%.2f%%" % (100-scores[1]*100))