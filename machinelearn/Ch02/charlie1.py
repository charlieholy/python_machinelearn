from numpy import *
p = random.rand(4,4)
print(p)
randMat = mat(p)
# 矩阵求逆
q = randMat.I
#print(p*q)

print(p.shape[0])
