import sys
import json
import numpy as np
data = np.array([])
#data = json.loads(sys.argv[1])

#print(loaded_model.predict(new_array))
questionGroups = [["To start off, how old are you?"], ["Number of sexual partners", "When did you have your first sexual encounter(age)?", "How many pregnancies did you have?"], ["Do you smoke?", "How many years did you smoke for in the past?", "How many packs/yr would you say you smoked in your prime?"], ["Did/Do you take hormonal contraceptives", "How long did you take hormonal contraceptives for?"], ["Did/do you use an Intra-uterine device for birth control?", "How many years did you use IUDs for?"], ["Have you ever contracted a sexually transmitted disease?", "If so, how many?", "Condylomatosis", "Cervical Condylomatosis", "Vaginal Condylomatosis", "Vulvo-perineal Condylomatosis", "Syphilis", "Pelvic Inflammatory disease", "Genital Herpes", "Molluscum Contagiosum", "AIDs", "HIV", "Hepatitis B", "HPV(Human Papillomavirus", "Total number of STD diagnoses", "Time since first diagnosis", "Time since last diagnosis"], ["Did you ever go through a Dx test?", "Did you test positive for Dx test(Cancer)?", "Did you test positive for Dx test(CIN)?", "Did you test positive for Dx test HPV?"], ["Did you ever test positive on a Hinselmann test(Colposcopy)?", "Did you test positive on a Schiller test?", "Did you ever test positive for any urinary tract diseases known from a cytology test?"]]
for x in questionGroups :
    for y in x :
        a = float(input(y+" "))
        data = np.append(data, a)
        print("\n")
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
#print(data)
json_file = open('./cervical_cancer_model.json', 'r')
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
loaded_model.load_weights("Cervical_cancer_weights.h5")
loaded_model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
new_array = data.reshape([1,35])
pred = loaded_model.predict(new_array)
print(pred)
#sys.stdout.flush()