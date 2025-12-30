
def simulate_login(username,password):
	if username == "user" and password == "admin123":
		return "success"
	else:
		return "failed"

test_data = [
	{"username" : "user", "password" : "admin123", "expected": "success"},
	{"username" : "admin", "password" : "next123", "expected": "success"},
	{"username" : "guest", "password" : "admin456", "expected": "failed"}
]

passed = 0
failed = 0

for data in test_data:
	actual = simulate_login(data["username"],data["password"])

	if actual == data["expected"]:
		passed += 1
	else:
		failed += 1

print(f"Total test cases : {len(test_data)}")
print(f"Passes Cases : {passed}")
print(f"Filed Cases : {failed}")
