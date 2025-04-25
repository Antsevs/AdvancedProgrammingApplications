import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.linear_model import LinearRegression


def menu(choice):
    global closeVal #make closeVal available globally to modify within menu
    
    if choice == "12.1":
        closeVal = False

        #read csv file and remove null entries
        rides = pd.read_csv('cab_rides.csv').dropna()

        #randomly rearrange and grab first 100 rows of updated dataframe
        A = rides.sample(100)
        A.to_csv('cab_rides_rearranged.csv')

        #Part i
        plt.figure(1)
        sb.countplot(data = A, x = 'cab_type')

        plt.xlabel('Cab Type', fontsize = '14')
        plt.ylabel('Count', fontsize='14')
        plt.title('Number of of each cab type in dataframe', fontsize = '16')

        #Part ii
        plt.figure(2)
        sb.histplot(data = A, x = 'distance', bins = 10)

        plt.xlabel('Distance (miles)', fontsize = '14')
        plt.ylabel('Count', fontsize = '14')
        plt.title('Cabs sorted by Distance per Dataframe', fontsize = '16')

        #Part iii
        plt.figure(3)
        sb.scatterplot(data = A, x = 'distance', y = 'price')

        plt.xlabel('Distance (miles)', fontsize = '14')
        plt.ylabel('Price (dollars)', fontsize = '14')
        plt.title('Distribution of Distance to Price', fontsize = '16')
        
        plt.show()
    elif choice == "12.2":
        closeVal = False
        
        #define input and output features
        rides = pd.read_csv('cab_rides.csv').dropna()

        reverseRides = rides.tail(1000)
        
        X = reverseRides[['distance']]
        y = reverseRides[['price']]
        y_array = np.ravel(y)

        #initialize estimator
        model = LinearRegression()

        #fit estimator
        model.fit(X,y)

        b = model.intercept_

        a = model.coef_[0]

        #predict
        X_test = pd.DataFrame({'distance': [10.0, 50.0, 80.0]})
        y_pred = model.predict(X_test)

        #estimator performance evaluation

        p_score = model.score(X,y)

        #linear equation is modelCoefficient(distance) + modelIntercept
        
        sb.scatterplot(data = reverseRides, x = 'distance', y = 'price')
        prices = a * reverseRides['distance'] + b
        plt.plot(reverseRides['distance'], prices, label = 'Regression Line')
        plt.xlabel('Distance (miles)', fontsize = '14')
        plt.ylabel('Price (dollars)', fontsize = '14')
        plt.title('Distribution of Distance to Price with Linear Model Regression Equation', fontsize = '16')

        plt.show()
    elif choice == "exit":
        print("Thank you, have a nice day.")
        closeVal = True
    else:
        print("Invalid choice, please try again.")
        closeVal = False

closeVal = False #instantiate continual check for exit code

while closeVal == False:
    choice = input("Please choose which exercise you would like to view (12.1 or 12.2)\nor type 'exit' to close the program\n")
    menu(choice)
