import pandas as pd
import matplotlib as plt
import sklearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:\\Users\\Sagar\\Desktop\\Think42Labs\\student-performance.csv")            # read the student-performance csv into a pandas dataframe

df['mm'] = df['mm'].replace('Male','Male,')                      # Clean data in the gender column 
df['mm'] = df['mm'].replace('Female','Female,')

dummy = pd.get_dummies(df)                                       # Write the categorical variables as dummies and print them out
print('Coding categorical variables:')
print(dummy.head())

Y = dummy['Total Marks']                                         # Use 'Total Marks' as the dummy variable and other variables as the indicator variables
X = dummy.drop('Total Marks',axis = 1)


lm = LinearRegression()                                          # Build a linear regression model after splitting the examples into training and test sets   
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size= 0.33,random_state = 5)
lm.fit(X_train,Y_train)

print("The mean square error on the training set is:" )          # Print out the mean error on the training and test tests and the estimated coefficients
print(np.mean((Y_train-lm.predict(X_train))**2))
print("The mean square error on the test set is :")
print(np.mean((Y_test-lm.predict(X_test))**2))
est_coeff = pd.DataFrame(list(zip(X.columns,lm.coef_)),columns = ('features','estimated_coefficients'))
print(est_coeff)

plt.scatter(lm.predict(X),Y)
plt.xlabel("Predicted Marks")                                    # Plot the predicted marks vs marks graph for all training examples
plt.ylabel("Marks")
plt.title("Marks vs Predicted Marks")
plt.show()




