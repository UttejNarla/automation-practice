def simulate_data(username, password):
    valid_users = ["user", "admin"]
    valid_passwords = ["admin123", "next123"]

    if username in valid_users and password in valid_passwords:
        return "PASS"
    else:
        return "FAIL"

def log_result(message):
    with open("login.log", "a") as file:
        file.write(message + "\n")

user_data = [
    {"username" : "user", "password" : "admin123"},
    {"username" : "admin", "password" : "next123"},
    {"username" : "admin2", "password" : "no123"},
    {"username" : "user2", "password" : "user123"}
]

def run_tests():
    for data in user_data:
        try:
            actual = simulate_data(data["username"],data["password"])

            if actual == "PASS":
                print("Login successful")
                log_result(f"Login Successful for user: {data['username']}")
            else:
                print("Login failed")
                log_result(f"Login Failed for user: {data['username']}")
        except Exception as e:
            log_result(f"Error Occurred: {e}")

if __name__ == "__main__":
    run_tests()
