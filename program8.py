from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
irisdata=load_iris()
print(irisdata.data)
x=irisdata.data
y=irisdata.target
x_train,x_test,y_train,y_test=train_test_split(x,y)
Knn=KNeighborsClassifier(n_neighbors=1)
Knn.fit(x_train,y_train)
print(x_test)
print(Knn.predict(x_test))
print(y_test)
result=Knn.predict([[2,4,6,2]])
print(irisdata.target_names[result])