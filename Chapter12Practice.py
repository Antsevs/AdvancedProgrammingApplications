import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

rides = pd.read_csv('archive\cab_rides.csv')

#first x lines
A = rides.head(3)
print(A)

 #random sample
B = rides.sample()
print(B)

#first x rows and first x columns of dataframe
C = rides.iloc[0:10, 0:4]
print(C)

#extracting certain rows and columns
D = rides.loc[0:4, ['destination', 'price']]
print(D)

plt.figure(1)
sb.countplot(data = rides, x = 'cab_type')

plt.xlabel('Cab Type', fontsize = '14'),plt.ylabel('Count', fontsize = '14')
plt.title('Number of Uber and Lyft in the dataframe', fontsize = '14')

plt.show()
