from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€')
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'

def test_update_account_status():
    """
    GIVEN an Account model
    WHEN the account status is updated
    THEN check the updated status is reflected in the model
    """
    account = Account("John Doe", "Spain", "€")
    assert account.status == "Active"
    
    account.status = "Inactive"
    assert account.status == "Inactive"


def test_update_account_balance():
    """
    GIVEN an Account model
    WHEN the account balance is updated
    THEN check the updated balance is reflected in the model
    """
    account = Account("John Doe", "Spain", "€")
    assert account.balance == 0.0
    
    account.balance = 100.0
    assert account.balance == 100.0