import secrets
import string


def password_generator(len):
    characters = (string.digits + string.ascii_letters + string.octdigits +
                 string.ascii_lowercase + string.ascii_uppercase + string.punctuation)

    password = [secrets.choice(characters)
           for i in range(len)]

    password = ''.join(password)

    return password
