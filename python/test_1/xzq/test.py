import pandas as pd
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

import matplotlib.pyplot as plt

y = range(1, 17)

plt.bar(np.arange(16), y, alpha=0.5, width=0.3, color='yellow', edgecolor='red', label='The First Bar', lw=3)
plt.bar(np.arange(16) + 0.4, y, alpha=0.2, width=0.3, color='green', edgecolor='blue', label='The Second Bar', lw=3)
plt.legend(loc='upper left')
plt.show()