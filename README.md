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
    cd Model-1
    ```

2. **Train the Model**

  Run all cells inside Model-1.ipynb

3. **Saved Model**

  Uncommet the command for saving model 
  
  ```bash
  model.save("model_name.h5")
  ```

4. **Stored the Model**

   Stored the saved h5 model in Google Cloud Storage Bucket and use the link to load the model in the Flask API

  
