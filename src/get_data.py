import requests
import json

DOG_API_ENDPOINT = 'https://dog.ceo/api/breeds/image/random'
CAT_API_ENDPOINT = 'https://api.thecatapi.com/v1/images/search'
MEDIA_PATH = '../media'
JSON_KEY_FILE = './keys.json'

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
#
def get_cat_images(n):

    headers = {
        'Content-Type': "application/json",
        'x-api-key': get_key('cat_api_key')
    }

    for i in range(1, n + 1):

        # Make request to api and parse out url of returned cat image
        response = requests.get(CAT_API_ENDPOINT, headers=headers, params=cat_query_string)
        cat_image_url = response.json()[0]['url']

        # Retrieve cat image and write to file
        r = requests.get(cat_image_url)
        with open(MEDIA_PATH + '/cats/cat' + str(i) + '.' + cat_image_url.split('.')[-1], 'wb') as out_file:
            out_file.write(r.content)

# Retrieves and saves n random images of dogs
# Parameters:
#       n (int):  Number of dog images to retrieve and save
#
def get_dog_images(n):

    for i in range(1, n + 1):

        # Make request to dog api and parse out url of returned dog image
        r = requests.get(DOG_API_ENDPOINT)
        dog_image_url = r.json()['message']

        # Retrieve dog image and write to file
        r = requests.get(dog_image_url)
        with open(MEDIA_PATH + '/dogs/dog' + str(i) + '.' + dog_image_url.split('.')[-1], 'wb') as out_file:
            out_file.write(r.content)


if __name__ == "__main__":
    get_cat_images(1)
    get_dog_images(1)
