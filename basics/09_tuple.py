# 元组可以创建有序序列 保存不同类型的数据
developer = ("张三", 18, "男", "软件开发")
print(developer)
print(developer[0])  # 张三
print(developer[1])  # 18
print(developer[2])  # 男
print(developer[3])  # 软件开发

# 元组的元素不能修改
# developer[0] = "李四"  # TypeError: 'tuple' object does not support item assignment

# 访问元组的元素
print(developer[0])  # 张三
print(developer[1])  # 18
print(developer[2])  # 男
print(developer[3])  # 软件开发

# 另一种创建元组tuple()
developer2 = tuple(["李四", 25, "女", "数据分析"])
print(developer2)

# 查看一项是否在元组中
print("张三" in developer)  # True
print("李四" in developer)  # False
print("李四" in developer2)  # True

# 像处理列表一样解包元组
name, age, gender, profession = developer
print(name)  # 张三
print(age)  # 18
print(gender)  # 男
print(profession)  # 软件开发

# 收集剩余元素
name, *rest = developer
print(name)  # 张三
print(rest)  # [18, '男', '软件开发']

# 对元组使用切片
print(developer[1:3])  # 输出: (18, '男')
print(developer[:2])   # 输出: ('张三', 18)
print(developer[2:])   # 输出: ('男', '软件开发')
print(developer[:])    # 输出: ('张三', 18, '男', '软件开发')


