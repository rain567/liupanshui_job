import pygal
from test_1.pygal.die import Die

# 创建一个D6实例
die1 = Die()
die2 = Die()

# 投几次骰子，并将结果存储在一个列表中
results = []
for roll_null in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(2, die1.num_sides + die2.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化处理结果
hist = pygal.Bar()
hist.title = '两个骰子1000次各面次数'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = '面'
hist.y_title = '次数'

hist.add('D6', frequencies)
hist.render_to_file('两个骰子.svg')