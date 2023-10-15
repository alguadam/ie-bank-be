from iebank_api import app
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'country': 'Spain', 'currency': '€'})
    assert response.status_code == 200
    
def test_get_single_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<account_id>' page is requested (GET) with a valid account ID
    THEN check the response is valid
    """
        
    testing_client.post("/accounts", json={"name": "John Doe", "country": "Spain", "currency": "$"})
    
    account_number = 1
    response = testing_client.get(f'/accounts/{account_number}')
    assert response.status_code == 200

def test_update_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<account_id>' page is updated (PUT) with a valid account ID
    THEN check the response is valid
    """
    testing_client.post("/accounts", json={"name": "John Doe", "country": "Spain", "currency": "$"}) 
    updated_data = {'name': 'Greta Lerer'}
    account_id = 1
    response = testing_client.put(f'/accounts/{account_id}', json=updated_data)
    assert response.status_code == 200

