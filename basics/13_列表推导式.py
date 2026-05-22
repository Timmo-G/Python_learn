# 本节之前使用：
even_numbers = []

for i in range(21):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)  # 输出: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 列表推导式是一种简洁的语法，用于从一个可迭代对象创建一个新的列表
# 语法: [expression for item in iterable if condition]
# 生成0到20的偶数列表
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)  # 输出: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

numbers = [1, 2, 3, 4, 5]
result = [(i,'even')if i % 2 == 0 else (i,'odd')for i in numbers]
print(result)  # 输出: [(1, 'odd'), (2, 'even'), (3, 'odd'), (4, 'even'), (5, 'odd')]

# 代码
even_numbers = [num for num in range(21) if num % 2 == 0]

# 可以这样理解：
# 1. Python 看到这个结构，知道要创建一个列表推导式
# 2. 它自动创建一个临时变量叫 `num`
# 3. 让 `num` 依次取 0, 1, 2, ..., 20 这些值
# 4. 每次检查 `num % 2 == 0`
# 5. 如果为真，就把当前的 `num` 值放入新列表

# 实验一：跟踪变量变化
print('开始列表推导式...')

even_num = []
for num in range(5):
    print(f'当前 num: {num}')
    if num % 2 == 0:
        even_num.append(num)
        print(f'条件成立 添加 {num} 到列表')
    else:
        print(f'条件不成立 {num} 跳过')
    
print(f'最终结果: {even_num}')
print(f'尝试访问 num: ',end ='')

try:
    print(num)
except NameError:
    print('变量num不存在了')