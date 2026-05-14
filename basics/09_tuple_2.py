# 元组的sorted不会返回新的元组，而是返回一个列表
t = (3, 1, 2)
sorted_t = sorted(t)
print(sorted_t)  # 输出: [1, 2, 3]
print(t)  # 输出: (3, 1, 2) 元组本身没有改变
# 元组的sort方法不存在，会抛出AttributeError
# t.sort()  # AttributeError: 'tuple' object has no attribute 'sort'

# 为可迭代的对象元组自定义排序 可选reverse 和 key
t2 = ("apple", "banana", "cherry")
sorted_t2 = sorted(t2, reverse=True)
print(sorted_t2)  # 输出: ['cherry', 'banana', 'apple']
sorted_t2_key = sorted(t2, key=len)
print(sorted_t2_key)  # 输出: ['apple', 'banana', 'cherry'] 按长度排序

