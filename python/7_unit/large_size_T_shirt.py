# 大号T恤：编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
# 使其默认情况下制作一件印有字样“I lovt Python”的大号T恤。
# 调用这个函数来制作一如下T恤：一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）。

def make_shirt(size, txt='I LOVE PYTHON'):
    return {'尺寸': size, '字样': txt}


print(make_shirt('M码'))
print(make_shirt('XL码', 'EXPEDIENT'))
