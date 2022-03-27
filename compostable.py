from flask import Flask, render_template, request, Response
from werkzeug.utils import secure_filename


import tensorflow as tf
from tensorflow import keras
import numpy as np
import pathlib

num = 100;

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
    print("Index is " + str(index))
    if index == 6: #trash
        num = 2
        print(num)
    elif index == 1 or index == 4: # compost 
        num = 0
        print(num)
    else:  #recycle
        num = 1
        print(num)

path = 'templates/images'
path = pathlib.Path(path)
image = list(path.glob('*.jpg'))
get_prediction(str(image[0]), model)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("landing.html")

@app.route("/image")
def image():
    return render_template("image.html")

@app.route("/compost", methods=['GET'])
def compost():
    if num==2:
        return render_template("index.html", bestType = "trash", bestTyped = "trashed", image = "https://img.uline.com/is/image/uline/H-4202G?$Mobile_Zoom$")
    elif num==1:
        return render_template("index.html", bestType = "recycle", bestTyped = "recycled", image = "https://m.media-amazon.com/images/I/81cFCbFbxYL._AC_SX522_.jpg")
    else :
        return render_template("index.html", bestType = "compost", bestTyped = "composted", image = "https://www.lawnstarter.com/blog/wp-content/uploads/2019/07/rsz_shutterstock_313682036-compost-bin.jpg")
        
    #https://m.media-amazon.com/images/I/41OY0ymyYoL._AC_.jpg
if __name__ == "__main__":
    app.run(debug=True)