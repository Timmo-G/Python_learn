# 函数定义
def greet(name):
    print(f"Hello, {name}!")

# 函数调用
greet("Alice") 

# 带有默认参数的函数
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()
greet("Bob")

# 带有返回值的函数
def add(a, b):
    return a + b
result = add(5, 3) 
print("The sum is:", result)

# 带有条件语句的函数
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = 10
result = check_even_odd(number)
print(f"{number} is {result}.")

# 递归函数示例
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5 is:", factorial(5))

# 函数的作用域
def outer_function():
    outer_var = "i am outside"
    def inner_function():
        inner_var = "i am inside"
        print(outer_var)
        print(inner_var)
    inner_function()
outer_function()

# nonlocal 关键字示例
def outer_function():
    count = 0
    def inner_function():
        nonlocal count
        count += 1
        print(f"Count is: {count}")
    inner_function()
    inner_function()
outer_function()    

# global 关键字示例
counter = 0
def increment():    
    global counter
    counter += 1
    print(f"Counter is: {counter}")
increment()
increment() 