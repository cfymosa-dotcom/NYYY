class BankAccount:
    def init(self, balance, name, secret):
        self.__balance = balance
        self.name = name
        self.__secret = secret
    
    def withdraw(self, amount, secret):
        print(f"Withdrawing {amount} from {self.name}'s account.")
        if secret == self.__secret:

            remain = self.__balance - amount
            if remain < 0:
                print("Insufficient funds. Current balance")
            else:
                self.__balance = remain
                print("Withdrawal successful.")
                print(f"Remaining balance: {self.__balance}")
        else:
            print("invalid secret code. Please try again.")
    
    def check_balance(self, secret):
        if secret == self.__secret:
            print(f"{self.name}'s balance: {self.__balance}")
        else:
            print("Invalid secret code. Please try again.")
    
    def deposit(self, amount, secret):
        print(f"Depositing {amount} to {self.name}'s account.")
        if secret == self.__secret:
            self.__balance += amount
            print("Deposit successful.")
            print(f"New balance: {self.__balance}")
        else:
            print("Invalid secret code. Please try again.")
    
    def payment(self, service_type, amount, secret):
        print(f"Processing payment for {service_type} from {self.name}'s account.")
        if secret == self.__secret:
            remain = self.__balance - amount
            if remain < 0:
                print("Insufficient funds. Payment failed.")
            else:
                self.__balance = remain
                print("Payment successful.")
                print(f"Remaining balance: {self.__balance}")
        else:
            print("Invalid secret code. Please try again.")
    
    def transfer(self, to_account, amount, secret):
        print(f"Transferring {amount} from {self.name} to {to_account.name}.")
        if secret == self.__secret:
            if self.__balance < amount:
                print("Insufficient funds. Transfer failed.")
            else:
                self.__balance -= amount
                to_account.__balance += amount
                print("Transfer successful.")
                print(f"{self.name}'s new balance: {self.__balance}")
                print(f"{to_account.name}'s new balance: {to_account.__balance}")
        else:
            print("Invalid secret code. Please try again.")


dara = BankAccount(balance=20000, name="dara", secret="98765")
visal = BankAccount(balance=5000, name="visal", secret="1234")

accounts = {"dara": dara, "visal": visal}

def display_menu():
    print("\n=== Bank Account Menu ===")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Payment")
    print("5. Transfer")
    print("6. Exit")
    print("========================\n")