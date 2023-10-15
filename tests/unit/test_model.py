from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, country, status and created_at fields are defined correctly
    """
    account = Account('John Doe', 'Spain', '€')
    assert account.name == 'John Doe'
    assert account.country == 'Spain'
    assert account.currency == '€'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'
    
def test_account_balance_update():
    """
    GIVEN an existing Account with initial balance 100.0
    WHEN the account balance is updated through deposit and withdrawal
    THEN check if the balance is updated correctly
    """
    initial_balance = 100.0
    account = Account('Jane Smith', 'USA', '$')
    amount_to_add = 50.0
    account.balance += amount_to_add
    assert account.balance == initial_balance + amount_to_add


def test_account_status_change():
    
    """
    GIVEN an existing Account
    WHEN the account status is changed
    THEN check if the status is updated correctly
    """
    
    account = Account('Alice Johnson', 'Canada', '$')
    assert account.status == 'Active'

    account.status == 'Inactive'
    assert account.status == 'Inactive'


