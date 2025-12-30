# The function being tested (The Logic)
def simulate_data(username, password):
    if username == "user" and password == "admin123":
        return "success"
    else:
        return "failed"

# --- PYTEST FUNCTIONS ---

def test_login_valid_user():
    # Positive Case 1
    result = simulate_data("user", "admin123")
    assert result == "success"

def test_login_wrong_password():
    # Negative Case 1
    result = simulate_data("user", "wrong123")
    assert result == "failed"

def test_login_empty_fields():
    # Negative Case 2
    result = simulate_data("", "")
    assert result == "failed"
