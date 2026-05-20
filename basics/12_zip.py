developer = ['GodY','HuanglY']
ids = [1,2]
list(zip(ids,developer))# [(1, 'GodY'), (2, 'HuanglY')]转换为列表
# zip()函数接受多个可迭代对象作为参数，并返回一个迭代器，每次迭代返回一个包含来自每个可迭代对象的对应元素

# 使用zip函数和for循环来同时迭代两个列表
for id, name in zip(ids, developer):
    print(f"ID: {id}, Name: {name}")
# 输出:
# ID: 1, Name: GodY
# ID: 2, Name: HuanglY