def test_case(username, password):
	print(f"Username is {username}, Password is {password}")

test_data = [
	{"username" : "user", "password" : "admin123"},
	{"username" : "user2", "password" : "next123"}
]

for data in test_data:
	test_case(data["username"],data["password"])
