from khayyam import JalaliDatetime


loan_value = 2000000
num_of_installments = 10
share_value = 200000
installment_value = 100000


class Person:
    def __init__(self, name, id, balance, group = None, loan=False, loan_debt=0, share=share_value):
        self.name = name
        self.id = id
        self.group = group
        self.balance = balance
        self.loan = loan
        self.loan_debt = loan_debt
        self.share = share
        self.creation_time = JalaliDatetime.now()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return print(f'{amount} Rials were deposited into your account. Your balance: {self.balance}')
        else:
            return print('the entered value in not valid')
            
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            return print(f'{amount} Rials is withdrawed from your balance. your balance: {self.balance}')
        else:
            return print('your balance is not enough')
        
    def pay_debt(self):
        total_debt = 0
        if self.loan == True:
            total_debt = total_debt + 100000
        total_debt = total_debt + self.share
        if self.balance >= total_debt:
            self.balance = self.balance - total_debt
            if self.group != None:
                bank.groups[self.group].total_debt -= total_debt
            bank.balance += total_debt
        else:
            print('your balance is not enough to pay your debt')
             

####################################################################################################    
# ali = Person('shahriar', '0016986490', 'gholami', 1000000, {'taken':True, 'date':'1400-01-01'}, 1500000, 2500000)
# print(ali.creation_time)
####################################################################################################


class Bank:
    def __init__(self):
        self.accounts = {}
        self.groups = {}
        self.balance = 0

    def create_account(self, name, id, group, initial_balance):
        if id not in self.accounts:
            new_person = Person(name, id, group, initial_balance, loan = False, loan_debt = 0, share = share_value)
            self.accounts[id] = new_person
            return print(f'account with user id: {id} created')
        else:
            return print('account with this user id is already created.')
    
    def get_account_balance(self, id):
        if id in self.accounts:
            return print(self.accounts[id].balance)
        else:
            print('there is no account with this id')

    def create_group(self, name, members, representor_id, total_debt, account, balance):
        new_group = Group(name = name, representor_id = representor_id, account = account, balance = balance)
        self.groups[name] = new_group
        print(f'Group "{name}" has been created.')

    def remove_group(self, name):
        if name in self.groups:
            del self.groups['name']

    def remove_account(self, id):
        if id in self.accounts:
            del self.accounts[id]

bank = Bank()

# ####################################################################################################
# bank = Bank()
# bank.create_account('yashar', '0016986504', 'gholami', 1000000)
# bank.get_account_balance('0016986504')
# ####################################################################################################


class Group:
    def __init__(self, name, representor_id, account, balance):
        self.group_name = name
        self.members = {}
        self.representor = representor_id
        self.account = account
        self.balance = balance
        installments = 0
        for member in self.members:
            if member.loan != False:
                installments = installments + 1
        self.total_debt = installments*installment_value + len(self.members)*share_value

    def add_member(self, name, id, group, initial_balance):
        if id not in self.members:
            new_person = Person(name, id, self.group_name, initial_balance = 0, loan = False, loan_debt = 0, share = share_value)
            self.members[id] = new_person
            return print(f'new member with id:{id} added to the group.')
        else:
            return print('the user is already a member of group.')

    def pay_debt(self):
        self.balance = self.balance - self.total_debt
        bank.balance = bank.balance + self.total_debt


    def show_report(self):
        pass

    def remove_member(self,id):
        if id in self.members:
            del self.members[id]

    def close_group(self):
        pass

bank = Bank()
bank.create_account('yashar', '0016986504', 'gholami', 1000000)
bank.create_group('Group1', ['0016986504'], '0016986504', 0, bank.accounts['0016986504'],0)


# print(bank.accounts['0016986504'].name)
# print(bank.groups)
bank.groups['Group1'].pay_debt()





