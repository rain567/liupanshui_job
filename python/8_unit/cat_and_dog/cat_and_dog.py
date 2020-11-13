import random
"""
猫鼠大战
"""


class Animal:
    def __init__(self, nickname, variety, atk, health_point) -> None:
        self.nickname = nickname
        self.variety = variety
        self.atk = atk
        self.health_point = health_point

    # 更新生命中
    def update_health_point(self, price):
        self.health_point += price

    # 减少生命值
    def be_injured(self, harm):
        self.update_health_point(-harm)

    # 攻击
    def attack(self, animal):
        animal.be_injured(self.atk)
        return True

    # 回复生命值
    def eat_food(self, food):
        self.update_health_point(food)


class Dog(Animal):
    def __init__(self, nickname, variety, atk, health_point) -> None:
        super().__init__(nickname, variety, atk, health_point)


class Cat(Animal):
    def __init__(self, nickname, variety, atk, health_point) -> None:
        super().__init__(nickname, variety, atk, health_point)

    # 重写猫的减少什么在方法
    def be_injured(self, harm):
        # 猫有概率躲避技能
        if self.run_away():
            print('{}躲避成功，攻击失败'.format(self.nickname))
            return False
        return super(Cat, self).be_injured(harm)

    @classmethod
    def run_away(cls):
        """
        猫的技能逃跑，如果和4求余为0则躲避
        :return:
        """
        return random.randint(0, 9) % 4 == 0


if __name__ == '__main__':
    dog = Dog('ww', '哈皮', 7, 30)
    cat = Cat('tom', '美短', 5, 20)

    # 记录回合数
    bout = 1
    # 进攻方
    att_animal = None
    # 防守方
    guard_animal = None
    while True:
        print('\n第{}回合：'.format(bout))
        # 随机判断这个回合轮到哪方进攻
        event = random.randint(0, 9) % 2 == 0
        # 如果是能是偶数则猫进攻，反之则狗进攻
        if event:
            att_animal = cat
            guard_animal = dog
        else:
            att_animal = dog
            guard_animal = cat

        print('{} 攻击 {}，'.format(att_animal.nickname, guard_animal.nickname), end='')
        # 判断攻击是否成功
        if att_animal.attack(guard_animal):
            print('造成{}点伤害，'.format(guard_animal.atk), end='')
        # 判断是否死亡
        if guard_animal.health_point <= 0:
            print('{}死亡，{}获胜'.format(guard_animal.nickname, att_animal.nickname))
            break
        print('{}还剩{}点血'.format(guard_animal.nickname, guard_animal.health_point))
        # 判断随机数和三求余为0，回复生命值
        food_num = random.randint(0, 9)
        if random.randint(1, 10) % 3 == 0:
            guard_animal.eat_food(food_num)
            print('{}幸运捡到食物，回复{}点血量，还剩{}点血量'.format(guard_animal.nickname, food_num, guard_animal.health_point))

        bout += 1
