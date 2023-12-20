# BloodyHappy FrontEnd

## Introduction

This is the BloodyHappy Machine Learning Model

## Prerequisites

Before you begin, make sure you have the following installed:

- Tensorflow@2.12.0
- Pillow@10.1.0
- MatplotLib
- Numpy

## How to Replicate This Project on Your Local Machine

1. **Clone this repository:**

    ```bash
    git clone https://github.com/CapstoneProject-BloodyHappy/MachineLearning.git
    ```

2. **Train the Model**

  Run all cells inside Model-1.ipynb

3. **Saved Model**

  Uncommet the command for saving model 
  
  ```bash
  model.save("model_name.h5")
  ```

4. **Stored the Model**

   Stored the model on the flask-ml/app

5. **Model Path**

   On flask-ml/app/process.py add the path to the model.h5

    ```bash
    model = tf.keras.models.load_model("path/to/your/model.h5")
    ```
  
