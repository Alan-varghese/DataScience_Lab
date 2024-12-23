a1=['T','T','T','F','F','F']
a2=['T','T','F','F','T','T']
classification=['+','+','-','+','-','-']
from heapq import merge
from sklearn import preprocessing,tree
le=preprocessing.LabelEncoder()
a1_encoded=le.fit_transform(a1)
print("A1:",a1_encoded)
a2_encoded=le.fit_transform(a2)
y=le.fit_transform(classification)
print("A2:",a2_encoded)
print("Classification:",y)
x=list(zip(a1_encoded,a2_encoded))
print(x)
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
tree.plot_tree(clf)