from Database import DB
from os import system
import time, string

system("cls")

def main():

    db = DB("test.db")

    #db.genRandomUsers(200)
    
    result = db.dbExecute("select count(*) from users")
    print("Total entries:", result[0][0], end="")

    db.dbCloseConnection()

if __name__ == "__main__":
    main()

