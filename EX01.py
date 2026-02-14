class BankAccount :
    def _init_(balance,name,secret)
        self.balance = balance
        self.name = name
        self.secret = secret
    def withdraw(self,balnace,name,secret);
        print(f"{name},balance is {balance},withdraw is{secret}")
    def deposite(self,balnace,name,secret);
        print(f"{name},balance is {balance},deposite is{secret}")

Nana = BankAccount("10000","Nana","1212")
Nana.withdraw("100","Nana","1212")
Nana.deposite("100","Nana","1212")


kana = BankAccount("20000","kana","1213")
kana.withdraw("100","kana","1213")
kana.deposite("100","kana","1213")
#print("Remaining balance is",Nana)