import pytest
from BankCode import Bank,InsufficientBalance

@pytest.fixture
def default_account():
    # Creates the default Bank Account
    return Bank()

@pytest.fixture
def balance_account():
    # Creates Bank Account with balance 500
    return Bank(500)

def test_default_account(default_account):
    assert default_account.balance == 100
    
def test_set_account_balance(balance_account):
    assert balance_account.balance == 500

def test_add_balance(balance_account):
    balance_account.add_money(1000)
    assert balance_account.balance == 1500

def test_withdraw_balance(balance_account):
    balance_account.withdraw_money(300)
    assert balance_account.balance == 200

def test_exceed_withdraw_amount(balance_account):
    with pytest.raises(InsufficientBalance):
        balance_account.withdraw_money(1000)
    