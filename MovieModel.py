import pandas as pd
import matplotlib as plt
import sklearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:\\Users\\Sagar\\Desktop\\Think42Labs\\updated_movies.csv",encoding = 'latin-1')                 #read the updated_movies.csv saved in the previous file 

del df['star']                                                                          #delete the actor name and movie name columns 
del df['name']
    

dummy = pd.get_dummies(df)                                                              #get dummy variables for the remaining categorical variables
print('Coding categorical variables:')
print(dummy.head())                                                                     

Y = dummy['gross']                                                                      # use gross revenue as the depedent variable
X = dummy.drop('gross',axis = 1)                                                        # use remaining variables as the predictors

lm = LinearRegression()                                                                 # Fit a linear regression model on the dataset 
lm.fit(X,Y)

est_coeff = pd.DataFrame(list(zip(X.columns,lm.coef_)),columns = ('features','estimated_coefficients'))
print(est_coeff)

plt.scatter(lm.predict(X),Y)                                                            #plot the Predicted revenue vs the revenue on all training examples
plt.xlabel("Predicted revenue")     
plt.ylabel("Revenue")
plt.title("Revenue vs Predicted Revenue")
plt.show()
