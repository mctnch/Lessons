import numpy as np
a = np.array([1,2,3,4,5,8])
a
np.append(a,40)
np.insert(a,1,100) # add value 100 to be index 1 member of a

#2D
b = np.array([[1,2],[3,4]])
b

np.insert(b,1,100,axis =  0)
np.insert(b,1,100,axis =  1)