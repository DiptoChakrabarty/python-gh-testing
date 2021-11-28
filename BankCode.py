class InsufficientBalance(Exception):
    pass

class Bank:
    def __init__(self,balance: int = 100) -> None:
        self.balance = balance
    
    def add_money(self, money: int) -> None:
        self.balance = self.balance + money
        print(f"Total Balance is {self.balance}")
    
    def withdraw_money(self, money: int) -> None:
        if money > self.balance:
            raise InsufficientBalance(f"{money} not present in account with balance {self.balance}")
        self.balance = self.balance - money
        print(f"Total Balance is {self.balance}")
        
            
        