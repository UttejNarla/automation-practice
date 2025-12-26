nano python/day7_mini_automation_project.pydef execute_login_test(login_data):
	username = login_data["username"]
	password = login_data["password"]

	print(f"Attempting login with user = {username}")

	#Simulated validation (structure only)
	if username == "admin" and password == "admin123":
		return "PASS"
	else:
		return "FAIL"

#Test data (list of dictionaries)
test_data = [
	{"username" : "admin", "password" : "admin123"},
	{"username" : "user1", "password" : "pass123"},
	{"username" : "guest", "password" : "guest123"}
]

passed = 0
failed = 0

#Test execution loop
for data in test_data:
	result = execute_login_test(data)

	if result == "PASS":
		passed += 1
	else:
		failed +=1

print("\n--- Test Summary ---")
print(f"Total test: {len(test_data)}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")

