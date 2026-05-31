# np.array()
import numpy as np

# 一维向量 从列表创建
v = np.array([1,2,3])
print(v)  # 输出: [1 2 3]
print(type(v))  # 输出: <class 'numpy.ndarray'>
# 二维矩阵 从列表的列表创建
m = np.array([[1,2,3],[4,5,6]])
print(m)  # 输出: [[1 2 3]
          #       [4 5 6]]
print(type(m))  # 输出: <class 'numpy.ndarray'>
#shape 属性,永远要知道自己操作在几维数据
print(v.shape)
print(m.shape)

# 常用工厂函数(不需要通过列表创建数组)
# np.zeros() 创建一个全零数组
zeros_array = np.zeros((2,3))
print(zeros_array)  # 输出: [[0. 0. 0.]
                    #       [0. 0. 0.]]
# np.ones() 创建一个全一数组
ones_array = np.ones((3,4))
print(ones_array)  # 输出: [[1. 1. 1. 1.]
                    #       [1. 1. 1. 1.]
                    #       [1. 1. 1. 1.]]
# np.eye() 创建一个单位矩阵
identity_matrix = np.eye(4)
print(identity_matrix)  # 输出: [[1. 0. 0. 0.]
                        #       [0. 1. 0. 0.]
                        #       [0. 0. 1. 0.]
                        #       [0. 0. 0. 1.]]

# np.arange() 创建一个等差数列
arange_array = np.arange(0, 10, 2)
print(arange_array)  # 输出: [0 2 4 6 8]
# np.linspace() 创建一个等间隔数列
linspace_array = np.linspace(0, 1, 5)
print(linspace_array)  # 输出: [0.  0.25 0.5  0.75 1. ]




# 矩阵乘法
# @ 符号用于矩阵乘法
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = a @ b
print(c)
print(c.shape)

# A * B 逐元素乘法(要求两个矩阵的shape相同)
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
C = A * B
print(C)
print(C.shape)




# np.linalg.inv() 计算矩阵的逆
sigma = np.array([[3.0,1.0],
                  [1.0,3.0]])
# eig计算特征值
eigenvalues,Q = np.linalg.eig(sigma)
print('特征值:',eigenvalues)
print('特征向量:',Q)

Lambda = np.diag(eigenvalues)
sigma_rebuilt = Q @ Lambda @ Q.T
print(np.allclose(sigma,sigma_rebuilt))

print(np.allclose(np.alloclose(Q @ Q.T,np.eye(2))))

# 转置
A = np.array([[1,2,3],[4,5,6]])
print(A.shape)

print(A.T.shape)

# 转置的性质1:(AB)^T = B^T A^T
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.allclose((A @ B).T, B.T @ A.T))

# 转置的性质2: (A^T)^T = A
A = np.array([[1,2],[3,4]])
print(np.allclose((A.T).T, A))  

# 转置的性质3: (A + B)^T = A^T + B^T
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.allclose((A + B).T, A.T + B.T))

# 转置的性质4: (cA)^T = cA^T
A = np.array([[1,2],[3,4]])
c = 2
print(np.allclose((c * A).T, c * A.T))

# 转置的性质5: (A^-1)^T = (A^T)^-1
A = np.array([[1,2],[3,4]])
A_inv = np.linalg.inv(A)
print(np.allclose((A_inv).T, np.linalg.inv(A.T)))
