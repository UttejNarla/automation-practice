def validate_login(username, password):
    valid_users = ["user", "admin"]
    valid_passwords = ["admin123", "next123"]

    if not username or not password:
        return "EMPTY_FIELDS"

    if username in valid_users and password in valid_passwords:
        return "SUCCESS"

    return "FAILURE"

def test_valid_user_login():
    assert validate_login("user", "admin123") == "SUCCESS"

def test_admin_login():
    assert validate_login("admin", "next123") == "SUCCESS"

def test_wrong_password():
    assert validate_login("user", "wrong123") == "FAILURE"

def test_unknown_user():
    assert validate_login("guest", "admin123") == "FAILURE"

def test_empty_fields():
    assert validate_login("", "") == "EMPTY_FIELDS"

def test_empty_password():
    assert validate_login("user", "") == "EMPTY_FIELDS"
