## Code
This directory contains the code for the Convolution Neural Network (CNN) we designed and implemented by hand (using Tensorflow and Keras).The two main scripts in this directory define, train, and evaluate our CNN.

### convnet.py
This python script is where our CNN is implemented. The implementation includes building the structure of the CNN, reading in and preprocessing the training and testing data, as well as performing the training, testing, and evaluation of the model. There's one large advantage to the type of preprocessing we did on our data, and that's the fact that we end up with more, relatively unique datapoints, without having to really work for them. There is a drawback of this, however, in that since we are creating data from data we already have, we run a greater risk of overfitting our model. To combat this, we also added some dropout. There is also a function at the bottom that graphs the progression of the error over the training period. We also ended up setting the model up to work with tensorboard, so we were able to view the progress through that.

### train.py
This python script is responsible for a couple of orchestration things. The first is setting up the media path directories, so the model knows where to get the training and testing images from. The second thing is it counts the number of training and testing images, because the model uses these counts to determine the number of steps per epoch to take to use all the data. The third thing it does is instantiate and run the model and plot the results. This is the file to run when you want to run our CNN.

