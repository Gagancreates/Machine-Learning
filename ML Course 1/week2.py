#lets implement multiple linear regression
#let the paramters be
import numpy as np
# w=np.array([1, 2, -1.2])
# #let the features be
# x=np.array([10, 20, 30])
# d=np.array([0.2, 0.4, 0.9])
# #lets calculate the hypothesis or the output function
# f=np.dot(w,x)+ 3
# print(f)

# #lets implement gradient descent here
# w= w - 0.1*d
# print(w)
# print(w[0])
# # so numpy parallely processes the requests 

# a = np.arange(4)
# print(f"a:  {a}")
# print(a.shape)
# print([x+d])


# # creating matrices using numpy
# X=np.zeros((3, 3))
# print(X)   # this creates a 3x3 matrix with all entries as 0

# matrix=np.array([[1, 2,3], [2, 3,4], [123, 4, 5]])
# print(matrix)

#most usefule case using the reshape option
# m1=np.arange(10).reshape(5, 2)
# print(m1[4,1])


# m2=np.arange(6).reshape(-1, 3)              #HERE -1 AUTOMATICALLY DECIDESTHE NUMBER OF ROWS BASED ON THE NUMBER OF COLUMNS ENTERED
# print(m2)


matir=np.array([[1,2,3], [2, 3, 5]])
print(matir[0])