import numpy as np
def create_matrix(mc):
    print("Array"+str(mc)+"Elements")
    array_1=map(int,input().split())
    array_1=np.array(list(array_1))
    print("Array"+str(mc)+"Elements")
    row,column=map(int,input().split())
    if(len(array_1)!=(row*column)):
        print("Row and Column size doesnt match with total elements!! retry")
        return create_matrix(mc)
    array_1=array_1.reshape(row,column)
    print("Array"+str(mc))
    print(array_1)
    return array_1
arr1=create_matrix(1)
arr2=create_matrix(2)
if(arr1.shape==arr2.shape):
    print("\Dot Product")
    print(np.dot(arr1,arr2))
else:
    print("\Dimension Doesn't Match")
