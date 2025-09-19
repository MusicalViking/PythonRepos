"""
Program Name : ch12exB
Program description : Cash register using a class function
Author: Arthur Belanger
Date created: 4-23-25
Notes: I followed you in class on this but do not get what you wanted us to turn in for values on the
transations or if you wanted them to be an input or not?
"""
import time

divider = ("_ _ _ ")
print(divider * 3)

class Register():
    def __init__(self):
        self._totalDue = 0

    def startTransaction(self):
        self._totalDue = 0

    def addItem(self, amount):
        self._totalDue += amount

    def getTotal(self):
        return self._totalDue

def main():
    myRegister = Register()
    myRegister.startTransaction()
    myRegister.addItem(10)
    myRegister.addItem(25)
    print(f'Total Amount Due: ${myRegister.getTotal():2.2f} ')
    myRegister.startTransaction()
    myRegister.addItem(17.50)
    myRegister.addItem(30)
    print(f'Total Amount due: ${myRegister.getTotal():2.2f}')

if __name__ == '__main__':
    main()




print(divider * 3)
print("Arthur Belanger")
print("CIS-110 - Program #ch12exB ")
print(time.ctime())
    
