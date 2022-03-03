class AtmBank(object):
    def __init__(self,color,shape,holders,rupees):
        self.color = color
        self.rupees = rupees
        self.shape = shape
        self.holders = holders

    def deposit(self,rupees):
        print("Today i am going to deposit ",rupees," rupees in the Bank")
    def credit(self,rupees):
        print("Today i am going to credit ",rupees," rupees from the Bank")    

diary1 = AtmBank("red",'200',"rectangle",'7')    

diary1.deposit('5000')
diary1.credit('2500')      