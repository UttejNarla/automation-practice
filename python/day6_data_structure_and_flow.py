def execute_login_test(username,password):
	print(f"Attempting login with user= {username}")

login_data = [
	{"username" : "admin", "password" : "admin123"},
	{"username" : "admin2", "password" : "admin 234"}
]

for data in login_data:
	execute_login_test(data['username'], data['password'])

total_tests = len(login_data)
print(f"\nTotal tests executed : {total_tests}")

