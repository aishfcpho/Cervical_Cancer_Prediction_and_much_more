import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fields = [
 'pelvic_incidence',    
'pelvic_tilt',
'lumbar_lordosis_angle',   
 'sacral_slope',   
 'pelvic_radius',   
 'degree_spondylolisthesis',   
 'pelvic_slope', 
 'Direct_tilt', 
 'thoracic_slope', 
 'cervical_tilt', 
'sacrum_angle',
 'scoliosis_slope', 'outcome']
data = pd.read_csv("./datasets/Dataset_spine.csv")
# Drop the unnamed column in place (not a copy of the original)#
data.drop('Unnamed: 13', axis=1, inplace=True)
data = pd.concat([data, pd.get_dummies(data['Class_att'])], axis=1)
data.drop(['Class_att','Normal'], axis=1, inplace=True)
data.columns = fields
training = (data.drop("outcome", axis=1))
testing = data["outcome"]
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
#   Split into training/testing datasets using Train_test_split
X_train, X_test, y_train, y_test = train_test_split(training, testing, test_size=0.33, random_state=22, stratify=testing)

import numpy as np

# convert to numpy.ndarray and dtype=float64 for optimal
array_train = np.asarray(training)
array_test = np.asarray(testing)
print(array_train.shape)
print(array_test.shape)

#   Convert each pandas DataFrame object into a numpy array object. 
array_XTrain, array_XTest, array_ytrain, array_ytest = np.asarray(X_train), np.asarray(X_test), np.asarray(y_train), np.asarray(y_test)

from keras.models import Sequential
from keras.layers import Dense, Activation
import keras
print(array_XTrain.shape)
print(array_ytrain.shape)


model = Sequential()
model.add(Dense(32, activation='tanh', input_dim=12))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

labels = keras.utils.to_categorical(array_ytrain, num_classes=10)
test_labels = keras.utils.to_categorical(array_ytest, num_classes=10)
history = model.fit(array_XTrain, labels,epochs=1000, batch_size=30)
scores = model.evaluate(array_XTest, test_labels, verbose=0)

print("Score:", scores)
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
print("Saved model to disk")

weights = model.layers[0].get_weights()[0]
biases = model.layers[0].get_weights()[1]