import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(precision=4)

def main():

    ### Part 1 - Input

    # Ones column buffer
    ones = np.ones((433, 1))
    ones_2 = np.ones((74, 1))

    # Input
    inputArr = np.loadtxt(open("housing_train.txt", "rb"), delimiter=" ", usecols = range(12))
    x_train = np.concatenate((ones, inputArr), axis=1)
    y_train = np.loadtxt(open("housing_train.txt", "rb"), delimiter=" ", usecols = [13])

    inputArr2 = np.loadtxt(open("housing_test.txt", "rb"), delimiter=" ", usecols = range(12))
    x_test = np.concatenate((ones_2, inputArr2), axis=1)
    y_test = np.loadtxt(open("housing_test.txt", "rb"), delimiter=" ", usecols = [13])


    ### Part 2 - compute optimal weight vector w
    print "Training W: "
    w_train = compute_w(x_train, y_train)
    print w_train
    print "Testing W: "
    w_test = compute_w(x_test, y_test)
    print w_test

    ### part 3 -- compute SSE
    print "Training SSE: "
    print compSSE(x_train, y_train, w_train)
    print "Training SSE: "
    print compSSE(x_test, y_test, w_test)




def compute_w(x,y):
    ### compute optimal weight vector w
    xTx = np.matmul(np.transpose(x), x)
    xTx_inverse = np.linalg.inv(xTx)
    xTy = np.matmul(np.transpose(x), y)

    w = np.matmul(xTx_inverse, xTy)
    return w

def compSSE(x, y, w):
    ### compute SSE
    e1 = np.transpose(y - np.matmul(x, w))
    e2 = y - np.matmul(x, w)
    e3 = np.matmul(e1, e2)
    return e3

if __name__ == '__main__':
    main()
