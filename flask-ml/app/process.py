from tensorflow.keras.preprocessing import image
import tensorflow as tf
import numpy as np
import urllib
from tensorflow.keras.preprocessing import image
from io import BytesIO

def predictImage(url):
    try:
        model = tf.keras.models.load_model("./app/model.h5")

        with urllib.request.urlopen(url) as data:
            img1 = image.load_img(BytesIO(data.read()), target_size=(150, 150))
    
        Y = image.img_to_array(img1)        
        X = np.expand_dims(Y,axis=0)
        X_normalized = X / 255.0

        value_predicted = model.predict(X_normalized)

        if value_predicted >= 0.5:
            return 'Non Anemia'
        else:
            return 'Anemia'

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 'Error'