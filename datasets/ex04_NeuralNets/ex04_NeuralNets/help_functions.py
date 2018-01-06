import numpy as np
# to make this notebook's output stable across runs
np.random.seed(1)

def dataset_regression(n=300):
    
    x1=np.sort(np.random.uniform(size=n)*2*np.pi)
    y=np.sin(x1)+np.random.normal(size=n)/4
    x1 = x1.reshape((-1, 1))
    y = y.reshape((-1, 1))
    return x1,y
