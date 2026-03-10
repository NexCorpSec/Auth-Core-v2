from src.auth import login

def test_login():
    assert login("admin","admin123") == True
