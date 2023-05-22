# def get_account_name(account):
#     return account["holder_name"]

class BankAccount:
    def __init__(self, holder_name, balance, account_type):
        self.holder_name = holder_name
        self.balance = balance
        self.type = account_type