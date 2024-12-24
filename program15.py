from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout,Conv2D,MaxPool2D,Flatten
from tensorflow.keras import utils
from sklearn.metrics import accuracy_score
[X_train,y_train],[X_test,y_test]=mnist.load_data()
X_train=X_train.reshape(X_train.shape[0],28,28,1)
X_test=X_test.reshape(X_test.shape[0],28,28,1)
X_train=X_train.astype('float32')
X_test=X_test.astype('float32')
X_train/=255
X_test/=255
n_classes=10
print("Shape before one-hot encoding: ",y_train.shape)
y_train = utils.to_categorical(y_train, n_classes)
y_test = utils.to_categorical(y_test, n_classes)
print("Shape after one-hot encoding: ",y_train.shape)
model=Sequential()
model.add[Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=(28,28,1))]
model.add[MaxPool2D(pool_size=(2,2))]
model.add[Flatten()]
model.add(Dense(128,activation='relu'))
model.add[Dense(n_classes,activation='softmax')]
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(X_train,y_train,batch_size=128,epochs=10,verbose=1,validation_data=(X_test,y_test))