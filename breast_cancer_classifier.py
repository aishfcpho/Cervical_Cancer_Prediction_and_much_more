import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from sklearn.model_selection import train_test_split
data = pd.read_csv('./datasets/breast_cancer_dataset.csv')
data = data.drop("id", axis=1)
#print(data.columns)
data = (data.drop("Unnamed: 32", axis=1))
seaborn.set()
corr = data.corr()
f, ax = plt.subplots(figsize=(12,9))
heat_map = seaborn.heatmap(corr, cmap='inferno', annot=True)
#plt.show()
from sklearn.svm import SVC
clf = SVC('rbf')
training = data.drop("diagnosis", axis=1)
testing = data["diagnosis"]
X_train, X_test, y_train, y_test = train_test_split(training, testing, test_size=0.33, random_state=22, stratify=testing)
array_XTrain, array_XTest, array_ytrain, array_ytest = np.asarray(X_train, dtype=np.float), np.asarray(X_test, dtype=np.float), np.asarray(y_train), np.asarray(y_test)
for i in range(0, len(array_ytrain)):
    if array_ytrain[i] == 'M' :
        array_ytrain[i] = 1
    else :
        array_ytrain[i] = 0
for i in range(0, len(array_ytest)):
    if array_ytest[i] == 'M' :
        array_ytest[i] = 1
    else :
        array_ytest[i] = 0
from sklearn.metrics import accuracy_score
#np.place(array_XTrain, array_XTrain == , [0])
#np.place(array_XTest, array_XTest == , [0])
clf.fit(array_XTrain, array_ytrain)
#pred = clf.predict(array_XTest)
#score = accuracy_score(pred, array_ytest)
#print(score)