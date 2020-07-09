# Melanoma Detection

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical](#technical)
  * [Installation](#installation)
  * [Run](#run)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [To Do](#to-do)
  * [Bug / Feature Request](#bug---feature-request)
  * [Technologies Used](#technologies-used)
  * [Team](#team)
  * [License](#license)
  * [Credits](#credits)

## Demo
Trained model is deployed using Heroku Platform
Link: https://detection-melanoma.herokuapp.com/

## Overview
This project is aimed to classifiy an image as malignant or benign and thereby detect skin cancer [Melanoma].

## Dataset and preprocessing
ISIC 2019 Dataset for benign and malignant cases available in Kaggle
JPEG images are converted to TFRecord format for faster processing and used tensor flow dataset class to load the data in batches.
TFRecord files created are uploaded back to kaggle and hence into GCS Cloud.
TFRecord files are created for various sizes of images - 224x224 60% center cropped, 384x384 50% center cropped.

## Motivation
Motivation to do this project is to apply state of the art computer vision techinques to real world applications

## Technical 
Tensorflow deep learning frame work is used.

Model trained on Kaggle TPU

EfficientNetB4 pre trained model is used, Please refer the research paper for the architecture of EfficientNet -

Images are augmented with respect to zoom,shear,rotate left/right flip up/down during training randomly.

Significant Class imbalance problem was seen as expected in medical images. Number of positive data points were 584 compared to 30,264 Negative data points
Training data is under sampled i.e on EDA of the meta deta it was seen that for the same part of the body, for the same patient multiple images were found.These images were
of different sizes or taken from a different angle,natural augmentation!!!!. But since we do augmentation during training, i felt there is no harm in not using these duplicate
images and i was right as well [Checked the performance of the model with all the available data as well, there was almost no difference].

Loss functions experimented are Binary crossentropy, weighted binary cross entropy, focal loss  -> weighted binary cross entropy gave better performance.

Cyclic learning rate, Learning rate with decay,Learning rate decay with warmup has been experimented -> Learning rate decay with warmp gave better results.

Batch size of 8,16,32 has been experimented.

Stratified KFold technique is used for cross validation splits.

AUC achieved is 0.895


## Installation
The Code is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Run

#### Windows User



## Deployement on Heroku
Set the environment variable on Heroku as mentioned in _STEP 1_ in the __Run__ section. [[Reference](https://devcenter.heroku.com/articles/config-vars)]

![](https://i.imgur.com/TmSNhYG.png)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── app 
│   ├── __init__.py
│   ├── main.py
│   ├── model
│   ├── static
│   └── templates
├── config
│   ├── __init__.py
├── processing
│   ├── __init__.py
├── requirements.txt
├── runtime.txt
├── LICENSE
├── Procfile
├── README.md
└── wsgi.py
```

## To Do


## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/rowhitswami/Indian-Currency-Prediction/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/rowhitswami/Indian-Currency-Prediction/issues/new). Please include sample queries and their corresponding results.

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://keras.io/img/logo.png" width=200>](https://keras.io/) [<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://www.kindpng.com/picc/b/301/3012484.png" width=200>](https://aws.amazon.com/s3/) 

[<img target="_blank" src="https://sentry-brand.storage.googleapis.com/sentry-logo-black.png" width=270>](https://www.sentry.io/) [<img target="_blank" src="https://openjsf.org/wp-content/uploads/sites/84/2019/10/jquery-logo-vertical_large_square.png" width=100>](https://jquery.com/)

## Team


## License
[![Apache license](https://img.shields.io/badge/license-apache-blue?style=for-the-badge&logo=appveyor)](http://www.apache.org/licenses/LICENSE-2.0e)

Copyright 2020 Rohit Swami

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Credits
