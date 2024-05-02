import numpy as np

a  = np.arange(1,11)
a

b = np.arange(11,21)
b

c = np.concatenate((a,b))
c

d = np.append(a,100)
d
a

#2D
e = np.array([[1,2],[3,4]])
e

f = np.append(e,[[10],[20]],axis = 1)
f

g =  np.append(e,[[10,20]],axis = 0)
g