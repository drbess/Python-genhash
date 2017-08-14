import hashlib
import uuid


def new_password(password):
    salt = uuid.uuid4().hex

    # The uuid generates a random number
    return hashlib.sha1(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(new_password, user_password):

    password, salt = new_password.split(':')
    return password == hashlib.sha1(salt.encode() + user_password.encode()).hexdigest()

new_pass = raw_input('Enter a string to be hashed: ')
new_password = new_password(new_pass)

# Try new_pass if all else fails
print('Your new password hashed: ' + new_password)


