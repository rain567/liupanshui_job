# 这里是从keras的datasets中导入mnist数据集
from keras.datasets import mnist
# 这里是将matplotlib.pyplot重名为plt
import matplotlib.pyplot as plt
(X_train, y_train), (X_test, y_test) = mnist.load_data()#
# 所以这里返回的是手写图片的两个tuple，第一个tuple存储的是我们已经人工分类好的图片，
# 也就是每一张图片都有自己对应的标签，然后可以拿来训练，第二个tuple存储的是我们还没分类的图片，
# 在第一个tuple训练完后，我们可以把第二个tuple利用神经网络进行分类，
# 根据实验结果的真实值与我们的预测值进行对比得到相应的损失值，再利用反向传播进行参数更新，再进行分类，然后重复前述步骤直至损失值最小
# plot 4 images as gray scale
plt.subplot(331)
# 这个subplot函数的作用是确定图像的位置以及图像的个数，前两个3的意思是可以放9张图片，如果变成221的话，就是可以放4张图片，然后后面的1，是确定图像的位置，处于第一个，以下的subplot同理
plt.imshow(X_test[0], cmap=plt.get_cmap('gray'))
# 这里个把图片显示出来
# X_train存储的是图像的像素点组成的list数据类型，这里面又由一个二维的list（28 x 28的像素点值）和一个对应的标签list组成，y_train存储的是对应图像的标签，也就是该图像代表什么数字
plt.subplot(332)
plt.imshow(X_train[1], cmap=plt.get_cmap('gray'))
plt.subplot(333)
plt.imshow(X_train[2], cmap=plt.get_cmap('gray'))
plt.subplot(334)
plt.imshow(X_train[3], cmap=plt.get_cmap('gray'))
plt.subplot(335)
plt.imshow(X_train[4], cmap=plt.get_cmap('gray'))
plt.subplot(336)
plt.imshow(X_train[5], cmap=plt.get_cmap('gray'))
plt.subplot(337)
plt.imshow(X_train[6], cmap=plt.get_cmap('gray'))
plt.subplot(338)
plt.imshow(X_train[7], cmap=plt.get_cmap('gray'))
plt.subplot(339)
plt.imshow(X_train[8], cmap=plt.get_cmap('gray'))
# 在这里imshow函数的官方文档：https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow
# 我们这里第一个参数是图片的像素点值组成的数组（列表），第二个参数是指明图片的色彩
# show the plot
# 最后这里官方文档是这样说的：Display a figure. When running in ipython with its pylab mode, display all figures and return to the ipython prompt.，所以我们可以知道show函数是把所有图片都展示出来
plt.show()