# -*- coding: utf-8 -*-
"""CMPE 258-Deep Learning Project Celestial Body detection .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VPHyh_ckmWXCnIs9wIidbSHDwI2T78Vj

**Celestial Body Object Detector**

# About the project
In this project we have used the Darknet YOLOv4 object detector on our custom dataset. The dataset is comprised of 3 classes.
- Stars
- Spiral Galaxies
- Elliptical Galaxies

**About Darknet:**<br>
Darknet is a high performance open source framework for the implementation of neural networks. Written in C and CUDA, it can be integrated with CPUs and GPUs.
Advanced implementations of deep neural networks can be done using Darknet. These implementations include You Only Look Once (YOLO) for real-time object detection, ImageNet classification, recurrent neural networks (RNNs), and many others.

Darknet has two key dependencies:
- OpenCV
- CUDNN

Note: The data to avoid session storage issues is copied over from the users Google Drive.

**About the Dataset**

As mentioned before the datset is based on 3 classes, the number of images for each class is described as below:

- Stars [ Traing images: 1412, Testing images: 610 ,Total: 2022]
- Spiral Galaxy [ Traing images: 2245, Testing images: 300 ,Total: 2545]
- Elliptical Galaxy [ Traing images: 2352, Testing images: 300 ,Total: 2652]

All in a custom dataset of 7219 images was curated and  manually annotated in Yolo format for this model.

- The dataset for the Star class was taken from the [Astronomy dataset](https://www.kaggle.com/datasets/divyansh22/dummy-astronomy-data)
- The dataset for the Elliptical Galaxy and the Spiral Galaxy was gathered and sorted from  the astro.NN library.

**Cloning the Darknet Repository**
"""

!git clone https://github.com/AlexeyAB/darknet

"""**Enable Opencv and Cuda**"""

# Commented out IPython magic to ensure Python compatibility.
# %cd darknet
!sed -i 's/OPENCV=0/OPENCV=1/' Makefile
!sed -i 's/GPU=0/GPU=1/' Makefile
!sed -i 's/CUDNN=0/CUDNN=1/' Makefile
!sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile

!/usr/local/cuda/bin/nvcc --version

"""**Making Darknet**"""

!make

"""**Defining Helper functions**"""

# Commented out IPython magic to ensure Python compatibility.
def imShow(path):
  import cv2
  import matplotlib.pyplot as plt
#   %matplotlib inline

  image = cv2.imread(path)
  height, width = image.shape[:2]
  resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)

  fig = plt.gcf()
  fig.set_size_inches(18, 10)
  plt.axis("off")
  plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
  plt.show()

# For uploading files
def upload():
  from google.colab import files
  uploaded = files.upload() 
  for name, data in uploaded.items():
    with open(name, 'wb') as f:
      f.write(data)
      print ('saved file', name)

# use this to download a file  
def download(path):
  from google.colab import files
  files.download(path)

"""**Mounting the Google Drive**"""

# Commented out IPython magic to ensure Python compatibility.
# %cd ..
from google.colab import drive
drive.mount('/content/gdrive')

!ln -s /content/gdrive/My\ Drive/ /mydrive
!ls /mydrive

# Commented out IPython magic to ensure Python compatibility.
# %cd darknet

"""**Viewing files**"""

!ls /mydrive/cmpe258

"""**Copying over the files over to the root directory**"""

!cp /mydrive/cmpe258/obj.zip ../
!cp /mydrive/cmpe258/test.zip ../

"""**Unzipping files**"""

!unzip ../obj.zip -d data/
!unzip ../test.zip -d data/

"""**Taking a look at the dataset**"""

imShow('/content/darknet/data/obj/Disk, Edge-on, No Bulge10171.png')

imShow('/content/darknet/data/obj/Smooth, Cigar shaped10361.png')

imShow('/content/darknet/data/obj/Smooth, in-between round21777.png')

imShow('/content/darknet/data/obj/sn12c01_03_352_378_6.jpg')

"""**Copying over the yolov4 configuration file over to the darknet configuration folder**"""

!cp /mydrive/cmpe258/yolov4-obj.cfg ./cfg

"""**Copy over the label files and data file**"""

!cp /mydrive/cmpe258/obj.names ./data
!cp /mydrive/cmpe258/obj.data  ./data

"""**Copying over train and test scripts**"""

!cp /mydrive/cmpe258/generate_train.py ./
!cp /mydrive/cmpe258/generate_test.py ./

"""**Running the train and test scripts**"""

!python generate_train.py
!python generate_test.py

"""**Verifying train and test path files have been made**"""

!ls data/

"""**Downloading pre-trained yolo weights**"""

!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137

"""**Traing weights for our custom dataset**"""

!./darknet detector train data/obj.data cfg/yolov4-obj.cfg /mydrive/cmpe258/backup/yolov4-obj_last.weights -dont_show -map

"""Note:Stopped training at 2500 iterations

**Checking Mean Average Precision (mAP) for different weights**

For weights tarined for 1000 iterations
"""

!./darknet detector map data/obj.data cfg/yolov4-obj.cfg /mydrive/cmpe258/backup/yolov4-obj_1000.weights

"""For weights tarined for 2000 iterations"""

!./darknet detector map data/obj.data cfg/yolov4-obj.cfg /mydrive/cmpe258/backup/yolov4-obj_2000.weights

"""Calculating mAP for the best weights accumalated """

!./darknet detector map data/obj.data cfg/yolov4-obj.cfg /mydrive/cmpe258/backup/yolov4-obj_best.weights

"""Calculating mAP for the last weights accumalated """

!./darknet detector map data/obj.data cfg/yolov4-obj.cfg /mydrive/cmpe258/backup/yolov4-obj_last.weights

"""**Running the model**

Changing the configuration file from training mode to testing mode
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd cfg
!sed -i 's/batch=64/batch=1/' yolov4-obj.cfg
!sed -i 's/subdivisions=16/subdivisions=1/' yolov4-obj.cfg
# %cd ..

"""Making predictions using the last weights accumalated"""

!./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/cmpe258/backup/yolov4-obj_last.weights /mydrive/cmpe258/images/test_image1.png -thresh 0.3
imShow('predictions.jpg')

"""Prediction on unseen data"""

!./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/cmpe258/backup/yolov4-obj_last.weights /mydrive/cmpe258/images/test_image2.png -thresh 0.3
imShow('predictions.jpg')

!./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/cmpe258/backup/yolov4-obj_last.weights /mydrive/cmpe258/images/test_image3.jpg -thresh 0.3
imShow('predictions.jpg')

!./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/cmpe258/backup/yolov4-obj_last.weights /mydrive/cmpe258/images/test_image5.jpg -thresh 0.3
imShow('predictions.jpg')

!./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/cmpe258/backup/yolov4-obj_last.weights /mydrive/cmpe258/images/test_image6.png -thresh 0.3
imShow('predictions.jpg')

!./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/cmpe258/backup/yolov4-obj_last.weights /mydrive/cmpe258/images/test_image7.png -thresh 0.3
imShow('predictions.jpg')

!./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/cmpe258/backup/yolov4-obj_last.weights /mydrive/cmpe258/images/PGC0037258.png -thresh 0.3
imShow('predictions.jpg')

