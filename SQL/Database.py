import sys
import sqlite3 as sql


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

    def _getCursor(self):
        return self._getConnection().cursor()

    def dbExecuteMult(self, query):
        # unsafe
        cur = self._getCursor()
        cur.executescript(query)
        return cur.fetchall()

    def dbExecute(self, query):

        cur = self._getCursor()
        cur.execute(query)
        return cur.fetchall()

    def dbExecuteSafe(self, query):
        query = self._sanitize(query)
        self.dbExecute(query)

    def dbExecuteAndPrintSafe(self,query):
        query = self._sanitize(query)
        self._printResult(self.dbExecute(query))

    def dbExecuteAndPrint(self, query):
        self._printResult(self.dbExecute(query))

    def dbDropTable(self, tableName):
        tableName = self._sanitize(tableName)
        self.dbExecute(str.format("drop table if exists {}", tableName))

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

    def login(self, username, password):

        query = str.format(
            "select * from users where name = '{0}' and deadliftMax = {1}", username, password)
        print(query)
        self.dbExecuteAndPrint(query)

