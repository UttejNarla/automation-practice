def simulate_data(user_data):
	print(f"Executing testing for : {user_data['username']}")
	if user_data["expected"] == "success":
		return "PASS"
	else:
		return "FAIL"


test_data = [
	{"username" : "user", "password" : "admin123", "skip" : False, "expected" : "success"},
	{"username" : "user2", "password" : "next123", "skip" : True, "expected" : "success"},
	{"username" : "admin", "password" : "not123", "skip" : False, "expected" : "success"},
	{"username" : "guest", "password" : "mine123", "skip" : False, "expected" : "failed"}
]

passed = 0
failed = 0
skipped = 0

print("---Starting testing summary---")

for data in test_data:
	if data["skip"]:
		print(f"SKIPPED : {data['username']}")
		skipped += 1
	else:
		if simulate_data(data) == "PASS":
			passed += 1
		else:
			failed += 1

print("TEST SUMMARY REPORT")
print(f"Total test cases :     {len(test_data)}")
print(f"Passed :               {passed}")
print(f"Failed :               {failed}")
print(f"Skipped :              {skipped}")
