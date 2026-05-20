languages = {'spanish','english','russian','chinese'}
for language in languages:
    print(language)
# 若想要跟踪每个元素的索引，可以创建一个计数器变量并在每次迭代时递增它
index = 0

for language in languages:
    print(f"{index}: {language}")
    index += 1
# 但是，Python提供了一个内置函数enumerate()，可以同时获取元素   的索引和值，简化了代码
for index, language in enumerate(languages):
    print(f"{index}: {language}")
# enumerate()函数接受一个可迭代对象作为参数，并返回一个枚举对象。枚举对象是一个迭代器，每次迭代返回一个包含索引和值的元组。默认情况下，索引从0开始，但你可以通过传递一个可选的start参数来指定索引的起始值
for index, language in enumerate(languages, start=1):
    print(f"{index}: {language}")