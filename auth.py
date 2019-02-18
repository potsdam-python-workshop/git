import getpass
import pickle
import random
import string

CHARS = string.ascii_letters + string.digits + string.punctuation

def pwhash(password):

    # hash the password
    hashedpw = 0
    for char in password:
        hashedpw += ord(char)
    return hashedpw

def get_salt():
    salt_chars = random.choices(CHARS, k=10)
    salt =  ''.join(salt_chars)
    return salt

def get_credentials():

    username = input("Enter username:")
    password = getpass.getpass("Enter password:")

    return (username, password)

def authenticate(username, password, pwdb, sadb):
    status = False
    if username in pwdb:

        if pwhash(password + sadb[username]) == pwdb[username]:
            status = True
        else:
            print('Wrong password!')
    else:
        add_user(username, password, pwdb, sadb)

    return status

def add_user(username, password, pwdb, sadb):

    sadb[username] = get_salt();
    pwdb[username] = pwhash(password + sadb[username]);

    write_pwdb(pwdb)
    write_sadb(sadb)

def read_pwdb():
    try:
        with open("pwdb.pkl", "rb") as fh:
            pwdb = pickle.load(fh)
    except FileNotFoundError:
        pwdb = {}

    return pwdb

def read_sadb():
    try:
        with open("sadb.pkl", "rb") as fh:
            sadb = pickle.load(fh)
    except FileNotFoundError:
        sadb = {}

    return sadb

def write_pwdb(pwdb):
    with open("pwdb.pkl", "wb") as fh:
        pickle.dump(pwdb, fh)

def write_sadb(sadb):
    with open("sadb.pkl", "wb") as fh:
        pickle.dump(sadb, fh)

if __name__ == "__main__":

    username, password = get_credentials()

    pwdb = read_pwdb()
    sadb = read_sadb()

    status = authenticate(username, password, pwdb, sadb)

    if status:
        print('Authentication succeeded:')
    else:
        print('Authentication failed')

