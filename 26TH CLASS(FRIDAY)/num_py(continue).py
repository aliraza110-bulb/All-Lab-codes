import numpy as np

# array1=np.array([[1,2,3],[5,87,9]])

# np.save('file1.npy',array1)
# np.save('file2.npy',array1)

# load_array=np.load('file1.npy')
# print(load_array)

# array2=np.array([[1,23,587],[5876,865,546]])
# array3=([[155,3264],[89,56435]])

# np.savez('file2.npy',file1=array2,file2=array3)




np.seterr(divide='raise')


array1 = np.array([1, 2, 3])
array2 = np.array([0, 2, 0])

try:
    result = np.divide(array1, array2)

except ZeroDivisionError as e:
    print("Error ! cannot divide by zero")



