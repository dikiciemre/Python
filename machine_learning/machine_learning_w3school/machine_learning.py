#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:15:09 2023

@author: emredikici
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats






"""
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = np.mean(speed) # dizinin ortalamasını bulur.

print(mean)
"""





"""
median = np.median(speed) # Medyan, bir veri setini sıralandığınızda ortadaki değeri ifade eder. 

print(median)
"""





"""
mode = stats.mode(speed)

print(mode)
"""






"""
std = np.std(speed)

print(std)
"""






"""
var = np.var(speed)

print(var)
"""





"""
percentile = np.percentile(speed, 75)

print(percentile)
"""





"""
uniform = np.random.uniform(0.0, 5.0, 20)

print(uniform)
"""





"""
x = np.random.normal(5.0, 1.0, 10000)

plt.hist(x, 100)
plt.show()
"""






"""
x1 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y1= [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x1, y1)
plt.show()
"""






#         ************* Regression *************


# *****Linear Regression*****




"""
x2 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y2 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x2, y2)
plt.show()
"""






"""
x3 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y3 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x3, y3)

def myfunc(x3):
  return slope * x3 + intercept

mymodel = list(map(myfunc, x3))

plt.scatter(x3, y3)
plt.plot(x3, mymodel)
plt.show()
"""






"""
x4 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y4 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x4, y4)

print(r)
"""




# *****Polynomial Regression*****



"""
x5 = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y5 = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x5, y5, 3))

myline = np.linspace(1, 22, 100)

plt.scatter(x5, y5)
plt.plot(myline, mymodel(myline))
plt.show()
"""





# R-Squared
"""
x6 = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y6 = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x6, y6, 3))

print(r2_score(y6, mymodel(x6)))
"""






# Predict Future Values
"""
x7 = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y7 = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x7, y7, 3))

speed = mymodel(17)
print(speed)
"""








# Bad Fit?
"""
x8 = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y8 = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = np.poly1d(np.polyfit(x8, y8, 3))

myline = np.linspace(2, 95, 100)

plt.scatter(x8, y8)
plt.plot(myline, mymodel(myline))
plt.show()
"""







#         ************* Machine Learning - Train/Test *************



"""
np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))

myline = np.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()
"""




# R2
"""
from sklearn.metrics import r2_score

np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))

r2 = r2_score(train_y, mymodel(train_x))

print(r2)
"""






# Bring in the Testing Set
"""
from sklearn.metrics import r2_score

np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))

r2 = r2_score(test_y, mymodel(test_x))

print(r2)
"""









#         ************* Creating a Confusion Matrix *************




"""
from sklearn import metrics

actual = np.random.binomial(1,.9,size = 1000)
predicted = np.random.binomial(1,.9,size = 1000)

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

cm_display.plot()
plt.show()



# F-score calculate
F1_score = metrics.f1_score(actual, predicted)


# Specificity calculate
Specificity = metrics.recall_score(actual, predicted, pos_label=0)


# Accuracy calculate
Accuracy = metrics.accuracy_score(actual, predicted)


# Precision calculate
Precision = metrics.precision_score(actual, predicted)


# Sensitivity_recall calculate
Sensitivity_recall = metrics.recall_score(actual, predicted)
"""







#         ************* Machine Learning - Hierarchical Clustering *************





"""
from scipy.cluster.hierarchy import dendrogram, linkage


x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))

linkage_data = linkage(data, method='ward', metric='euclidean')
dendrogram(linkage_data)

plt.show()
"""





"""
from sklearn.cluster import AgglomerativeClustering


x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))

hierarchical_cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
labels = hierarchical_cluster.fit_predict(data)

plt.scatter(x, y, c=labels)
plt.show()
"""








#         ************* Machine Learning - Logistic Regression *************


"""
from sklearn import linear_model


#Reshaped for Logistic function.
X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X,y)

#predict if tumor is cancerous where the size is 3.46mm:
predicted = logr.predict(np.array([3.46]).reshape(-1,1))
print(predicted)
"""






# Coefficient
"""
from sklearn import linear_model

#Reshaped for Logistic function.
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X,y)

log_odds = logr.coef_
odds = numpy.exp(log_odds)

print(odds)
"""







# Probability
"""
def logit2prob(logr,x):
  log_odds = logr.coef_ * x + logr.intercept_
  odds = np.exp(log_odds)
  probability = odds / (1 + odds)
  return(probability)
"""









"""
from sklearn import linear_model
# kodun açıklaması
#3.78 0.61 The probability that a tumor with the size 3.78cm is cancerous is 61%.

#2.44 0.19 The probability that a tumor with the size 2.44cm is cancerous is 19%.

#2.09 0.13 The probability that a tumor with the size 2.09cm is cancerous is 13%.

X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X,y)

def logit2prob(logr, X):
  log_odds = logr.coef_ * X + logr.intercept_
  odds = np.exp(log_odds)
  probability = odds / (1 + odds)
  return(probability)

print(logit2prob(logr, X))
"""







#         ************* Preprocessing - Categorical Data *************



"""
from sklearn import linear_model


# Veri oluştur
data = {
    'Car': ['Toyota', 'Mitsubishi', 'Skoda', 'Fiat', 'Mini'],
    'Model': ['Aygo', 'Space Star', 'Citigo', '500', 'Cooper'],
    'Speed': [160, 180, 175, 165, 200],
    'Weight': [790, 1160, 929, 865, 1140],
    'CO2': [99, 95, 95, 90, 105]
}

# DataFrame oluştur
car_data = pd.DataFrame(data)

# DataFrame'i göster
print(car_data)


ohe_cars = pd.get_dummies(car_data[['Car']]) # One Hot Encoding


X = pd.concat([car_data[['Speed', 'Weight']], ohe_cars], axis=1)
y = car_data['CO2']

regr = linear_model.LinearRegression() # linner regresyon
regr.fit(X,y)

##predict the CO2 emission of a Volvo where the speed is 180, and the weight is 1300:
predictedCO2 = regr.predict([[180, 1300,0,0,0,0,0]])

print(predictedCO2)
"""








#         ************* Machine Learning - K-means *************



"""
from sklearn.cluster import KMeans


x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))
inertias = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()
"""



















