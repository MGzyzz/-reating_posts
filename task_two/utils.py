import random


def id_generator():
    count = 0
    while True:
        count += 1
        yield count


def random_image():
    images = ['/pexels-helena-lopes-1862000.jpg', '/pexels-kevin-villaruz-1660603.jpg', '/pexels-marcus-herzberg-1473673.jpg', '/pexels-umar-mukhtar-1538177.jpg']
    random.shuffle(images)
    while True:
        for image in images:
            yield image


random_img = random_image()

id_gen = id_generator()
