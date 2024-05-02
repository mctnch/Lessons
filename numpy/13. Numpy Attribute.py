import numpy as np

a = np.array([1,2,3,4])
a
a.ndim
a.dtype

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
b
b.ndim
b.dtype

c = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],dtype= "complex")
c 

a.shape
b.shape
c.shape


a.size

b.size

c.size

b.dtype
b.itemsize #unit : bytes ( 8 bits = 1 byte)

c.dtype