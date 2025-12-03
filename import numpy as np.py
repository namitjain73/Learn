import numpy as np



import numpy as np
l1 = [1,2,3,4]
l2 = [5,6,7,8]
n = np.array(l1)
m = np.array(l2)
add = np.add(n,m)
sub = np.subtract(n,m)
mul = np.multiply(n,m)
div = np.divide(n,m)
print(div)





d1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]]
d2 = [[2,3,4],[14,12,15],[47,45,48],[45,59,65]]
n = np.array(d1)
m = np.array(d2)
add = np.add(n,m)
sub = np.subtract(n,m)
mul = np.multiply(n,m)
div = np.divide(n,m)
print(div)


t1 = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
]

t2 = [
    [[1, 1, 1], [2, 2, 2]],
    [[3, 3, 3], [4, 4, 4]],
    [[5, 5, 5], [6, 6, 6]]
]

n = np.array(t1)
m = np.array(t2)

div = np.divide(n, m)


x = 16
print(np.sqrt(x))



arr=np.array([[1,2,3],[4,5,6]])
arr1 = np.array([[6,7,8],[9,8,7]])
print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
# print(arr @ arr1.T)
print(np.dot(arr,arr1.T))

print(arr) 
r2 = arr.reshape(3,2)
print(r2)
