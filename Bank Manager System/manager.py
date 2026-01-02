from account import Account, Saving, Current
from datastore import Datastore 

class Manager:
    
    acc_counter = 1000   

    def __init__(self):
        self.ds = Datastore() 
        
    def generateAccNo(self):
        Manager.acc_counter += 1
        return Manager.acc_counter
    
    def createAcc(self):
        name = input("Enter NAME: ")
        balance = int(input("Enter Deposit Minimum 1000: "))
        status = input("Enter Status (active/inactive): ").lower()

        if balance < 1000:
            print("Minimum deposit must be 1000")
            return

        if status not in ("active", "inactive"):
            print("Invalid status")
            return
        
        acc_no = self.generateAccNo()

        acc_type = input("Enter Account Type (saving/current): ").lower()

        if acc_type == "saving":
            acc = Saving(name, acc_no, balance, status)
        else:
            acc = Current(name, acc_no, balance, status)
        
        self.ds.addData(acc)
        self.ds.addReport(f'Account {acc_no} created with balance {balance}')
        
        print("Account Created Successfully!!!!!!!!!")
        
        
    def checkBal(self):
        acc_no = int(input("Enter ACCOUNT No: "))
        acc = self.ds.getData(acc_no)
        
        if acc is None:
            print("Account Not Found")
            return 
        
        if acc.status != "active":
            print("Account is INACTIVE")
            return
        
        print(f'Current Balance: {acc.balance}')
        
    def withdrawMoney(self):
        acc_no = int(input("Enter ACCOUNT No: "))
        acc = self.ds.getData(acc_no)

        if acc is None:
            print("Account Not Found")
            return 
        
        if acc.status != "active":
            print("Account is INACTIVE")
            return
        
        amount = int(input("Enter Amount To Withdraw: "))
        
        if acc.balance - amount >= 1000:
            acc.balance -= amount
            self.ds.addReport(f'{amount} withdrawn from account {acc_no}')
            print(f"Withdraw Successful. Current Balance: {acc.balance}")
        else:
            print("Insufficient Balance (Min balance 1000 required)")
            
            
    def depositeMoney(self):
        acc_no = int(input("Enter ACCOUNT No: "))
        acc = self.ds.getData(acc_no)
        
        if acc is None:
            print("Account Not Found!")
            return 
        
        if acc.status != "active":
            print("Account is INACTIVE")
            return
        
        amount = int(input("Enter Amount You Want To Deposit: "))
        acc.balance += amount 
        
        self.ds.addReport(f'{amount} deposited in {acc_no}')
        print(f'Deposit Successful! Balance: {acc.balance}')
        
    def endDayReport(self):
        print("----- END DAY REPORT -----")
        for msg in self.ds.getReport():
            print("-", msg)
    
    def managerMenu(self):
        while True:
            print(f'\nChoose Your Task')
            print("1.CREATE AN ACCOUNT")
            print("2.CHECK BALANCE")
            print("3.WITHDRAW MONEY")
            print("4.DEPOSIT MONEY")
            print("5.END DAY REPORT")
            print("6.EXIT")
            
            ch = input("Enter Your Choice: ")
            
            if ch == '1':
                self.createAcc()
            elif ch == '2':
                self.checkBal()
            elif ch == '3':
                self.withdrawMoney()
            elif ch == '4':
                self.depositeMoney()
            elif ch == '5':
                self.endDayReport()
            elif ch == '6':
                print("Exiting Manager Menu")
                break
            else:
                print("Invalid Choice")
