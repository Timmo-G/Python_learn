fruits = ['apple', 'banana', 'cherry']
# 传统方法
fruit_now = []
for i in fruits:
    fruit_now.append(f'{i}有{len(i)}个字母')
print(fruit_now)  # 输出: ['apple', 'banana', 'cherry']
# 列表推导式
fruit_tomorrow = [f'{i}有{len(i)}个字母'for i in fruits]
print(fruit_tomorrow)  # 输出: ['apple', 'banana', 'cherry']

print("传统方法：", fruit_now)
print("推导式：   ", fruit_tomorrow)
print("两者相同吗？", fruit_now == fruit_tomorrow)
