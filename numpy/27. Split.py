import numpy as np

a = np.arange(1,21)
a
np.split(a,4)  #sections num must be can divide size of a

np.split(a,5)

a = a.reshape(5,4)
a

np.hsplit(a,4)
np.vsplit(a,5)