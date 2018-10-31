import requests
import json
import threading
from math import ceil, floor

DOG_API_ENDPOINT = 'https://dog.ceo/api/breeds/image/random'
CAT_API_ENDPOINT = 'https://api.thecatapi.com/v1/images/search'
MEDIA_PATH = '../media'
JSON_KEY_FILE = './keys.json'
NUMBER_OF_THREADS = 10
NUMBER_OF_IMAGES = 20

CAT_API_KEY = ''

cat_query_string = {"format":"json"}


# Retrieves specified key from the key json file
# Parameters:
#       title:  the title of the key to retrieve
#
def get_key(title):
    with open(JSON_KEY_FILE) as key_file:
        keys = json.load(key_file)

    return keys[title]

# Retrieves and saves n random images of cats
# Parameters:
#       n (int):  Number of cat images to retrieve and save
#       names (list): list of numbers to append to names of images
#
def get_cat_images(n, names):

    headers = {
        'Content-Type': "application/json",
        'x-api-key': get_key('cat_api_key')
    }

    for i in range(n):

        # Make request to api and parse out url of returned cat image
        response = requests.get(CAT_API_ENDPOINT, headers=headers, params=cat_query_string)
        cat_image_url = response.json()[0]['url']

        # Retrieve cat image and write to file
        r = requests.get(cat_image_url)
        with open(MEDIA_PATH + '/cats/cat' + str(names[i]) + '.' + cat_image_url.split('.')[-1], 'wb') as out_file:
            out_file.write(r.content)

# Retrieves and saves n random images of dogs
# Parameters:
#       n (int):  Number of dog images to retrieve and save
#       names (list): list of numbers to append to names of images
#
def get_dog_images(n, names):

    for i in range(n):

        # Make request to dog api and parse out url of returned dog image
        r = requests.get(DOG_API_ENDPOINT)
        dog_image_url = r.json()['message']

        # Retrieve dog image and write to file
        r = requests.get(dog_image_url)
        with open(MEDIA_PATH + '/dogs/dog' + str(names[i]) + '.' + dog_image_url.split('.')[-1], 'wb') as out_file:
            out_file.write(r.content)


# Parameters:
#       n (int): total number of images to get, evently distributed about each datasource
#
def get_images(n):

    chunks = get_image_chunks(n, NUMBER_OF_THREADS)

    threads = []
    for i in range(int(NUMBER_OF_THREADS / 2)):
        t = threading.Thread(target=get_dog_images, args=(len(chunks[i]), chunks[i],))
        threads.append(t)
        t.start()

    for i in range(int(NUMBER_OF_THREADS / 2), NUMBER_OF_THREADS):
        t = threading.Thread(target=get_cat_images, args=(len(chunks[i]), chunks[i],))
        threads.append(t)
        t.start()


'''
    Example: 23 images in 10 threads. Chunks:
    3,3,3,2,2,2,2,2,2,2 - large chunks are first (3), small chunks second.
    size of large chunk is 3
    size of small chunk is 2
    number of large chunks is also 3 (there are 3 3's)
    number of small chunks is 7
'''
def get_image_chunks(number_of_images, number_of_chunks):
    
    images = [x for x in range(1, number_of_images + 1)]

    size_of_chunks = number_of_images / number_of_chunks

    size_of_large_chunks = ceil(size_of_chunks)
    number_of_large_chunks = int((size_of_chunks - int(size_of_chunks)) * number_of_chunks)

    size_of_small_chunks = size_of_large_chunks - 1 if number_of_large_chunks > 0 else size_of_large_chunks
    number_of_small_chunks = int(number_of_chunks - number_of_large_chunks)
    
    large_chunks = [images[i:i+size_of_large_chunks] for i in range(0, (number_of_large_chunks * size_of_large_chunks), size_of_large_chunks)]
    small_chunks = [images[i:i+size_of_small_chunks] for i in range(number_of_large_chunks * size_of_large_chunks, len(images), size_of_small_chunks)]

    large_chunks.extend(small_chunks)

    return large_chunks
    





if __name__ == "__main__":
    #get_cat_images(1)
    #get_dog_images(1)
    get_images(NUMBER_OF_IMAGES)
