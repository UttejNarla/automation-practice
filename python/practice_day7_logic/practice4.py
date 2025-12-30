test_name = [
	{"test" : "Login with valid user"},
        {"test" : "Login with invalid user"},
        {"test" : "Login with locked account"}
]


for data in test_name:
	print(f"Test Name : {data['test']}")
