import numpy as np
# 特殊矩阵构造np.diag([a,b,c])
# 对角矩阵
S = np.diag([2,0.5,1.0])
a = np.array([1,2,3])
A = np.diag(a)

print(a)
print(A)
print(S)

# np.eye(n) 单位矩阵
A_inv = np.linalg.inv(A)
is_inverse = np.allclose(A @ A_inv,np.eye(3))
print(is_inverse)



# 矩阵属性
# 逆矩阵np.linalg.inv
B = np.array([[1,2],
              [2,3]])
B_inv = np.linalg.inv(B)
# 行列式det
B_det = np.linalg.det(B)
# 向量长度norm
v = np.array([3,4])
norm = np.linalg.norm(v)
print(norm)



# 随机生成np.random.randn() 标准正态分布
w = np.random.randn(3,3)
# random.rand() 均匀分布
u = np.random.rand(3,3)



# 数组操作与验证
# 角度转弧度
theta = np.radians(90)
print(theta)

# 合并数组stack与concatente
z = np.array([1,2,3])
x = np.array([4,5,6])
n = np.array([7,8,9])
np.stack([z,x,n],axis = 0)#升维
#1 2 3
#4 5 6
#7 8 9
np.concatenate([z,x,n],axis = 0)#不升维
#1 2 3 4 5 6 7 8 9

#np.zeros与ones
np.zeros((2,3))
np.ones((2,3))
np.zeros_like(A)
np.ones_like(A)

# allclose浮点数安全比较