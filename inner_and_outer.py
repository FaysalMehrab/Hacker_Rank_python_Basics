
import numpy as np

A = list(map(int, input().split()))
arr1 = np.array(A)

B = list(map(int, input().split()))
arr2 = np.array(B)



print (np.inner(A, B))
print (np.outer(A, B))