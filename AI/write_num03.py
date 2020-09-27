import tensorflow as tf
tf.__version__

mint=tf.keras.datasets.mnist
(x_,y_),(x_1,y_1)=mint.load_data()

import matplotlib.pyplot as plt
plt.imshow(x_[0], cmap="binary")
plt.show()