# filter 筛选
word = ['apple', 'banana', 'cherry', 'date', 'elderberry']
def is_long_word(word):
    return len(word) > 4
long_word = list(filter(is_long_word,word))
print(list(long_word))  # 输出: ['apple', 'banana', 'cherry', 'elderberry']
#filter() 函数用于从可迭代对象中选择满足特定条件的元素。filter() 函数接受一个函数和一个可迭代对象作为它的参数。

# map 映射
#map() 接受一个函数和一个可迭代对象作为它的参数

celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]

# sum
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # 输出: 15
toatal_new = sum(numbers,statr=10)
print(toatal_new)  # 输出: 25

