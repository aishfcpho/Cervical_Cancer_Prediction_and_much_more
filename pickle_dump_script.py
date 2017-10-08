import csv
import numpy as np
import pickle

data = np.array([])
with open('./datasets/Dataset_spine.csv', 'r') as lower_back_symptoms :
    reader = csv.reader(lower_back_symptoms, delimiter = ' ', quotechar= '|')
    for row in reader :
        print(x)
        data = np.append(data, row)
        print (row)
print(data)
with open('lower_back_data_pickle', 'wb') as f :
    pickle.dump(data, f)
