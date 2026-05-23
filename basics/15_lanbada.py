def square(num):
    return num ** 2
# lambda 匿名函数
# lambda 函数是一种匿名函数，使用 lambda 关键字定义。它可以接受任意数量的参数，但只能有一个表达式。lambda 函数通常用于需要一个简单函数作为参数的场景，例如在 filter()、map() 和 sorted() 等函数中。
# 语法: lambda arguments: expression
# 计算平方
square_lambda = lambda num: num ** 2
print(square_lambda(5))  # 输出: 25

