import numpy as np

x = [[1,230,176],[1,254,185],[1,243,183],[1,233,180]]
y = [1655,1850,1709,1766]

matrix = np.array(x)
matrixT = matrix.transpose()

yVector = np.array(y)

multi = np.matmul(matrixT, yVector)
multiMatrix = np.matmul(matrixT, matrix)

minusOne = np.linalg.matrix_power(multiMatrix, -1)

matrixFinal = np.matmul(minusOne, multi)

print(matrixFinal)