import numpy as np

a = np.arange(1,11)
a
np.delete(a,2)

b = np.arange(1,13)
b
b= np.arange(1,13).reshape(4,3)
b
np.delete(b,2,axis = 0)
np.delete(b,2,axis = 1)
