import numpy as np
def create_matrix(mc):
    print("Array"+str(mc)+"Elements")
    array_1=map(int,input().split())
    array_1=np.array(list(array_1))
    print("Array"+str(mc)+"Row Column")
    row,column=map(int,input().split())
    if(len(array_1)!=(row*column)):
        print("Row and Column size doesn't match")
        return create_matrix(mc)
    array_1=array_1.reshape(row,column)
    print("Array"+str(mc))
    print(array_1)
    print("Transpose")
    return array_1
print(create_matrix(1).transpose())