import pygal
from test_1.pygal.die import Die

# 创建一个D6实例
die1 = Die(6)
die2 = Die(4)

# 投几次骰子，并将结果存储在一个列表中
results = []
# 次数
count = 1000000
for roll_null in range(count):
    result = die1.roll() + die2.roll()
    results.append(result)

# 分析结果
frequencies = []
# 骰子出现的最小点数和最高点数
counts = []
for value in range(2, die1.num_sides + die2.num_sides + 1):
    counts.append(value)
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化处理结果
hist = pygal.Bar()
hist.title = '两个骰子{}次各面次数'.format(count)
hist.x_labels = counts
hist.x_title = '面'
hist.y_title = '次数'

hist.add('D6', frequencies)
hist.render_to_file('两个骰子点数不一致-{}次.svg'.format(count))
