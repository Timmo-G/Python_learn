#列表的基本语法
cities = ['Los Angeles', 'London', 'Tokyo']
#访问列表中的元素
print(cities[0])  # 输出: Los Angeles
print(cities[1])  # 输出: London
print(cities[2])  # 输出: Tokyo
#序号从-1开始
print(cities[-1])  # 输出: Tokyo
print(cities[-2])  # 输出: London
print(cities[-3])  # 输出: Los Angeles
#另一种创建列表的方式list() 构造函数用于将可迭代对象转换为列表
develoer = 'Python'
developer_list = list(develoer)
print(developer_list)  # 输出: ['P', 'y', 't', 'h', 'o', 'n']
#获取列表的长度
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 输出: 5
#特定索引处的值
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages)  # 输出: ['JavaScript', 'Java', 'C++', 'Rust']
# 列表是可变的，只要传入有效的索引，就可以修改列表中的元素
programming_languages[1] = 'Go'
print(programming_languages)  # 输出: ['JavaScript', 'Go', 'C++ ', 'Rust']
#如果传入的索引超出边界，Python会抛出IndexError异常
# programming_languages[4] = 'Swift'  # 这行代码会抛出IndexError: list assignment index out of range 

#删除列表中的元素
del programming_languages[2]  # 删除索引为2的元素，即'C++'
print(programming_languages)  # 输出: ['JavaScript', 'Go', 'Rust']

#查看列表中的元素可以使用in
print('Go' in programming_languages)  # 输出: True
print('C++' in programming_languages)  # 输出: False   

# 列表嵌套
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])  # 输出: [1, 2, 3]
print(matrix[1])  # 输出: [4, 5, 6] 
# 访问嵌套中的列表
print(matrix[0][1])  # 输出: 2
print(matrix[1][2])  # 输出: 6

#解包列表
developer = ['Alice', 34, 'Rust Developer']
name, age, role = developer
print(name)  # 输出: Alice
print(age)   # 输出: 34
print(role)  # 输出: Rust Developer
#收集剩余的元素
numbers = [1, 2, 3, 4, 5]
first, second, *rest = numbers
print(first)  # 输出: 1
print(second) # 输出: 2
print(rest)   # 输出: [3, 4, 5]
#如果赋值和元素个数不匹配，Python会抛出ValueError异常
# name, age = developer  # 这行代码会抛出ValueError: not enough values to unpack (expected 2, got 3)


# 切片操作符的使用
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # 输出: [2, 3, 4]
print(numbers[:3])   # 输出: [1, 2, 3]
print(numbers[2:])   # 输出: [3, 4, 5]
print(numbers[:])    # 输出: [1, 2, 3, 4, 5]
#只想偶数序列
even_numbers = numbers[1::2]
print(even_numbers)  # 输出: [2, 4]
#反转列表  
reversed_numbers = numbers[::-1]
print(reversed_numbers)  # 输出: [5, 4, 3, 2, 1]


