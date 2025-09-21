#pickle setup

import pickle
with open('userSecurity','rb') as D:
    username = pickle.load(D)
    password = pickle.load(D)
userTrial = input('Please enter your username: ')
while userTrial.lower() != username:
    print('That username is incorrect please try again')
    userTrial = input('Please enter your username: ')
pwTrial = input('please enter your password: ')
while pwTrial != password:
    print('That password is incorrect please try again')
    pwTrial = input('Please enter your password: ')
print()
print('Welcome',username,"!")

#class setup

prices = []
categories = []
whatList = []
counter = 0
totalExpenses = 0.0
class expense:
    def __init__(self,price,category,what):
        self.price = price
        self.category = category
        self.what = what
    def log(self):
        prices.append(self.price)
        self.totalExpense = totalExpenses + self.price
        categories.append(self.category)
        whatList.append(self.what)
    def view(self):
        for i in whatList:
            print(i)


while 1 == 1:
    wish = input("What do you wish to do today? (log , view): ")
    if wish == "log":
        category = input("What type of expense do you have? (food, item, service, living): ")
        what = input("What did you buy? ")
        price = float(input("How much did your expense cost $"))
        expense1 = expense(price,category,what)
        expense1.log()
        counter = counter + 1
        print("Your expense has been logged!")
    if wish == "view":
        print("Your expenses are: ")
        expense.view(expense)



