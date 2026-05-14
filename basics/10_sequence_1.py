# for
programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)

for char in 'hello':
    print(char)

# for嵌套
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num)


# while
count = 0
while count < 5:
    print(count)
    count += 1 

# while猜数字
secret_number = 3
guss = 0

while guss != secret_number:
    guss = int(input("请输入一个数字: "))
    if guss < secret_number:
        print("太小了！")
    elif guss > secret_number:
        print("太大了！")
    else:
        print("恭喜你，猜对了！")

# break和continue
for num in range(1, 10):
    if num == 5:
        break  # 当num等于5时，退出循环
    print(num)  # 输出: 1, 2, 3, 4
for num in range(1, 10):
    if num % 2 == 0:
        continue  # 当num是偶数时，跳过当前循环的剩余部分
    print(num)  # 输出: 1, 3, 5, 7, 9
    