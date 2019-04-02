import sys
import sqlite3 as sql
import random, string
from os import system


class DB():

    def __init__(self, dbName):
        self.con = sql.connect(dbName)

        if self.con == None:
            raise Exception("Could not create/connect to database")

        self._addAllowedChars()

    def _getConnection(self):
        return self.con

    def closeConnection(self):
        self.con.close()

    def commit(self):
        self._getConnection().commit()

    def _getCursor(self):
        return self._getConnection().cursor()

    def dbExecuteMult(self, query):
        # unsafe
        cur = self._getCursor()
        cur.executescript(query)
        return cur.fetchall()

    def dbExecute(self, query):

        cur = self._getCursor()
        try:
            cur.execute(query)
        except Exception as e:
            return ["!"]

        return cur.fetchall()

    def dbExecuteSafe(self, query):
        query = self._sanitize(query)
        self.dbExecute(query)

    def dbExecuteAndPrintSafe(self, query):
        query = self._sanitize(query)

        result = self.dbExecute(query)

        self._printResult(result)
            

    def dbExecuteAndPrint(self, query):
        self._printResult(self.dbExecute(query))

    def dbDropTable(self, tableName):
        tableName = self._sanitize(tableName)
        self.dbExecute(str.format("drop table if exists {}", tableName))
        self.commit()

    def getVersion(self):
        cur = self.getCursor()
        cur.execute('SELECT SQLITE_VERSION()')

        data = cur.fetchone()[0]

        print(str.format("SQLite version: {}", data))

    def _printResult(self, result):
        
        for row in result:
            finalStr = ""
            for elem in row:
                finalStr += str(elem) + ", "
            print(finalStr[:-2])

    def getTableNames(self, table):

        query = str.format("PRAGMA table_info({})", table)
        data = self.dbExecute(query)
        returnText = []

        for row in data:
            returnText.append(row[1])

        return returnText

    def _addAllowedChars(self):
        self.allowedChars = {}
        allowed = "abcdefghijklmnopqrstuvwxyzåäö0123456789 *!?-_&%$#@"
        for c in allowed:
            self.allowedChars[c] = True

    def _sanitize(self, query):

        self.sanitized = ""

        for c in query:
            if c.lower() in self.allowedChars:
                self.sanitized += c

        return self.sanitized
    

####################

    def genRandomUsers(self, n):

        fNames = ["Ella","Wilma","Ebba","Olivia","Astrid","Alma", "Elsa", "Alice", "Maja", 
        "Lilly","William","Liam","Noah","Lucas","Oliver","Oscar","Elias","Hugo","Adam","Alexander","Carl"]
        lNames = ["Smith","Jones","Taylor","Brown","Williams","Wilson","Johnson","Davies","Robinson",
        "Wright","Thompson","Evans","Walker","White","Roberts","Green","Hall","Jackson","Clarke","Flodin"]

        for i in range(n):

            #if i%10 == 0:
            #    system(str.format("title {:.3g}%",i/n*100))

            fName = random.choice(fNames)
            lName = random.choice(lNames)
            username = fName + self.id_generator(8, string.digits)
            password = self.id_generator(12)
            age = random.randint(18,60)

            self.register(username, password, fName, lName, age)
        
        self.commit()
            
    
    def id_generator(self, size=6, chars=string.ascii_letters + string.digits):
        
        return ''.join(random.choice(chars) for _ in range(size))


    def register(self, username, password, fName, lName, age):

        query = str.format("""
        insert into users (username, password, fName, lName, age) 
        values
        ('{0}', '{1}', '{2}', '{3}', {4})
        """, username, password, fName, lName, age)

        self.dbExecute(query)

    def login(self, username, password):

        query = str.format("""
        select * from users where username = '{0}' and password = {1}
        """, username, password)

        print(query)
        self.dbExecuteAndPrint(query)


    def createUserTable(self):
        query = """
            CREATE TABLE users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username varchar(16) unique,
            password varchar(16),
            fName varchar(8),
            lName varchar(12),
            age UNSIGNED TINYINT)"""

        self.dbDropTable('users')
        self.dbExecute(query)