import time

class BankAccount:
    def __init__(self, accountName : str, name : str, age : int) -> None:
        self._accountName = accountName
        self._name = name
        self._age = age
        self._currentMoney = 0.0
        self.createTime = time.time()
        self.creditScore = 0
        self.history = []
        self.countHistory = 1
        print(f"\nHello, {self._name}. You have made an account with the name \
\"{self._accountName}\". Welcome to the Money Bank, and thank you for choosing us!")
        
    def getAccountDetails(self) -> None:
        print(f"\nDetails for \"{self._accountName}\" are specified below:\n")
        print(f"Registered name: {self._name}")
        print(f"Registered age: {self._age}")
        print(f"Current money stored in bank: {self._currentMoney}")
        print(f"Current credit score: {self.creditScore}\n")

    def depositMoney(self, amount:float) -> None:
        print(f"You have chosen to deposit {amount} USD into this bank.\n\
Procedure is starting now.")
        self._currentMoney += round(amount,2)
        print(f"You now have {self._currentMoney} stored in this account.\n")
        self.creditScore += round(0.25*amount,2)
        mTime = time.strftime('%I:%M, %D')
        self.history.append(f'{self.countHistory}.\nDate: {mTime}\n\
Task: Deposited {amount} USD into this bank.\n')
        self.countHistory += 1

    def withdrawMoney(self, amount:float) -> None:
        if amount <= (self._currentMoney + self.creditScore):
            print(f"You have chosen to withdraw {amount} USD from this bank.\n\
    Procedure is starting now.")
            self._currentMoney -= round(amount,2)
            print(f"You now have {self._currentMoney} left in this account.\n")
            self.creditScore -= round(0.25*amount,2)
            if self.creditScore < 0: self.creditScore = 0
            mTime = time.strftime('%I:%M, %D')
            self.history.append(f'{self.countHistory}.\nDate: {mTime}\n\
Task: Withdrew {amount} USD from this bank.\n')
            self.countHistory += 1
        else:
            print("\nSorry, you do not have enough money to withdraw. Upgrade your credit\
score to increase the limit on your debt. You can achieve this by depositing more \
money into this bank. You can view your credit score in the Account Settings. You \
also lose credit score when you withdraw money from the bank.\n")

    def getHistory(self) -> None:
        if len(self.history) == 0:
            print("\nYou have no history with this account.\n")
        else:
            print('\n'.join(self.history))

def Main():
    def displayMenu():
        print("1. Show Account Details")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show Account History\n")
    accName = input("Hello, please provide an account name for your account: ")
    name = input("Now, input your legal name: ")
    age = int(input("Please input your legal age: "))
    obj = BankAccount(accName, name, age)
    displayMenu()
    choice = int(input("What choice would you like to do? "))
    while (choice >= 1) and (choice <= 4):
        if choice == 1:
            obj.getAccountDetails()
        elif choice == 2:
            amount = float(input("How much money do you want to deposit? "))
            obj.depositMoney(amount)
        elif choice == 3:
            amount = float(input("How much money do you want to withdraw? "))
            obj.withdrawMoney(amount)
        elif choice == 4:
            obj.getHistory()
        displayMenu()
        choice = int(input("What choice would you like to do? "))
        print('\n')

if __name__ == "__main__":
    Main()
