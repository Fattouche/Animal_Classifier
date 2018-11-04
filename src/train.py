from convnet import *
import os

MEDIA_PATH = '../media/'
TEST_PATH = os.path.join(MEDIA_PATH, 'test')
TRAINING_PATH = os.path.join(MEDIA_PATH, 'train')
NUMBER_OF_THREADS = 10
BREED_LIST = ['hound', 'retriever', 'poodle', 'husky',
              'bulldog', 'mastiff', 'pug', 'rottweiler', 'shihtzu', 'samoyed', 'greyhound']

# Count the number of testing and training images
# Returns a tuple (test_count, train_count)
def count_images():
    test_count = sum([len(files)
                      for r, d, files in os.walk(MEDIA_PATH+'test/')])
    train_count = sum([len(files)
                       for r, d, files in os.walk(MEDIA_PATH+'train/')])
    return test_count, train_count



if __name__ == '__main__':
    training_image_count, test_image_count = count_images()
    history = convnet(TRAINING_PATH, TEST_PATH, training_image_count, test_image_count)
    results(history)