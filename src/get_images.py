import requests
import json
import threading
import os
from math import ceil, floor

DOG_API_ENDPOINT = 'https://dog.ceo/api/breed/'
DOG_API_EXTENSTION = '/images'
MEDIA_PATH = '../media/'
NUMBER_OF_THREADS = 10
BREED_LIST = ['hound', 'retriever', 'poodle', 'husky',
              'bulldog', 'mastiff', 'pug', 'rottweiler', 'shihtzu', 'samoyed', 'greyhound']

# Retrieves and saves n random images of dogs
# Parameters:
#       n (int):  Number of dog images to retrieve and save
#       names (list): list of numbers to append to names of images


def get_image_urls():
    breed_dict = {}
    for breed in BREED_LIST:
        # Make request to dog api and parse out url of returned dog image
        r = requests.get(DOG_API_ENDPOINT+breed+DOG_API_EXTENSTION)
        dog_image_urls = r.json()['message']
        breed_dict[breed] = dog_image_urls
    return breed_dict


def get_dog_images(breed, dog_image_urls):
    directory_path = MEDIA_PATH+breed
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # This number can be changed to grab more or less images
    for dog_image_url in dog_image_urls[:10]:
        filename = "{0}/{1}/{2}".format(MEDIA_PATH,
                                        breed, dog_image_url.split("/")[-1])
        if os.path.isfile(filename):
            continue
        # Retrieve dog image and write to file
        r = requests.get(dog_image_url)
        with open(filename, 'wb') as out_file:
            out_file.write(r.content)


# Parameters:
#       n (int): total number of images to get, evently distributed about each datasource
#
def get_images():

    image_url_dict = get_image_urls()
    threads = []

    # Spin up a seperate thread to retrieve images for each different breed
    for breed, breed_urls in image_url_dict.items():
        t = threading.Thread(target=get_dog_images, args=(breed, breed_urls,))
        threads.append(t)
        t.start()


if __name__ == "__main__":
    get_images()
