import numpy as np
fm = [1, 8, 6] #-8.245
afm1 = [2, 0, -4] #-16.030
afm2 = [2, -16, 12] #-15.565
afm3 = [4, 16, 8] #-32.615
afm4 = [4, 0, -8] #-32.170
afm5 = [4, 0, 8] #-32.228
afm6 = [4, 0, -24] #-32.200

data = np.array([fm, afm1, afm2, afm3, afm4, afm5, afm6])
values = np.array([-8.245, -16.030, -15.565, -32.615, -32.170, -32.228, -32.200])
print(data)
c = np.linalg.lstsq(data, values, rcond=None)
print(c)
A = np.array([[1, -4, 1],
              [2, 1, -2],
              [1, 3, -3]])
b = np.array([-4, -2, -2])
s = np.linalg.lstsq(A, b, rcond=None)

