import pytest
from app import english_learning_app  # Import the Flask app

@pytest.fixture
def client():
    # Setup the test client
    with english_learning_app.test_client() as client:
        yield client

def test_home_page(client):
    """Test if the home page loads successfully"""
    response = client.get('/')  # Replace with the actual route to home if different
    print(response.data)
    assert response.status_code == 200
    assert b"Learn English" in response.data  # Optional check for content

def test_quiz_page(client):
    """Test if the quiz page loads successfully"""
    response = client.get('/quiz')  # Replace with the actual route to quiz if different
    assert response.status_code == 200
    assert b"English Quiz" in response.data  # Optional check for content
