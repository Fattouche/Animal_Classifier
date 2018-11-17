import os
import sys
import pandas as pd
'''
1. You should download all of the kaggle set at https://www.kaggle.com/c/dog-breed-identification/data
2. Extract the all.zip file and put it into media/Kaggle directory(you will need to make it)
3. Extract the train.zip into a directory called media/Kaggle/train_raw

Before you run this program, the folder structure should look like this:

/media
    /kaggle
        /train_raw
            image_1.png
            image_2.png
            ...

After running the program you should have

/media
    /kaggle
        /train
            /breed1
            /breed2
            /breed3
            ...
        /test
            /breed1
            /breed2
            /breed3
            ...

Once you have the training and test data formatted as shown, you can delete all csv files, any zip files and the train_raw directory. 
The only thing you should have leftover is the train and test directory.
'''

root = "../media/kaggle/"
training_data = root+"train_raw/train/"
train_path = "train"
test_path = "test"


def organize_images():
    os.makedirs(root, exist_ok=True)
    label_data = pd.read_csv(root+'labels.csv')
    files = os.listdir(training_data)
    test_number = len(files)*0.1
    for index, file in enumerate(files):
        folder_name = label_data.loc[label_data['id']
                                     == file.split('.')[0], 'breed'].values[0]
        source = training_data+file

        if(index < test_number):
            path = test_path
        else:
            path = train_path

        os.makedirs(root+path+'/'+folder_name, exist_ok=True)
        destination = root+path+'/'+folder_name+'/'+file
        os.rename(source, destination)


def main():
    organize_images()


if __name__ == '__main__':
    main()
