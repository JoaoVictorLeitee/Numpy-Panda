import numpy as np

if __name__ == '__main__':
    a = np.arange(10)
    print(a)
    print(a.ndim)

    print('______________________')
    b = np.arange(20).reshape(4,5,1)
    print(b)
    print(b.ndim)