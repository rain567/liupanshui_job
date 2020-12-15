import time

# 计算1~1000000 的总和：创建一个列表，其中包含数字1~1000000，
# 再使用min()和max()核实该列表确实是从1开始，到1000000结束的。
# 然后调用sum() 函数，计算1 ~1000000 的和。
# 观察Python将一百万个数字相加需要多长时间。
# 生成开始时间戳
# start_timestamp = time.time()
nums = range(1, 1000001)
# 生成结束时间戳
# end_timestamp = time.time()
# when = end_timestamp - start_timestamp
# print('生成一百万数字相加需要 %s 秒' % when)

print('最小数：%s' % min(nums))
print('最大数：%s' % max(nums))
# 保存开始时间戳
start_timestamp = time.time()
print('和为：%s' % sum(nums))
# 保存结束时间戳
end_timestamp = time.time()
# 计算计算用时
when = end_timestamp - start_timestamp
print('一百万数字相加需要 %s 秒' % when)

# tets[]