import numpy as np

#create 0D array
arr = np.array(1)

arr

arr.ndim # check array dimension

#create 1D array 
# list to array
#1
a = np.array([1,2,3]) 
a
a.ndim
# 2
li = [1,2,3,4]    
b = np.array(li)
b

# tuple to array
tu = (1,2,3,4)    # tuple to array
c = np.array(tu)
c