# 大小写转换
m_str_1 = 'gdy'
upperm_str_1 = m_str_1.upper()
print(m_str_1)
print(upperm_str_1)

m_str_2 = 'GDY'
lowm_str_2 = m_str_2.lower()
print(m_str_2)
print(lowm_str_2)

# 新建字串 移除指定的前导和尾随字符。如果未传入参数，则移除前导和尾随空白字符
my_str = ' hello world '
trimmped_str = my_str.strip()
print(my_str)
print(trimmped_str)

# 替换字符串
my_str2 = 'hello world'
replacemy_str = my_str2.replace('hello','hi')
print(my_str2)
print(replacemy_str)

# 拆分字符串将字串按指定的分隔符拆分成字串列表。如果未指定分隔符，则按空白字符拆分。
my_str3 = 'hello world'
split_str = my_str3.split()
print(split_str)

#连接字符串 join将可迭代对象的元素用分隔符连接成一个字串
my_list = ['hello','world']
joined_str = ' ' .join(my_list)
print(joined_str)

# 返回一个布尔值，指示字串是否以指定的前缀开头
my_str = 'hello world'
starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)

# 返回一个布尔值，指示字串是否以指定的后缀结尾
my_str = 'hello world'
end_with_world = my_str.endswith('world')
print(end_with_world)

# 返回 substring 第一次出现的索引，如果未找到则返回 -1。
my_str = 'hello world'
find_world_index = my_str.find('world')
print(find_world_index)

# 返回字串在字串中出现的次数
my_str = 'hhhhello world'
h_count = my_str.count('h')
print(h_count)

# 返回一个字符串 首字母大写 其他全部小写
my_str = 'hellO WoRld'
capital_str = my_str.capitalize()
print(capital_str)

# 如果所有字母都是大/小写，则返回True，否则返回False isupper/islower
my_str = 'hellO WoRld'
isupper_str = my_str.isupper()
islower_str = my_str.islower()
print(isupper_str,islower_str)

# 新建一个字符串 其中每个单词首字母都大写,其余小写
my_str = 'hellO WoRld'
title_str = my_str.title()
print(title_str)

