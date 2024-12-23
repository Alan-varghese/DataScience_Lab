color=['red','red','red','yellow','yellow','yellow','yellow','yellow','red','red']
Type=['sports','sports','sports','sports','sports','suv','suv','suv','suv','sports']
origin=['domestic','domestic','domestic','domestic','imported','imported','imported','imported','domestic','imported','imported']
stolen=['yes','no','yes','no','yes','no','yes','no','no','yes']
from heapq import merge
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
color_encoded=le.fit_transform(color)
print("color:",color_encoded)
Type_encoded=le.fit_transform(Type)
print("Type:",Type_encoded)
origin_encoded=le.fit_transform(origin)
label=le.fit_transform(stolen)
print("origin:",origin_encoded)
print("stolen:",label)
features=list(zip(color_encoded,Type_encoded,origin_encoded))
print(features)