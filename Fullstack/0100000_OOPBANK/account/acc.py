class Account:

    def __init__(self, filepath):
        #instance var
        self.filepath = filepath
        self.balance = 0
        try:
            with open(filepath ,'r') as file:
                self.balance = int(file.read())
        except:
            pass

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit(self):
        try:
            with open(self.filepath ,'w') as file:
                file.write(str(self.balance))
        except:
            print('Changes not commited') 


class Checking(Account):  #name of the mother class
    """Generates checking of the object"""

    type ="checking" #class variable shared by all the instances outside ot the methods

    def __init__(self , filepath , fee):
        Account.__init__(self,filepath)
        self.fee = fee #.instance variable from parameter
    
    def transfer(self, amount ):
        self.balance = self.balance -amount - self.fee


#0100000_OOPBANK
account = Account("account/balance.txt")
#account.withdraw(100)
print(account.balance)
account.commit()

# checking = Checking("account/balance.txt", 100)
# checking.deposit(10)
# checking.transfer(29)
# print(checking.balance)


yann_checking = Checking("account/yann.txt", 198)
yann_checking.deposit(102000)
yann_checking.transfer(29)
print(yann_checking.balance)
print(yann_checking.type)
yann_checking.commit()


yannpro_checking = Checking("account/yannpro.txt", 299)
yannpro_checking.deposit(1200)
yannpro_checking.transfer(29)
print(yannpro_checking.balance)
print(yannpro_checking.type)
yannpro_checking.commit()

print(yannpro_checking.__doc__)