import numpy as np

fm = [1, 8, 6, 12] # -8.245
afm1 = [2, 0, -4, -8]  # -16.030
afm2 = [2, -16, 12, 24] # -15.565
afm3 = [4, 16, 8, 0] # -32.615461
afm4 = [4, 0, -8, 0]  # -32.170
afm5 = [4, 0, 8, -16]  # -32.228
afm6 = [4, 0, -24, 48]  # -32.200
data = [fm, afm1, afm2, afm3, afm4, afm4, afm5, afm6]
values = [-8.245, -16.030, -15.565, -32.615, -32.170, -32.228, -32.200]

eq2 = 1
eq3 = 5
eq4 = 6


A = [data[0], data[eq2], data[eq3], data[eq4]]
b = [values[0], values[eq2], values[eq3], values[eq4]]
print('_________________________________')
print('Inputs:')
print(A[0], b[0], 'fm')
print(A[1], b[1], 'afm', eq2)
print(A[2], b[2], 'afm', eq3)
print(A[3], b[3], 'afm', eq4)
x = np.linalg.solve(A, b)
print('_________________________________')
print('Outs:')
print('Eg =', "%.4f" % x[0], 'eV')
print('J1 =', "%.4f" % x[1], 'eV')
print('J2 =', "%.4f" % x[2], 'eV')
print('J3 =', "%.4f" % x[3], 'eV')
print('_________________________________')