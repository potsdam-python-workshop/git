import getpass
import pickle
import hashlib
import random
import string

CHARS = string.ascii_letters + string.digits + string.punctuation

def pwhash(password, salt):
    m = hashlib.sha512()
    m.update(salt.encode('utf-8'))
    m.update(password.encode('utf-8'))
    return m.digest()

def create_salt():
    salt_chars = random.choices(CHARS, k=10)
    salt = ''.join(salt_chars)
    return salt

def get_credentials():
    username = input("Enter username:")
    password = getpass.getpass("Enter password:")
    return (username, password)

def authenticate(username, password, pwdb):
    status = False
    if username in pwdb:
        # get hashed password and salt
        hashed_password = pwdb[username]['password']
        user_salt = pwdb[username]['salt']
        # check given password with expected value
        if hashed_password == pwhash(password, user_salt):
            status = True
        else:
            print('Wrong password!')
    else:
        add_user(username, password, pwdb)

    return status

def add_user(username, password, pwdb):
    user_salt = create_salt();
    hashed_password = pwhash(password, user_salt)
    
    pwdb[username] = {
            'salt': user_salt,
            'password': hashed_password,
            }
    write_pwdb(pwdb)

def read_pwdb():
    try:
        with open("pwdb.pkl", "rb") as fh:
            pwdb = pickle.load(fh)
    except FileNotFoundError:
        pwdb = {}

    return pwdb

def write_pwdb(pwdb):
    with open("pwdb.pkl", "wb") as fh:
        pickle.dump(pwdb, fh)


if __name__ == "__main__":
    username, password = get_credentials()
    pwdb = read_pwdb()
    status = authenticate(username, password, pwdb)
    if status:
        print('Authentication succeeded:', pwdb)
    else:
        print('Authentication failed')
