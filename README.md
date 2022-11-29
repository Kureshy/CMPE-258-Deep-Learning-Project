# CMPE-258-Deep-Learning-Project
--------------------------
# Celestial Body detection using YOLOV4

This Repository contains the files for CMPE 258 class group project. 

## Team Members
| Name          | Student ID    |
| ------------- |---------------|
| Waqas Kureshy | 015421575   |
| Prabjyot Obhi | 012223861   | 


In this project we have used the Darknet YOLOv4 object detector on our custom dataset. The dataset is comprised of 3 classes.
- Stars
- Spiral Galaxies
- Elliptical Galaxies

Darknet has two key dependencies:
- OpenCV
- CUDNN

About the Dataset:
As mentioned before the dataset is based on 3 classes, the number of images for each class is described as below:

| Class |	Training Images	| Testing Images	| Total Images |
|------------|	--------------------|-------------------|---------------| 
|Stars	| 1412	|610	|2022|
|Spiral Galaxy	|2245	|300	|2545|
|Elliptical Galaxy|	2352|	300	|2652|


## Dataset:<br>
- The Star dataset can be obtained from [link](https://www.kaggle.com/datasets/divyansh22/dummy-astronomy-data/download?datasetVersionNumber=4). <br>

- For obtaining the galaxies do <br>
```
!pip install astroNN 
```
The Galaxies dataset can be obtained from running the Dataset script. After running the scrpt images of the galaxies would be automatically downloaded.

------------------

## Annotations:
A few annotations along with the dataset are provided in the Dataset folder. But one can easily annotate images using an online tool like [link](https://www.makesense.ai).

For the Purpose of training and testing a Jupyter notebook has been provided. This particular project was made using google colab and the notebook has step by step 
points laid out for the usage.

-------------------

## Project

-------------
**Note: The steps are provided as a generalization, if youre trying to perform the same task just upload the provided files in the folder stated below. The notebook is coded in such a way that it takes information from this folder.**
----------------

Create a folder in google drive named
```
cmpe258
```
<br>
In this particular folder add the following files:

```
generate_train.py
generate_test.py
```

These scripts are used for generating training and testing paths for the notebook.
 
 A **YOLO** configuration file has been provided, that contains the models configuration steps and it also needs to be in the same folder. This particular model's configuration file has been altered to work for three above mentioned classes only, for using the same configuration file edit out the classes fields in the configuration file using a **Editor** to the number of classes you want.
 
 Next zip up the files containing the dataset in individual files, it would be better if the training and testing files are named as
 ```
 obj.zip
 test.zip
 ```
 respectively, as the train and testing scripts have hardcoded coded for using these zipped files.
 
 Next, on a **TXT** file write down the name of the classes and name it as
 ```
 obj.names
 ```
 and upload it in the same folder.
 
 Next, create another **TXT** file and add the following details, the code below is an example and may differ if the same task is not carried out
 ```
classes=3
train=data/train.txt
valid=data/test.txt
names=data/obj.names
backup=/mydrive/cmpe258/backup/
 ```
 In the same folder create another folder called backup for saving the trained weights at regular iterations.
 
 Note:This model makes use of the users **Google Drive and the paths have to be in the same order for the model to work**
 
 If all steps have been performed carefully the notebook should run, smoothly.
 
 --------------------------
 
 ## Predictions
 
 For making predictions, create a folder called
 ```
 images
 ```
 in the same **cmpe258** folder and add pictures you want to test the model on.
 
 To run the model on your own images use the following command, be sure to insert your image name in the code as indicated in the < > brackets:
 
 ```
 !./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/cmpe258/backup/yolov4-obj_last.weights /mydrive/cmpe258/images/<your image name> -thresh 0.3
imShow('predictions.jpg')
 
 ```
 
 -----------------
 
 A sample output is shown as <br>
 
 ![result5](https://user-images.githubusercontent.com/78277453/204438523-8f755a17-7b89-4b12-8121-c0fa1ae968b4.png)

 



