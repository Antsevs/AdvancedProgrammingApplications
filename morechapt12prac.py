import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.linear_model import LinearRegression #Estimator

##STEP 1, DEFINE INPUT AND OUTPUT FEATURES
rides = pd.read_csv('archive\cab_rides.csv').dropna() #dropna gets rid of missing values

#input dataframe
X = rides[['distance']]

#output dataframe
y = rides[['price']]

#output dataframe array
y_array = np.ravel(y)


##STEP 2, INITIALIZE ESTIMATOR

model = LinearRegression()


##STEP 3, FITTING ESTIMATOR

model.fit(X,y)

b = model.intercept_
print('\nModel intercept: ', b)

a = model.coef_
print('\nModel Coefficient: ', a)


##STEP 4, PREDICTION
# predicting for 2, 3, and 5 miles distance 
X_test = pd.DataFrame({'distance': [2.0, 3.0, 5.0]})

y_pred = model.predict(X_test)
print('\n Predicted outputs for 2, 3, and 5 mile trips = ', y_pred)


##STEP 5, ESTIMATOR PERFORMANCE EVALUATION

p_score = model.score(X,y)
print('\nR-squared Score for the prediction of the complete dataframe: ', p_score)
