import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
from sklearn.model_selection import train_test_split
data = pd.read_csv('./datasets/kag_risk_factors_cervical_cancer.csv')
# json_file = open("cervical_cancer_data.json", 'w')
#plt.show()
#print(data.describe())

training = (data.drop('Biopsy', axis=1))
testing = data['Biopsy']
X_train, X_test, y_train, y_test = train_test_split(training, testing, test_size=0.33, random_state=22, stratify=testing)
array_XTrain, array_XTest, array_ytrain, array_ytest = np.asarray(X_train), np.asarray(X_test), np.asarray(y_train), np.asarray(y_test)
np.place(array_XTrain, array_XTrain == '?', [0])
np.place(array_XTest, array_XTest == '?', [0])
print(array_XTrain.shape)
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Dropout
import keras

model = Sequential()
model.add(Dense(units=500, 
                input_dim=35, 
                kernel_initializer='uniform', 
                activation='relu'))
model.add(Dropout(0.5))

#Hidden layer 1
model.add(Dense(units=200,  
                kernel_initializer='uniform', 
                activation='relu'))
model.add(Dropout(0.5))

#Output layer
model.add(Dense(units=1,
                kernel_initializer='uniform', 
                activation='sigmoid'))

print(model.summary())
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
labels = keras.utils.to_categorical(array_ytrain)
test_labels = keras.utils.to_categorical(array_ytest)
history = model.fit(x=array_XTrain, y=labels,epochs=1000, batch_size=30)
scores = model.evaluate(array_XTest, test_labels, verbose=0)
print("Score: ", scores[1])

model_json = model.to_json()
with open("cervical_cancer_model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("cervical_cancer_weights.h5")
print("Saved model to disk")

#from sklearn.svm import SVC
#from sklearn.metrics import accuracy_score
#clf = SVC(kernel='linear')
#clf.fit(array_XTrain, array_ytrain)
#pred = clf.predict(array_XTest)
#score = accuracy_score(pred, array_ytest)
#print(score)
#from sklearn.externals import joblib
#joblib.dump(clf, 'cervical_cancer_classifier.pk1')
#clf = joblib.load('./cervical_cancer_classifier.pk1')
#pred = clf.predict(array_XTest)
#score = accuracy_score(pred, array_ytest) 
#print(score)
#print(len(array_XTrain))
#print(len(array_XTest))