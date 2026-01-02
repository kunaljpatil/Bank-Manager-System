# We ARE BUILDING BANK MANAGER SYSTEM 
#1 ACCOUNT
#   i SAVING ACCOUNT
#   ii CURRENT ACCOUNT

class Account:
    
    def __init__(self, name, acc_no, balance, status):
        self.name = name 
        self.acc_no = acc_no 
        self.balance = balance
        self.status = status 
    
    def showData(self):
        return (
            f'NAME: {self.name}\n'
            f'ACC NO: {self.acc_no}\n'
            f'BALANCE: {self.balance}\n'
            f'STATUS: {self.status}'
        )


class Saving(Account):
    mini_bal = 1000

    def __init__(self, name, acc_no, balance, status):
        super().__init__(name, acc_no, balance, status)
        self.mini_bal = Saving.mini_bal


class Current(Account):

    def __init__(self, name, acc_no, balance, status):
        super().__init__(name, acc_no, balance, status)
