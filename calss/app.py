from modules.bank_account import *

# l = []

# l.append(1)
# #tye .append is a "method". a special FUNCTION for the LIST CLASS
# #CLASSES have different METHODS for doing different useful things
# print(l)

# str = "Hello, Jen!"

# print(str.lower())

account = {
    "holder_name" : "John",
    "balance" : "500",
    "type" : "Business",
}

# print(get_account_name(account))

johns_account = BankAccount("John", 500, "Business")
randolph_account = BankAccount("Randolph", 0, "Business")

# print(johns_account.balance)
# print(randolph_account.type)