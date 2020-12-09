import pygal

from test_1.pygal.die import Die

# 创建一个D6实例
die = Die()

# 投几次骰子，并将结果存储在一个列表中
results = []
for roll_null in range(100000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化处理结果
hist = pygal.Bar()
hist.title = '骰子1000次各面次数'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = '面'
hist.y_title = '次数'

hist.add('D6', frequencies)
hist.render_to_file('骰子.svg')