class AtmBank(object):
    def __init__(self,accountname,cardnumber,balanceholders,rupees):
        self.accountname = accountname
        self.cardnumber = cardnumber
        self.balanceholders = balanceholders
        self.rupees = rupees

    def deposit(self,rupees):
        print("Today i am going to deposit ",rupees," rupees in the Bank")
    def credit(self,rupees):
        print("Today i am going to credit ",rupees," rupees from the Bank")    

atmbank1 = AtmBank("Kedar",'1357',"4",'50,000,000')    

atmbank1.deposit('5000')
atmbank1.credit('2500')      