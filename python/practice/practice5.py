test_cases = ["login", "logout", "payment"]

for test in test_cases:
	if test == "payment":
		print(f"{test}: FAIL")
	else:
		print(f"{test}: PASS")
