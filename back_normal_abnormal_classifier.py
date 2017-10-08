from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
json_file = open('model.json', 'r')
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
loaded_model.load_weights("model.h5")
loaded_model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
