# -*- coding: utf-8 -*-
import numpy as np


class ProductionSystem:
    def __init__(self):
        f=open("productions.txt","r")
        self.productions=[]
        self.charicters=[]
        self.myclass=(f.readline().strip("最终类别为：").strip()).split("，")
        for line in f.readlines():
            if line != '\n':
                line = line.replace("->", " ")
                line = line.replace(",", " ")
                line = line.split()
                self.productions.append(line)
                for ch in line:
                    if (ch not in self.myclass) and (ch not in self.charicters):
                        self.charicters.append(ch)

    def show_production(self):
        print()

    def match(self, x):
        for ch in self.productions[x][:-1]:
            if ch in self.work:
                continue
            else:
                return False
        return True

    def classify(self, work):
        used = np.zeros(len(self.productions))
        counter = len(self.work)
        while True:
            for i in range(len(self.productions)):
                if used[i]==0 and self.match(i):
                    used[i]=1
                    self.work.append(self.productions[i][-1])
                    if self.work[-1] in self.myclass:
                        return True
            tmp = len(self.work)
            if tmp == counter:
                return False
            else:
                counter = tmp

    def do_work(self):
        print("所有类别有:")
        for t in self.myclass:
            print('{:<10}'.format(t), end="")
        print()
        print("所有属性有：")
        counter=0
        for t in self.charicters:
            counter += 1
            if counter%5==0:
                print('{:<10}'.format(t))
            else:
                print('{:<10}'.format(t), end='')
        self.work = input("\n请输入属性\n----属性之间用空格隔开----\n")
        self.work = self.work.split()
        if self.classify(self.work):
            print("该物种为："+self.work[-1])
        else:
            print("抱歉，未能识别出该物种\n")


def main():
    p=ProductionSystem()
    p.do_work()


if __name__ == "__main__":
    main()