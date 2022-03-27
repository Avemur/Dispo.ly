import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import pathlib

batch_size = 32
img_height = 180
img_width = 180

train_dir = 'train/'
train_dir = pathlib.Path(train_dir)

val_dir = 'test/'
val_dir = pathlib.Path(val_dir)

training_data = tf.keras.utils.image_dataset_from_directory(
  train_dir,
  image_size=(img_height, img_width),
  batch_size=batch_size)

val_data = tf.keras.utils.image_dataset_from_directory(
  val_dir,
  image_size=(img_height, img_width),
  batch_size=batch_size)

data_aug = keras.Sequential(
  [layers.RandomFlip("horizontal", input_shape=(img_height, img_width, 3)),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
   ]
)

class_names = training_data.class_names

import matplotlib.pyplot as plt

'''plt.figure(figsize=(10, 10))
for images, labels in training_data.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")'''

AUTOTUNE = tf.data.AUTOTUNE

training_data = training_data.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_data = val_data.cache().prefetch(buffer_size=AUTOTUNE)

normalization_layer = layers.Rescaling(1./255)

num_classes = len(class_names)

model = Sequential([
  data_aug,
  layers.Rescaling(1.0/255, input_shape=(img_height, img_width, 3)),

  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Dropout(0.2, input_shape=(16,)),

  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Dropout(0.2, input_shape=(32,)),

  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Dropout(0.2, input_shape=(64,)),

  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dropout(0.2, input_shape=(128,)),
  layers.Dense(num_classes)
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.summary()

history = model.fit(
  training_data,
  validation_data=val_data,
  epochs=20
)

img = tf.keras.utils.load_img(
    'test/compost/compost5.jpg', target_size=(img_height, img_width)
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)
predictions = model.predict(img_array)

score = tf.nn.softmax(predictions[0])
print(class_names[np.argmax(score)])

print(np.max(score))
#class_names ['cardboard', 'compost', 'glass', 'metal', 'paper', 'plastic', 'trash']

model.save('model1')