# here I am implementing forward prop to learn what happens under the hood when we use libraries such as tensorflow
import numpy as np
def g(x):
    return 1/(1+ np.exp(-x))

def dense(input, w, b):
    a=g(np.matmul(input, w)+b)
    return a
        
x = np.array([0.5, -1.2])

# Random weights and biases
np.random.seed(42)  # to make output reproducible

w1 = np.random.randn(2, 3)
b1 = np.random.randn(3)

w2 = np.random.randn(3, 4)
b2 = np.random.randn(4)

w3 = np.random.randn(4, 2)
b3 = np.random.randn(2)

w4 = np.random.randn(2, 1)
b4 = np.random.randn(1)


def sequential(x):
    a1=dense(x, w1, b1)
    a2=dense(a1, w2, b2)
    a3=dense(a2, w3, b3)
    output=dense(a3, w4, b4)
    return output

out=sequential(x)
print(f"The output for the forwARD PROPOGATION NN is {out}")