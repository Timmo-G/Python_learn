#通过缩排来确定代码块
age = 20
if age >= 18:
    print('你已经成年了')  
else:    
    print('你还未成年')
#布尔值
age = 20
is_adult = age >= 18
print(is_adult)  # 输出: True
#条件表达式
age = 20
status = '成年' if age >= 18 else '未成年'
print(status)  # 输出: 成年 

# and or not
age = 20
is_adult = age >= 18
is_student = True   
if is_adult and is_student:
    print('你是一个成年学生')
if is_adult or is_student:
    print('你是一个成年或者学生')
if not is_adult:
    print('你还未成年') 
