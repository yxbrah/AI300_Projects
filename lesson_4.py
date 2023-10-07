class Stock:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def value(self):
        return self.price * self.quantity
    

class Portfolio:
    Portfolio_name='hihi' #try not to have this. always have self. cause if i modify this attribute using object. EVERYTHING CREATED FROM THIS WILL BE MODIFIED!!!!!!!!!!!!!!!!!!
    #this  is class attribute
    def __init__(self):#init=constrcutor method
        self.stocks = []
        #self refers to object, and not class.depdnign on what is being called.
        # if i call self on Jon_portfolio (object), i am referring to Jon_portfolio.
        # if i call self on Portfolio (class), i am referring to Portfolio.

    def add_stock(self, price, quantity):
        self.stocks.append(Stock(price, quantity))

    def total_value(self):
         #for stock in self.stocks:
            #stock_values=[]
            #stock_values.append(stock)
            #return sum(stock_values)
        return sum(stock.value() for stock in self.stocks)
    
print('hello world')


apple=Stock(170,10)
Jon_portfolio=Portfolio()
Jon_portfolio.add_stock(170,50)
print(f'Jon has $ {Jon_portfolio.total_value()}')


class BankAccount:
    bank_name = "Bank of Python"  # class attribute
    #init is constructor
    def __init__(self, account_holder_name, account_number, balance): #self->object attribute
			# instance attributes
        self.account_holder_name = account_holder_name  #on the right is passed in by function. #self-> somewhere in the memory, allocate space,create new account, put in a value.
        self.account_number = account_number
        self.balance = balance #use getter instead of attribute, may be reasons why method was implemented
    def welcome(self):
        print('welcome,',self.account_holder_name,'!')

    def check_balance(self): #getter method.
        return self.balance
    
    def deposit(self,figure):
        self.balance+=figure
    
    def withdraw(self,figure):
        if (figure>self.balance):
            print ("insufficient funds")
        else:
            self.balance-=figure



account_details=['Darren',1234567,1000]
darren_account=BankAccount(*account_details) #* means unpack the variable list into respective 3 arguments. cleaner.

print('darren has $ {}'.format(darren_account.balance))
darren_account.welcome() #need to trigger method/function. if attribute no need bracket. (i.e. account_number). #no need to put print(as function alr show print)
darren_account.deposit(5000)
print(darren_account.check_balance())
darren_account.withdraw(10000)



#est_driven development means write out the interactions first, then write the code##############

class Creditcard:
    #bank_name='YX bank'
    def __init__(self,name,balance,number):
        self.name=name
        self.limit=2000
        #self.number=number
        self.balance=balance
        self.number=number
        
    def check_balance(self):
        print(f'dear {self.name}, you have $ {self.balance} to pay')
    
    def set_card_limit(self,figure):
        if figure>100000 or figure <0:
            print(f'invalid limit increment, you keyed in ${figure}')
        else:
            self.limit+=figure
            print(f'your new limit is ${self.limit}')

    def purchase(self,pay):
        if pay<0 or pay>self.balance:
            print('please purchase properly')
        else:
            self.balance+=pay
            print(self.balance)
    def payment(self,paying):
        if paying<0:
            print('please key in properly')
        else:
            self.balance-=paying
            print(f'your remaining balance ${self.balance}')
            if self.balance<0:
                self.balance=0
                print(f'your remaining balance ${self.balance}')


yx_credit=Creditcard('yx',5000,12345678)
yx_credit.purchase(500)
yx_credit.set_card_limit(500)
assert yx_credit.limit ==2500 ##to make sure credit limit is now 2500, if not will show as error. like a checker.
yx_credit.check_balance()

yx_credit.payment(200)

class BankAccount:
    bank_name = "Bank of Python"  # class attribute
    #init is constructor
    def __init__(self, account_holder_name, account_number, balance): #self->object attribute
			# instance attributes
        self.account_holder_name = account_holder_name  #on the right is passed in by function. #self-> somewhere in the memory, allocate space,create new account, put in a value.
        self.account_number = account_number
        self.balance = balance #use getter instead of attribute, may be reasons why method was implemented
    def welcome(self):
        print('welcome,',self.account_holder_name,'!')

    def check_balance(self): #getter method.
        return self.balance
    
    def deposit(self,figure):
        self.balance+=figure
    
    def withdraw(self,figure):
        if (figure>self.balance):
            print ("insufficient funds")
        else:
            self.balance-=figure



class SavingsAccount(BankAccount):
    def __init__(self,account_holder_name, account_number, balance,interest_rate):
        super().__init__(account_holder_name, account_number, balance)
        self.interest_rate=interest_rate


    def interest_earned(self,years):
        interest_generated= self.balance* years *self.interest_rate
        print(f'you have earned {interest_generated}')

yx_savings=SavingsAccount('yx',12345678,5000,0.01)
yx_savings.interest_earned(5)