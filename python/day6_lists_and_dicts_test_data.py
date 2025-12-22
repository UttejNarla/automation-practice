def login_test(username,password):
	if username == "admin" and password == "admin123":
		print(f"Login PASSED for {username}")
	else:
		print(f"Login FAILED for {username}")


test_data = [
    {"username": "admin", "password": "admin123"},
    {"username": "user1", "password": "pass123"},
    {"username": "invalid", "password": "wrong"}
]

for data in test_data:
	login_test(data["username"], data["password"])

passed = 0
failed = 0

for data in test_data:
    if data["username"] == "admin" and data["password"] == "admin123":
        passed += 1
    else:
        failed += 1

print(f"\nSummary: Passed={passed}, Failed={failed}")
