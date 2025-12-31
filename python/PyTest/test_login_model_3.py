def validate_login(username, password):
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
    result = validate_login(username, password)
    assert result == expected, (
        f"Expected SUCCESS for user='{username}', password='{password}', "
        f"but got '{result}'"
    )

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("user", "wrong123", "FAILURE"),
        ("guest", "admin123", "FAILURE"),
    ]
)

def test_invalid_logins(username, password, expected):
    result = validate_login(username, password)
    assert result == expected, (
        f"Expected FAILURE for user='{username}', password='{password}', "
        f"but got '{result}'"
    )

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("", "", "EMPTY_FIELDS"),
        ("user", "", "EMPTY_FIELDS"),
    ]
)
def test_edge_cases(username, password, expected):
    result = validate_login(username, password)
    assert result == expected, (
        f"Expected EMPTY_FIELDS for user='{username}', password='{password}', "
        f"but got '{result}'"
    )
