# Create a simple authentication system
*an alternative to the hopelessly boring `hello world` examples for an introduction to git*

Start creating a script called `auth.py`

### Expected usage:
  - run the script
  - the script asks for username and password
  - if the user is known and password is correct: print the password database
  - if the user is not known, ask to add it to the password database
  - if a user has been added, store the updated database to disk

### Basic API:
  - a function `get_credentials` that asks for username and password
  - a function `authenticate` that checks if user is in the password database and that the password is correct
  - a function `add_user` to add a new user with its password to the database
  - a function `read_pwdb` to read the password database from disk
  - a function `write_pwdb` to write the password database to disk

Suggestions:
  - the database can be a simple dictionary `{username: password}`
  - the database can be serialized to disk with [`pickle`](https://docs.python.org/3/library/pickle.html)
  - to experiment you can store the database on a temporary directory
  - remember to write the database to disk every time you add a new user


### Later, think about the following problems:
  - should we return different errors if username is not known or password is wrong? ⟶ do not leak valid usernames
  - [password *hashing*](https://en.wikipedia.org/wiki/Cryptographic_hash_function) ⟶ do not store passwords in clear text (database could be stolen, admins are nosy), do not store passwords at all but only its hash (database could be stolen)
  - [password *salting*](https://en.wikipedia.org/wiki/Salt_&#40;cryptography&#41;) ⟶ different users with same passwords should not have same hash ⟶ cracking one does not crack all: mitigates dictionary attacks, see below)

Addition to the basic API:
  - a function `pwhash` that given a password and a salt returns a hash
  - a function `get_salt` that returns a unique salt

### Try to crack it! (Advanced)
  - can you guess the [*hash collision*](https://en.wikipedia.org/wiki/Collision_attack) risk for the proposed solution?
  - try first a [*brute force*](https://en.wikipedia.org/wiki/Brute-force_attack) attack: is it feasible?
  - try a [*dictionary*](https://en.wikipedia.org/wiki/Dictionary_attack) attack (you can use this list of [probable passwords](https://github.com/danielmiessler/SecLists/tree/master/Passwords)): is it feasible?
  - think about [*lookup tables*](https://en.wikipedia.org/wiki/Lookup_table) and [*rainbow tables*](https://en.wikipedia.org/wiki/Rainbow_table) attacks
  - what are the trade-offs of the different attacks?

### Notes 
To make it for real:
  - insecure temporary file ([symlink race](https://en.wikipedia.org/wiki/Symlink_race) attack) ⟶ [`tempfile`](https://docs.python.org/3/library/tempfile.html) and its context managers
  - better way of generating passwords or random tokens: the [`secrets`](https://docs.python.org/3/library/secrets.html) module
  - cracking a password database is a form of art, see for example the [John the Ripper](http://www.openwall.com/john/) password cracker

### Installing Git GUI

If you encounter something like `git gui is not a git command` then probably Git GUI isn't installed yet. You can add it to your Git installation in the following ways:

#### macOS
```
# If this command outputs something with "AppleGit" you have a slimmed down version of Git
git --version
# In that case, continue with the following commands

# 1. Download the official installer from https://git-scm.com/download/mac and install it
...

# 2. Create an alias in .bash_profile
# Add a line "alias git='/usr/local/git/bin/git'" (without the ""), then save and exit
nano ~/.bash_profile

# 3. Activate the current configuration
source ~/.bash_profile

# 4. Test the change
git gui
```

#### Ubuntu
```
# Use the following command to add Git GUI to your installation
sudo apt install git-gui

# If you do a fresh Git install, you could also use this command to get everything at once
sudo apt install git-all
```
