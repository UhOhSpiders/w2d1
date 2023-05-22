# def get_account_name(account):
#     return account["holder_name"]


#THIS IS A CLASS. AN OBJECT WITH SET VARIABLES AND METHODS
class BankAccount:
    def __init__(self, holder_name, balance, account_type):
        self.holder_name = holder_name #THESE ARE ATRIBUTES OF THE CLASS
        self.balance = balance
        self.type = account_type
        self.rates = {"Personal" : 10,"Business" : 50}
    
    #THESE ARE METHODS BECAUSE THEY ARE ARE SPECIFIC TO THE CLASS
    def pay_in(self, amount):
        self.balance += amount

    def pay_monthy_fee(self):
            self.balance -= self.rates[self.type]
    
