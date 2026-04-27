#字串切片 string[start:stop]

my_str_1 = 'hello world'
print(my_str_1[1:4])

    # 1. 省略start
my_str = 'Hello world'
print(my_str[:7])  # Hello w
    # 2. 省略stop
my_str = 'Hello world'
print(my_str[2:])
    #3. 省略两个
my_str = 'Hello world'
print(my_str[:])#打印全部

# string[start:stop:step]
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd
    # 小技巧，将start和stop留空 step为-1可以逆置
print(my_str[::-1])