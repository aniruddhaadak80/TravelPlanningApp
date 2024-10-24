from sqlitedict import SqliteDict

# Save data using a key
def save(key, value, cache_file="data.sqlite3"):
    try:
        with SqliteDict(cache_file) as mydict:
            mydict[key] = value # Using dict[key] to store
            mydict.commit() # Need to commit() to actually flush the data
    except Exception as ex:
        print("Error during storing data (Possibly unsupported):", ex)

# Returns the stored data using the key
def load(key, cache_file="data.sqlite3"):
    try:
        with SqliteDict(cache_file) as mydict:
            value = mydict[key] # No need to use commit(), since we are only loading data!
        return value
    except Exception as ex:
        print("Error during loading data:", ex)

# This class stores the user data
class UserData:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        save(userName, self)
