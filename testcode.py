import tensorflow as tf
from tensorflow import keras
import numpy as np

model = keras.models.load_model('model1')

def get_prediction(path, model):
    img_height = 180
    img_width = 180

    img = tf.keras.utils.load_img(path, target_size=(img_height, img_width))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)

    #class_names ['cardboard', 'compost', 'glass', 'metal', 'paper', 'plastic', 'trash']
    #              [recycle  ,  compost,  recycle, recycle,  compost, recycle,   trash]

    score = tf.nn.softmax(predictions[0]) # list of probabilities
    index = np.argmax(score)
    if index == 6: #trash
        return 2
    elif index == 1 or index == 4: # compost 
        return 0
    return 1 # recycle

print(str(get_prediction('images/plastic.jpg', model)))