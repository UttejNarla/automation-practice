def simulation_data(username,password):
	if username == "user" and password == "admin123":
		return "success"
	else:
		return "failed"


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
		continue

	actual = simulation_data(data["username"],data["password"])
	if actual == data["expected"]:
		passed += 1
	else:
		failed += 1

print("-" *30)
print("TEST SUMMARY REPORT")
print(f"Total test cases :     {len(test_data)}")
print(f"Passed :               {passed}")
print(f"Failed :               {failed}")
print(f"Skipped :              {skipped}")
