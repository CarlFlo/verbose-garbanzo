from Database import DB
from os import system

system("cls")

db = DB("test.db")

createUserTable = """
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name varchar(8),
    deadliftMax int)
"""
getUsers = """
SELECT * FROM users
ORDER BY deadliftMax desc
"""

db.dbDropTable("users")
db.dbExecute(createUserTable)
db.dbExecute("insert into users (name,deadliftMax) values ('Carl', 210)")
db.dbExecute("insert into users (name,deadliftMax) values ('Carlos', 150)")
db.dbExecute("insert into users (name,deadliftMax) values ('Cortez', 100)")
db.dbExecute("insert into users (name,deadliftMax) values ('Charles', 145)")
db.dbExecute("insert into users (name,deadliftMax) values ('David', 473)")
db.dbExecute("insert into users (name,deadliftMax) values ('Sputnik', 125)")
db.dbExecute("insert into users (name,deadliftMax) values ('Al', 170)")
db.dbExecute("insert into users (name,deadliftMax) values ('Millan', 25)")
db.dbExecute("insert into users (name,deadliftMax) values ('Hafþór Júlíus Björnsson', 474)")

#db.dbExecuteAndPrint(getUsers)

#db.getUserByName("Carl' or 1=1 or '")

#db.login("Carl' or 1=1 or 'a'='a", "0")

#db.dbExecuteAndPrintSafe("select * from users order by name limit 5")

for i in range(10):
    print("Ha Ha")

#print(db._sanitize("!!''''' or #&/¤%&hej"))
