import getpass
import pickle
import random

def get_salt():
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k = 10))

def pwhash(password, salt):
    hashedpw = 0
    for char in password:
        hashedpw += ord(char)
    for char in salt:
        hashedpw += ord(char)
    return hashedpw

def get_credentials():
    username = input("Enter username:")
    password = getpass.getpass("Enter password:")
    return (username, password)

def authenticate(username, password, pwdb):
    status = False
    if username in pwdb:
        if pwhash(password, pwdb[username][1]) == pwdb[username][0]:
            status = True
        else:
            print('Wrong password!')
    else:
        add_user(username, password, pwdb)

    return status

def add_user(username, password, pwdb):
    salt = get_salt()
    pwdb[username] = (pwhash(password, salt), salt)
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
