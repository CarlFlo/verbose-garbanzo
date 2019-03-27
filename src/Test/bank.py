from os import system
from decimal import Decimal


class Bank:

    _accounts = {}

    def addAccount(self, username, password, fname, lname, money):
        acc = Account(username, password, fname, lname, money)
        self._accounts[username] = acc

    def getAccount(self, username):
        return self._accounts[username]


class Account:

    def __init__(self, username, password, fname, lname, money):

        if(money < 0):
            raise ValueError('Money is less than 0', money)

        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.money = Decimal(money)

    def getMoney(self):
        return self.money


bank = Bank()
bank.addAccount("cafl", "pass", "Carl", "Flodin", -552.3043824)

myAcc = bank.getAccount("cafl")
print(myAcc.fname, myAcc.getMoney())
