# 实验一：跟踪变量变化
print('开始列表推导式...')

even_num = []
for num in range(5):
    print(f'当前 num: {num}')
    if num % 2 == 0:
        even_num.append(num)
        print(f'条件成立 添加 {num} 到列表')
    else:
        print(f'条件不成立 {num} 跳过')
    
print(f'最终结果: {even_num}')
print(f'尝试访问 num: ',end ='')

try:
    print(num)
except NameError:
    print('变量num不存在了')