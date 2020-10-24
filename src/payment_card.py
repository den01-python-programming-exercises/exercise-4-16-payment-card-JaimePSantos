class PaymentCard:
    def __init__(self, opening_balance):
        # write code here
        self.balance = opening_balance

    def __str__(self):
        # write code here
        return "The card has a balance of %s pounds"%self.balance
    
    def eat_affordably(self):
      if(self.balance >= 2.60):
        self.balance-=2.60
      return self.balance
    # write code here

    def eat_heartily(self):
      if(self.balance >= 4.60):
        self.balance-=4.60
      return self.balance
    # write code here

    def add_money(self,amount):
      if(amount>0):
        if(self.balance+amount<=150.0):
          self.balance+=amount
        else:
          self.balance=150.0
  
      return self.balance
    # write code here

