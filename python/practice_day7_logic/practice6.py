def test_case(login_data):
	username = login_data["username"]
	password = login_data["password"]

	if username == "user" and password == "admin123":
		return "PASS"
	else:
		return "FAIL"

test_data = [
	{"username" : "user", "password" : "admin123"},
	{"username" : "admin", "password" : "next123"}
]

for data in test_data:
	print(test_case(data))
