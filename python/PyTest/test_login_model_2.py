def validate_login(username,password):
	valid_users = ["user", "admin"]
	valid_passwords = ["admin123", "next123"]

	if not username or not password:
		return "EMPTY_FIELDS"

	if username in valid_users and password in valid_passwords:
		return "SUCCESS"

	return "FAILURE"

import pytest

@pytest.mark.parametrize(
	"username,password,expected",
	[
		("user", "admin123", "SUCCESS"),
        	("admin", "next123", "SUCCESS"),
	]
)

def test_valid_logins(username, password, expected):
    assert validate_login(username, password) == expected

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("user", "wrong123", "FAILURE"),
        ("guest", "admin123", "FAILURE"),
    ]
)
def test_invalid_logins(username, password, expected):
    assert validate_login(username, password) == expected

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("", "", "EMPTY_FIELDS"),
        ("user", "", "EMPTY_FIELDS"),
    ]
)
def test_edge_cases(username, password, expected):
    assert validate_login(username, password) == expected
