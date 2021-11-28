import pytest
from BankCode import Bank,InsufficientBalance

def test_default_account():
    account = Bank()
    assert account.balance == 100
    
def test_set_account_balance():
    account = Bank(500)
    assert account.balance == 500

def test_add_balance():
    account = Bank(500)
    account.add_money(1000)
    assert account.balance == 1500

def test_withdraw_balance():
    account = Bank(500)
    account.withdraw_money(300)
    assert account.balance == 200

def test_exceed_withdraw_amount():
    account = Bank(500)
    with pytest.raises(InsufficientBalance):
        account.withdraw_money(1000)
    