import numpy as np
fm = [1, 8] #-8.245
afm1 = [2, 0] #-16.030
afm2 = [2, -16] #-15.565
afm3 = [4, 16] #-32.615
afm4 = [4, 0] #-32.170
afm5 = [4, 0] #-32.228
afm6 = [4, 0] #-32.200

values = np.array([-8.245, -16.030, -15.565, -32.615, -32.170, -32.228, -32.200])
data = np.array([fm, afm1, afm2, afm3, afm4, afm5, afm6])
c = np.linalg.lstsq(data, values, rcond=None)
print(c)