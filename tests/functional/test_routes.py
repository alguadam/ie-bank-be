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
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    assert response.status_code == 200

def test_update_account(testing_client):
    """
    GIVEN a Flask application
    WHEN an account is updated by sending a PUT request to '/accounts/<account_id>' endpoint
    THEN check the response is valid
    """
    # Assuming you have an 'account_id' to update, modify this as per your implementation
    account_id_to_update = 1
    response = testing_client.put(f'/accounts/{account_id_to_update}', json={'name': 'John Doe', 'currency': '$', 'country': 'Spain'})
    assert response.status_code == 200

def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN an account is deleted by sending a DELETE request to '/accounts/<account_id>' endpoint
    THEN check the response is valid
    """
    # Assuming you have an 'account_id' to delete, modify this as per your implementation
    account_id_to_delete = 1
    response = testing_client.delete(f'/accounts/{account_id_to_delete}')
    assert response.status_code == 200  # Assuming a successful deletion returns a 204 No Content status code