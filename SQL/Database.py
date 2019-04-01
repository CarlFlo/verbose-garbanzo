import sqlite3 as sql


class DB():

    def __init__(self, dbName):
        self.con = sql.connect(dbName)

        if self.con == None:
            raise Exception("Could not create/connect to database")

    def getConnection(self):
        return self.con

    def closeConnection(self):
        self.con.close()

    def getCursor(self):
        return self.getConnection().cursor()

    def dbExecute(self, query):
        cur = self.getCursor()
        cur.execute(query)
        return cur.fetchall()

    def dbExecuteAndPrint(self, query):
        self._printResult(self.dbExecute(query))

    def dbDropTable(self, tableName):
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
