## Code

This directory contains all of the code for the animal classification project. It has been split up into four main components:

1. Data gathering and preprocessing using an API.
2. Data gathering and preprocessing using a Kaggle data set.
3. Dog breed classification using custom built convolutional neural network.
4. Dog breed classification using pre built imageNet model.

Each of the dog breed classification steps has been ran on both the data sets so we have 4 different results for dog breed classification.

The two files `get_images_via_api.py` and `format_kaggle_data.py` in this directory are responsible for the data collection and processing for the api and kaggle data respectively. After each of these scripts is ran, the final directory structure should look as follows:

```
/media
	/Kaggle
		/Test/breeds...
		/Train/breeds...
	/API
		/Test/breeds...
		/Train/breeds...
```
`breeds...` in this case is a list of directories such that each directory corresponds to a single breed and contains all the images for that breed.


### get_images_via_api.py

This python script is responsible for number 1 as shown above. This python script hits `https://dog.ceo/api/breed/` which is an endpoint hosted by the `dog.ceo` website that simply returns a list of URLS that have images for a specific breed. For example, hitting `https://dog.ceo/api/breed/pug/images` will return roughly 230 links that point to images of pugs. These links point to a CDN which hosts the images, making the recovery significantly faster than if we had to hit their server. The script gets all the images for 11 different breeds and utilizes some python multithreading for faster download speeds. In order to properly sort the images, we have split up the directories so that 10% of the images go to the test directory and the remaining 90% go to the train directory. 


### format_kaggle_data.py

This python script is responsible for taking the downloaded kaggle data and processing it so it can be used by the CNN and pre built model. The interesting problem with the kaggle data is that unlike the API that returns a list of images for a specific breed, the kaggle data simply returns all of the images in one `train` directory and gives you a list of labels which classify the breeds of each image. Therefore, in order to preprocess these images we had to match each of the labels to an image and sort it into its correct breed directory. Similarly to the API, we decided that 10% of the images would be used for testing.