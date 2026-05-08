# append() 在末尾添加一项
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # 输出: [1, 2, 3, 4]
# 将列表添加到末尾
my_list.append([5, 6])
print(my_list)  # 输出: [1, 2, 3, 4, [5, 6]]

# extend() 将一个可迭代对象的元素添加到列表末尾
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # 输出: [1, 2, 3, 4, 5]
# extend() 将字符串的每个字符添加到列表末尾
my_list.extend('abc')
print(my_list)  # 输出: [1, 2, 3, 4, 5, 'a', 'b', 'c']

# insert() 在指定位置插入一项 
my_list = [1, 2, 3]
my_list.insert(1, 'a')
print(my_list)  # 输出: [1, 'a', 2, 3]
# insert() 在索引0处插入元素
my_list.insert(0, 'start')
print(my_list)  # 输出: ['start', 1, 'a', 2, 3]
# insert() 在索引末尾处插入元素
my_list.insert(len(my_list), 'end')
print(my_list)  # 输出: ['start', 1, 'a', 2, 3, 'end']

# remove() 删除列表中的第一项匹配项
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)
print(my_list)  # 输出: [1, 3, 2, 4]
# remove() 删除列表中的第一项匹配项
my_list.remove(2)
print(my_list)  # 输出: [1, 3, 4]
# 如果要删除的项不存在，Python会抛出ValueError异常
# my_list.remove(5)  # 这行代码会抛出ValueError: list.remove(x): x not found

# pop() 删除并返回指定位置的元素
my_list = [1, 2, 3]
popped_item = my_list.pop(1)
print(popped_item)  # 输出: 2
print(my_list)     # 输出: [1, 3]
# pop() 删除并返回最后一个元素
last_item = my_list.pop()
print(last_item)  # 输出: 3
print(my_list)    # 输出: [1]
# 如果要删除的索引不存在，Python会抛出IndexError异常
# my_list.pop(5)  # 这行代码会抛出IndexError: pop index out of range

# sort() 对列表进行原地排序
my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)  # 输出: [1, 2, 3, 4]
# sort() 使用自定义的排序键
my_list = ['apple', 'banana', 'cherry','gdy']
my_list.sort(key=len)
print(my_list)  # 输出: ['apple', 'cherry', 'banana']
# sort() 使用自定义的排序键和反向排序
my_list.sort(key=len, reverse=True)
print(my_list)  # 输出: ['banana', 'cherry', 'apple']

# sorted() 返回一个新的排序列表
my_list = [3, 1, 4, 2]
sorted_list = sorted(my_list)
print(sorted_list)  # 输出: [1, 2, 3, 4]
print(my_list)     # 输出: [3, 1, 4, 2]  # 原列表保持不变
# sorted() 使用自定义的排序键 
my_list = ['apple', 'banana', 'cherry','gdy']
sorted_list = sorted(my_list, key=len)
print(sorted_list)  # 输出: ['apple', 'cherry', 'banana']
# sorted() 使用自定义的排序键和反向排序
sorted_list = sorted(my_list, key=len, reverse=True)
print(sorted_list)  # 输出: ['banana', 'cherry', 'apple']

# reverse() 反转列表中的元素
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # 输出: [3, 2, 1]

# index 方法
my_list = ['a', 'b', 'c', 'd']
print(my_list.index('c'))  # 输出: 2
# 如果要查找的项不存在，Python会抛出ValueError异常 
# print(my_list.index('e'))  # 这行代码会抛出ValueError: 'e' is not in list

