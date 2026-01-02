class Datastore:
    
    def __init__(self):
        self.acc_data = {}
        self.report = []
        
    def addData(self, account):
        self.acc_data[account.acc_no] = account
        
    def getData(self, acc_no):
        if acc_no in self.acc_data: 
            return self.acc_data.get(acc_no)
        else:
            return None
    
    def addReport(self, message):
        self.report.append(message)
        
    def getReport(self):
        return self.report
