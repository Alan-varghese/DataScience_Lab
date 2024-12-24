from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('data.csv')
X = df[['Weight', 'Volume']]
y = df[['C02']]
X = X.values
y = y.values
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)  # Changed random_state to an integer
print(x_train)
print(y_train)

regr = LinearRegression()
regr.fit(x_train, y_train)
predictedC02 = regr.predict([[2300, 1300]])
print(predictedC02)