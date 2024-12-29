import random
import string


def generate_string(length):
    collection = string.ascii_uppercase + string.ascii_lowercase + string.digits
    random_characters = random.choices(collection, k=length)
    return "".join(random_characters)


print(generate_string(10))