from keras.models import load_model
new_model = load_model('emotionClassifier.h5')
import numpy as np

from keras.preprocessing import image

test_image = image.load_img('dataset/single_prediction/Geraldine_Chaplin_0004.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = new_model.predict(test_image)
#training_set.class_indices
if result[0][0] == 1:
    prediction = 'Anger'
if result[0][1] == 1:
    prediction = 'Disgust'
if result[0][2] == 1:
    prediction = 'Happiness'
if result[0][3] == 1:
    prediction = 'Neutral'
if result[0][4] == 1:
    prediction = 'Sadness'
if result[0][5] == 1:
    prediction = 'Surprise'

print(result)
print(prediction)
