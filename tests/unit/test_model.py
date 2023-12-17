from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', 'Germany')
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
    account = Account("John Doe", "€", "Germany")
    assert account.status == "Active"
    
    account.status = "Inactive"
    assert account.status == "Inactive"


def test_update_account_balance():
    """
    GIVEN an Account model
    WHEN the account balance is updated
    THEN check the updated balance is reflected in the model
    """
    account = Account("John Doe","€" ,"Spain")
    assert account.balance == 0.0
    
    account.balance = 100.0
    assert account.balance == 100.0

def test_account_initial_balance():
    """
    GIVEN an Account model
    WHEN a new Account is created without specifying an initial balance
    THEN the initial balance should be set to 0.0
    """
    account = Account('Jane Smith', '$', 'United States')
    assert account.balance == 0.0

def test_account_update_balance():
    """
    GIVEN an Account model
    WHEN the balance of an Account is updated
    THEN the updated balance should be reflected correctly
    """
    account = Account('Bob Johnson', '$', 'Germany')
    # Set an initial balance
    account.balance = 100.0
    assert account.balance == 100.0

    # Update the balance
    account.balance += 50.0
    assert account.balance == 150.0

    # Deduct an amount from the balance
    account.balance -= 75.0
    assert account.balance == 75.0


def test_account_update_balance_1():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the currency is set correctly
    """
    account = Account('John Doe', '€', 'Germany')
    assert account.currency == '€'

def test_account_update_balance_2():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the country is set correctly
    """
    account = Account('John Doe', '€', 'Germany')
    assert account.country == 'Germany'

def test_account_update_balance_3():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the name is set correctly
    """
    account = Account('John Doe', '€', 'Germany')
    assert account.name == 'John Doe'

def test_account_update_balance_4():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the name is set correctly
    """
    account = Account('John Doe', '€', 'US')
    assert account.country == 'US'

