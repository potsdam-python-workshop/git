import getpass
import pickle
import random


def get_credentials():
    username = input("Enter username:")
    password = getpass.getpass("Enter password:")
    return (username, password)

def authenticate(username, password, pwdb):
    status = False
    if username in pwdb:
        if pwhash(password,pwdb[username][1]) == pwdb[username][0]:
            status = True
        else:
            print('Wrong password!')
    else:
        add_user(username, password, pwdb)

    return status

def get_salt():
    salt=""
    for x in range(1, 10):
        salt += chr(random.randint(0,1114111))
    return salt

def add_user(username, password, pwdb):
    salt=get_salt()
    hashed=pwhash(password,salt)
    pwdb[username] = (hashed,salt)
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

def pwhash(password, salt):
    hashedpw=0
    password.join(salt)
    for char in password:
        hashedpw += ord(char)
    return hashedpw
        


if __name__ == "__main__":
    random.seed()
    username, password = get_credentials()
    pwdb = read_pwdb()
    status = authenticate(username, password, pwdb)
    if status:
        print('Authentication succeeded:', pwdb)
    else:
        print('Authentication failed')
