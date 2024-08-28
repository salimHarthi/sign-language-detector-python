# sign-language-detector-python

Sign language detector with Python, OpenCV and Mediapipe !

[![Watch the video](https://img.youtube.com/vi/MJCSjXepaAM/0.jpg)](https://www.youtube.com/watch?v=MJCSjXepaAM)

# Train your own

## collect data

To start collecting data run
`python collect_imgs.py`
when you run the above command you can press R to start collecting data a class name will show starting from 0 to any number you want each move is one class dont mix more than one move in a class

## Name your classes

In the text file classes.txt each line is a class so class 0 in the collect data set step will be the first line and so on

## Create dataset

run
`python create_dataset.py`

## Train your model

run
`python train_classifier`

# Run the app

run
`streamlit run app.py`
