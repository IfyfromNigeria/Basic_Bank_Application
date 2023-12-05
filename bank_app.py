class Account:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = account_number
        self.account_balance = float(account_balance)
        self.account_holder = account_holder

    def deposit(self, amount):
        self.account_balance += amount
        return f'CR ₦{amount}'
    
    def withdraw(self, amount):
        if amount > self.account_balance:
            print('Withdrawal amount is above available credit\nInsufficient fund')
        else:
            self.account_balance -= amount
        return self.account_balance
    
    def check_balance(self):
        print(f' ₦{self.account_balance}')

my_account = Account('0045979414', 0.00, 'Ifunanya Akupuome')
my_account.deposit(50000)
my_account.check_balance()

ifunanya_account = Account('0706185911', 0.00, 'Jennifer Major')
ifunanya_account.deposit(750000)
ifunanya_account.withdraw(50000)
ifunanya_account.check_balance()