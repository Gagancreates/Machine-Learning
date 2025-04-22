#implementing a neural network from scratch
# here I am using standard values for the weights w as well as the biases 

# this NN contains a input layer with 2 features for coffee roasting ( temperature, duration) and one hidden layer with 3 neurons
#  and a final output layer with 1 neuron


import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x1=np.array([200.0, 17.0])
w1_1=np.array([1.0, 1.2])
w1_2=np.array([1.0, 1.8])
w1_3=np.array([-1.0, 1.4])

b1_1=0.0
b1_2=1.09
b1_3=-0.9

a1_1=sigmoid(np.dot(w1_1, x1) + b1_1)
a1_2=sigmoid(np.dot(w1_2, x1) + b1_2)
a1_3=sigmoid(np.dot(w1_3, x1) + b1_3)

a1=np.array([ a1_1, a1_2, a1_3])
w2=np.array([1.0, -0.9, 0.7])
b2=0.8

output=sigmoid(np.dot(w2, a1)+ b2)
if output>0.5:
    print(1)
else:
    print(0)