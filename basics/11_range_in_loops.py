# range生成一个整数序列，常用于循环中
# range(start, stop, step)
# stop参数是必需的，表示生成的整数序列的结束值（不包含该值）。start参数是可选的，默认为0，表示生成的整数序列的起始值。step参数也是可选的，默认为1，表示生成的整数序列的步长。
# 生成0到9的整数序列
for i in range(10):
    print(i)
# 生成1到10的整数序列
for i in range(1, 11):
    print(i)
# 生成0到9的偶数序列
for i in range(0, 10, 2):
    print(i)    
# 生成10到1的整数序列
for i in range(10, 0, -1):
    print(i)

# range只接受整数参数，如果传入非整数参数会抛出TypeError异常
# for i in range(1.5):  # TypeError: 'float' object cannot be interpreted as an integer
#     print(i)

# 配合list函数可以将range对象转换为列表
numbers = list(range(5))
print(numbers)  # 输出: [0, 1, 2, 3, 4]

evennumbers = list(range(0, 10, 2))
print(evennumbers)  # 输出: [0, 2, 4, 6, 8]

