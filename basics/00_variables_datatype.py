
# 声明变量
name = 'gdy'
age = 25
# 变量名全小写 并且用下划线
user_name = 'G'
# 尽量避免使用单字母变量

# print用法
print('Hello World')

print('My nane is','Gdy')
#常见的数据类型
my_int_var = 10
print(type(my_int_var))
my_bool_var = True
print(type(my_bool_var))
my_float_var = 1.1
print(type(my_float_var))
my_string_var = 'G'
print(type(my_string_var))
my_set_var = {'hello',9,0.5}# 无序的唯一元素集合
print(type(my_set_var))
my_dictionary_var = {'name':'Gdy','age':24}#字典 匹配配对
print(type(my_dictionary_var))
my_tuple_var = ('Gdy',9 ,1)#元组 不可变的有序集合
print(type(my_tuple_var))
my_range_var = range(10)
print(type(my_range_var))
my_list_var = [22, 'Hello world', 3.14, True]#列表 有序集合

my_none_var = None
# isinstance的使用
isinstance('Hello world', str) # True
