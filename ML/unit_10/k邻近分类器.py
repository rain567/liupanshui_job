import heapq

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class KNN:
    # 读取数据
    def load_data(self):
        dataset = pd.read_csv('watermelon4a.csv')
        Attributes = dataset.columns
        m, n = np.shape(dataset)
        dataset = np.matrix(dataset)
        self.future = Attributes[1:n - 1]
        self.x = dataset[:, 1:m - 1]
        self.y = dataset[:, n - 1]
        self.m = m

    def get_distance(self):
        self.distance = np.zeros((self.m, self.m))
        for i in range(self.m):
            self.distance[i, i] = np.inf
            for j in range(i + i, self.m):
                d = self.edist(self.x[i, :], self.x[j, :])
                self.distance[i, j] = d
                self.distance[j, i] = d

    def edist(self, x1, x2):
        x1 = np.array(x1)
        x2 = np.array(x2)
        print(x1)
        return np.linalg.norm(x1 - x2)

    def train(self, k):
        label = np.ones((self.m,))
        for i in range(self.m):
            index = self.get_index(self.distance[i, :], k)
            label[i] = self.get_lable(index)
        return label

    def get_index(self, dist, k):
        dist = dist.tolist()
        index = map(dist.index, heapq.nsmallest(k, dist))
        return list(index)

    def get_lable(self, index):
        labellist = self.y[index]
        if np.sum(labellist) > 0:
            return 1
        else:
            return -1

    def my_plot(self, label):
        y = np.array(self.y).tolist()
        y = np.reshape(y, (17,)).tolist()
        print(y)

        Tgoodin = [i for i, x in enumerate(y) if x == 1]
        print(Tgoodin)
        Tbadin = [i for i, x in enumerate(y) if x == -1]
        print(Tbadin)
        Tgood = self.x[Tgoodin, :]
        Tbad = self.x[Tbadin, :]
        print(Tgood)

        label = label.tolist()
        Pgoodin = [i for i, x in enumerate(label) if x == 1]
        Pbadin = [i for i, x in enumerate(label) if x == -1]
        Pgood = self.x[Pgoodin, :]
        Pbad = self.x[Pbadin, :]

        plt.figure()
        l1, = plt.plot(Tgood[:, 0], Tgood[:, 1], 'r+')
        l2, = plt.plot(Tbad[:, 0], Tbad[:, 1], 'r_')
        l3, = plt.plot(Pgood[:, 0], Pgood[:, 1], 'bx')
        l4, = plt.plot(Pbad[:, 0], Pbad[:, 1], 'gx')
        plt.legend(
            handles=[
                l1, l2, l3, l4], labels=[
                'good', 'bad', 'good', 'bad'])
        plt.xlabel('density')
        plt.ylabel('Sugar')
        plt.show()


def main():
    knn = KNN()
    knn.load_data()
    knn.get_distance()
    label = knn.train(1)
    knn.my_plot(label)


if __name__ == '__main__':
    main()
