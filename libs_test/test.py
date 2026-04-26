# env_test.py - 用于验证Python环境和基本库
import sys
import numpy as np

print("=== 您的Python开发环境验证报告 ===")
print(f"1. Python版本: {sys.version}")
print(f"2. NumPy版本: {np.__version__}")

# 测试NumPy的基本功能
arr = np.array([1, 2, 3, 4, 5])
print(f"3. 创建的NumPy数组: {arr}")
print(f"4. 数组的平均值: {np.mean(arr)}")
print(f"5. 数组的标准差: {np.std(arr):.2f}")

# 生成一个随机矩阵
random_matrix = np.random.rand(2, 3)
print(f"6. 一个2x3的随机矩阵:\n{random_matrix}")

print("=" * 40)
print("✅ 环境验证通过！可以开始您的Python之旅了。")