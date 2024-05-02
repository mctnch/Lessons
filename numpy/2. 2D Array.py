import numpy as np

a = np.array([1,2,3])
a.ndim
a

#2D Array == overlap of 1D Arrays

b = np.array([[1,2,3],[4,5,6]])
b.ndim
b

li = [[1,2,3],[4,5,6],[7,8,9]]
c = np.array(li)
c


tu = ((1,2,3),(4,5,6),(7,8,9))
d = np.array(tu)
d


#access member
#array[row][column]
b 
b[0][0]
b[1][2]
b[-1][-2]
b[1][0] = 8
b

