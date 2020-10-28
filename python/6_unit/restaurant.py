# 餐馆：创建一个名为menu_orders的列表，在其中包含各种菜名；再创建一个名为finished_menu的空列表。
# 遍历列表menu_orders，对于其中的每种菜都打印一条消息，如“你的西红柿炒鸡蛋已出炉。”，并将其移动到列表finished_menu。
# 所有菜品都制作好后，打印一条消息，将这些菜品列出来。

menu_orders = ['鱼香肉丝', '水煮肉片', '回锅肉', '青椒肉丝']
finished_menu = []

while menu_orders:
    menu_order = menu_orders.pop()
    print('您的{}已出炉'.format(menu_order))
    finished_menu.append(menu_order)

print('完成的菜单列表：')
for greens in finished_menu:
    print(greens, end='、')

