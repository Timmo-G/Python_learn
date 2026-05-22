
# **Python异常处理：`try-except`详细教学**

您观察得很仔细！`try-except`是 Python 中非常重要的**异常处理**机制。让我为您详细解释。

## **1. 什么是异常处理？**

### **类比理解**

想象您要去朋友家：

* **正常情况** ：到达朋友家 → 按门铃 → 进门 ✅
* **异常情况** ：到达朋友家 → 按门铃 → 没人开门 ❌
* 怎么办？打电话、发微信、改天再来...

在编程中：

* **正常情况** ：代码顺利执行
* **异常情况** ：遇到错误（异常）
* **异常处理** ：告诉程序遇到错误时应该怎么办

### **没有异常处理的情况**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python"># 假设我们有一个文件
# 直接读取文件
content = open("不存在的文件.txt").read()  # ❌ 会崩溃
print("这行代码不会执行")</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

 **运行结果** ：

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-markdown">FileNotFoundError: [Errno 2] No such file or directory: '不存在的文件.txt'
# 程序崩溃，停止运行</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

---

## **2. `try-except`基础语法**

### **基本结构**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">try:
    # 尝试执行的代码（可能出错）
    代码块
except 异常类型:
    # 如果发生指定类型的异常，执行这里
    异常处理代码</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

### **完整格式**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">try:
    # 尝试执行的代码
    pass
except 异常类型1:
    # 处理异常类型1
    pass
except 异常类型2:
    # 处理异常类型2
    pass
except (异常类型3, 异常类型4):  # 同时处理多种异常
    # 处理异常类型3或4
    pass
except Exception as e:  # 捕获所有异常
    # 处理其他所有异常
    # 可以获取异常信息
    pass
else:
    # 如果没有异常发生，执行这里
    pass
finally:
    # 无论是否发生异常，最后都会执行这里
    pass</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

---

## **3. 实际示例解析**

### **示例1：处理文件不存在异常**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">try:
    # 尝试打开一个可能不存在的文件
    file = open("不存在的文件.txt", "r")
    content = file.read()
    file.close()
    print("文件内容：", content)
except FileNotFoundError:
    # 如果文件不存在，执行这里
    print("错误：找不到文件！")
    print("建议：请检查文件路径和名称")

print("程序继续运行...")</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

 **输出** ：

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-markdown">错误：找不到文件！
建议：请检查文件路径和名称
程序继续运行...</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

 **关键点** ：

1. 即使文件不存在，程序也不会崩溃
2. 会执行 `except`块中的代码
3. 然后继续执行后面的代码

### **示例2：处理除零错误**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">try:
    x = 10
    y = 0
    result = x / y  # ❌ 10 ÷ 0 会出错
    print(f"结果是：{result}")
except ZeroDivisionError:
    print("错误：不能除以零！")
    print("建议：检查除数是否为0")

print("计算完成")</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

 **输出** ：

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-markdown">错误：不能除以零！
建议：检查除数是否为0
计算完成</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

### **示例3：处理多种异常**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">try:
    num = int(input("请输入一个数字："))
    result = 100 / num
    print(f"100 ÷ {num} = {result}")
except ValueError:
    print("错误：请输入有效的数字！")
except ZeroDivisionError:
    print("错误：不能输入0！")
except Exception as e:
    print(f"发生了未知错误：{type(e).__name__} - {e}")

print("感谢使用计算器")</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

 **测试** ：

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-markdown">输入: abc
输出: 错误：请输入有效的数字！

输入: 0
输出: 错误：不能输入0！

输入: 5
输出: 100 ÷ 5 = 20.0</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

---

## **4. 获取异常信息**

### **使用 `as`关键字获取异常对象**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"异常类型：{type(e).__name__}")
    print(f"异常信息：{e}")
    print(f"异常详情：{e.args}")</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

 **输出** ：

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-markdown">异常类型：ZeroDivisionError
异常信息：division by zero
异常详情：('division by zero',)</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

### **完整示例**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">try:
    # 尝试各种可能出错的操作
    num = int("不是数字")
    result = 10 / 0
    file = open("不存在的文件.txt")
except ValueError as e:
    print(f"值错误：{e}")
except ZeroDivisionError as e:
    print(f"除零错误：{e}")
except FileNotFoundError as e:
    print(f"文件未找到：{e}")
except Exception as e:
    print(f"其他错误：{type(e).__name__} - {e}")</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

---

## **5. `else`和 `finally`子句**

### **`else`：没有异常时执行**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">try:
    num = int(input("请输入数字："))
    result = 100 / num
except ValueError:
    print("请输入有效数字")
except ZeroDivisionError:
    print("不能输入0")
else:
    # 只有在没有异常时执行
    print(f"计算成功！结果是：{result}")
    print("结果已保存到数据库")</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

### **`finally`：无论如何都会执行**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">try:
    file = open("data.txt", "r")
    content = file.read()
    print("文件内容：", content)
except FileNotFoundError:
    print("文件不存在")
finally:
    # 无论是否发生异常，都会执行
    print("清理资源...")
    # 这里通常用于关闭文件、释放资源等
    try:
        file.close()  # 尝试关闭文件
    except NameError:
        pass  # 如果 file 不存在（比如文件没打开），就跳过
    print("程序结束")</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

 **`finally`的经典用法** ：

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">file = None
try:
    file = open("重要文件.txt", "r")
    # 处理文件...
except FileNotFoundError:
    print("找不到文件")
finally:
    if file:  # 检查文件是否成功打开
        file.close()  # 确保文件被关闭
        print("文件已关闭")</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

---

## **6. 回到实验一的代码**

让我们再看您提到的实验一代码：

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python"># 实验 1：跟踪变量变化
print("开始列表推导式...")

even_numbers = []
for i in range(5):  # 模拟推导式的内部过程
    print(f"当前临时变量 i = {i}")
    if i % 2 == 0:
        even_numbers.append(i)
        print(f"  条件成立，加入列表。当前列表：{even_numbers}")
    else:
        print(f"  条件不成立，跳过")

print(f"最终结果：{even_numbers}")
print(f"尝试访问 i：", end="")
try:
    print(i)
except NameError:
    print("变量 i 不存在了")</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

### **逐行解释**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">print(f"尝试访问 i：", end="")
# 打印 "尝试访问 i："，不换行（end="" 表示结尾不加换行符）

try:
    print(i)  # 尝试打印变量 i
except NameError:  # 如果发生 NameError 异常（变量未定义）
    print("变量 i 不存在了")  # 执行这里</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

 **执行过程** ：

1. 先打印 "尝试访问 i："
2. 然后 `try`块中尝试打印 `i`
3. 如果 `i`不存在（NameError），执行 `except`块
4. 打印 "变量 i 不存在了"

 **输出** ：

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-markdown">尝试访问 i：变量 i 不存在了</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

---

## **7. 常见异常类型**

| 异常类型              | 触发时机     | 示例                             |
| --------------------- | ------------ | -------------------------------- |
| `SyntaxError`       | 语法错误     | `print("hello"`（缺少右括号）  |
| `NameError`         | 变量未定义   | `print(undefined_var)`         |
| `TypeError`         | 类型错误     | `"hello" + 123`（字符串+数字） |
| `ValueError`        | 值错误       | `int("abc")`                   |
| `IndexError`        | 索引越界     | `lst = [1,2]; print(lst[5])`   |
| `KeyError`          | 字典键不存在 | `d = {}; print(d["key"])`      |
| `FileNotFoundError` | 文件不存在   | `open("nonexistent.txt")`      |
| `ZeroDivisionError` | 除零错误     | `10 / 0`                       |
| `AttributeError`    | 属性错误     | `"hello".append("!")`          |
| `ImportError`       | 导入错误     | `import nonexistent_module`    |

### **示例：各种异常处理**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">def demonstrate_exceptions():
    try:
        # 1. NameError
        print(undefined_variable)
      
    except NameError:
        print("处理了 NameError：变量未定义")
  
    try:
        # 2. TypeError
        result = "hello" + 123
      
    except TypeError:
        print("处理了 TypeError：类型不匹配")
  
    try:
        # 3. IndexError
        lst = [1, 2, 3]
        print(lst[10])
      
    except IndexError:
        print("处理了 IndexError：索引超出范围")
  
    try:
        # 4. KeyError
        d = {"name": "张三"}
        print(d["age"])
      
    except KeyError:
        print("处理了 KeyError：字典键不存在")
  
    try:
        # 5. AttributeError
        num = 10
        num.append(20)
      
    except AttributeError:
        print("处理了 AttributeError：对象没有这个属性")

# 运行演示
demonstrate_exceptions()</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

---

## **8. 自定义异常处理逻辑**

### **自定义错误信息**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "错误：除数不能为零"
    except TypeError:
        return "错误：请输入数字"

print(divide_numbers(10, 2))    # 5.0
print(divide_numbers(10, 0))    # 错误：除数不能为零
print(divide_numbers(10, "a"))  # 错误：请输入数字</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

### **记录错误日志**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">import traceback
import datetime

def safe_divide(a, b):
    try:
        return a / b
    except Exception as e:
        # 记录错误日志
        with open("error_log.txt", "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] 错误: {type(e).__name__}\n")
            f.write(f"参数: a={a}, b={b}\n")
            f.write(f"追踪:\n{traceback.format_exc()}\n")
            f.write("-" * 50 + "\n")
        return None

# 测试
print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # None，但错误被记录到文件</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

### **重试机制**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">import time

def connect_to_server(max_retries=3):
    for attempt in range(max_retries):
        try:
            print(f"尝试连接服务器... (第{attempt+1}次)")
            # 模拟可能失败的连接
            if attempt < 2:  # 前两次模拟失败
                raise ConnectionError("连接失败")
            print("连接成功！")
            return True
        except ConnectionError as e:
            print(f"连接失败: {e}")
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # 指数退避
                print(f"等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
    print("达到最大重试次数，连接失败")
    return False

connect_to_server()</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

---

## **9. 最佳实践**

### **实践1：不要捕获所有异常却不处理**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python"># ❌ 不好的做法
try:
    # 很多代码
    pass
except:
    pass  # 静默忽略所有错误，不知道发生了什么

# ✅ 好的做法
try:
    # 可能出错的代码
    pass
except SpecificError as e:
    # 处理特定错误
    print(f"发生错误: {e}")
    # 记录日志、通知用户等
except Exception as e:
    # 其他错误
    print(f"未知错误: {e}")
    # 记录到日志</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

### **实践2：尽量缩小 try 块的范围**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python"># ❌ 不好的做法
try:
    data = get_data_from_api()  # 可能失败
    process_data(data)          # 可能失败
    save_to_database(data)      # 可能失败
    send_email_report()         # 可能失败
except Exception as e:
    print("出错了，但不知道是哪一步")

# ✅ 好的做法
try:
    data = get_data_from_api()
except ConnectionError:
    print("API连接失败")
    return

try:
    processed = process_data(data)
except ValueError:
    print("数据处理失败")
    return

try:
    save_to_database(processed)
except DatabaseError:
    print("数据库保存失败")
    return</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

### **实践3：使用 else 处理成功情况**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python"># 清晰地区分成功和失败逻辑
try:
    result = risky_operation()
except OperationError as e:
    print(f"操作失败: {e}")
    handle_failure()
else:
    print("操作成功")
    handle_success(result)
finally:
    cleanup_resources()  # 无论成功失败都要清理</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

---

## **10. 常见误区与调试技巧**

### **误区1：过度使用 try-except**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python"># ❌ 用异常处理代替条件判断
try:
    value = my_dict[key]
except KeyError:
    value = default_value

# ✅ 用 get() 方法更合适
value = my_dict.get(key, default_value)</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

### **误区2：隐藏真正的错误**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python"># ❌ 隐藏错误，难以调试
def calculate(data):
    try:
        return complex_calculation(data)
    except:
        return None  # 不知道发生了什么错误

# ✅ 至少记录错误
def calculate_better(data):
    try:
        return complex_calculation(data)
    except Exception as e:
        print(f"计算失败: {e}")
        return None</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

### **调试技巧：打印完整错误信息**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">import traceback

try:
    risky_code()
except Exception as e:
    print("错误类型:", type(e).__name__)
    print("错误信息:", str(e))
    print("完整追踪:")
    traceback.print_exc()  # 打印完整的错误栈</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

---

## **11. 练习题目**

### **练习1：安全计算器**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">def safe_calculator():
    """创建一个安全的计算器，处理所有可能的错误"""
    print("=== 安全计算器 ===")
    print("支持: +, -, *, /")
  
    try:
        num1 = float(input("输入第一个数字: "))
        operator = input("输入运算符 (+, -, *, /): ")
        num2 = float(input("输入第二个数字: "))
      
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("不能除以零")
            result = num1 / num2
        else:
            raise ValueError("不支持的运算符")
          
        print(f"结果: {result}")
      
    except ValueError as e:
        print(f"输入错误: {e}")
    except ZeroDivisionError as e:
        print(f"数学错误: {e}")
    except Exception as e:
        print(f"未知错误: {type(e).__name__} - {e}")
    else:
        print("计算成功!")
    finally:
        print("感谢使用计算器")

# 运行
safe_calculator()</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

### **练习2：文件处理工具**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">def file_processor(filename):
    """安全地读取和处理文件"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
          
        # 处理内容
        lines = content.split('\n')
        word_count = sum(len(line.split()) for line in lines)
      
        print(f"文件: {filename}")
        print(f"行数: {len(lines)}")
        print(f"单词数: {word_count}")
      
    except FileNotFoundError:
        print(f"错误: 文件 '{filename}' 不存在")
    except PermissionError:
        print(f"错误: 没有权限读取文件 '{filename}'")
    except UnicodeDecodeError:
        print(f"错误: 文件 '{filename}' 编码不正确")
    except Exception as e:
        print(f"未知错误: {type(e).__name__} - {e}")
    else:
        print("文件处理完成")

# 测试
file_processor("example.txt")</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

---

## **12. 总结**

### **`try-except`的核心价值**

1. **防止程序崩溃** ：优雅地处理错误，而不是让程序突然停止
2. **提供用户友好信息** ：告诉用户发生了什么，而不是显示技术性错误
3. **资源清理** ：确保文件、网络连接等资源被正确释放
4. **调试辅助** ：记录错误信息，帮助定位问题

### **记住这个模式**

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan isDark"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><pre><code class="language-python">try:
    # 尝试做某事
    do_something_risky()
except SpecificError:
    # 处理已知的特定错误
    handle_specific_error()
except Exception as e:
    # 捕获其他所有错误
    log_error(e)
    handle_unknown_error()
else:
    # 成功时执行
    on_success()
finally:
    # 无论如何都要执行
    cleanup()</code></pre></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

### **关键要点**

1. **`try`** ：包含可能出错的代码
2. **`except`** ：捕获和处理特定异常
3. **`else`** ：没有异常时执行
4. **`finally`** ：无论是否异常都执行
5. **`as`** ：获取异常对象，可以查看详细信息
