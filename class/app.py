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

hello = "string"

# here we are assigning "johns_account" with a custom class 
# of BankAccount. BankAccount is a custom object which takes
# 3 arguments
johns_account = BankAccount("John", 500, "Business")
pauls_account = BankAccount("Pauls", 1000000, "Personal")
randolph_account = BankAccount("Randolph", 0, "Business")

print(johns_account.holder_name)
print(randolph_account.type)

johns_account.pay_monthy_fee()
pauls_account.pay_monthy_fee()
print(johns_account.balance)
print(pauls_account.balance)