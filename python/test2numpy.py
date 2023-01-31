import numpy as np
 
mt = np.array([12,34,26,18,10])
print(mt)

mtfloat = np.array([1,2,3], dtype = np.float64)
mtint = np.array([1,2,3], dtype = np.int32)
print(mtfloat)
print(mtint)

um = np.ones([5,7])
print(um)

diagonal = np.eye(5)
print(diagonal)

#valores aleatórios
ale = np.random.random((5))
ale1 = np.random.randn((5))
ale2 = (10*np.random.random((3,4)))

print(ale)
print(ale1)
print(ale2)

#unique remove repetições
j = np.array(12,12,11,13,14,13,1,1,13,4,45,76,21,21)
j = np.unique(j)
print(j)