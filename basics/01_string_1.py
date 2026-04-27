# 单双引号包裹的相同

#多行可用三引号

my_str_1 = """hello,
world"""

my_str_2 = '''hello,
myself'''

#字符串包含了引号
    # 1. 用双引号包裹但引号 或单引号包裹双引号

    # 2. \用于转意

#查看字符串是否被包含在主串中
my_str = 'hello'
print('hell',my_str)#返回一个布尔值

#len可以查看长度
my_str_4 = 'nice try'
print(len(my_str_4))

#字符串支持索引（下标） 支持负索引，-1代表最后一个，-2代表倒数第二个
my_str_5 = 'Hello world'
print(my_str_5[-1])  # d
print(my_str_5[-2]) # l

#字串是不可修改变量 只能赋值，不能改变
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello
greeting = 'hi'

# greeting[0] = 'H' 
# # TypeError: 'str' object does not support item assignment

#字串插接（仅仅适用字串）
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

#内置的str可以转换为字符串
name = 'Gdy'
age = 24
str_plus = name + ' ' + str(age)
print(str_plus)

name_and_age = name
name_and_age += str(age)
print(name_and_age)

#f-string
name = 'G'
score = 420
name_age = f'my name is {name},my score is {score}'
print(name_age)

