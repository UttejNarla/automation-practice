test_cases = ["login", "signup", "checkout"]

for test in test_cases:
	if test == "checkout":
		print(f"{test}: FAILED")
	else:
		print(f"{test}: PASSED")

print("\nRetrying failed test:")

for attempt in range(1,5):
	print(f"Retry attempt {attempt}")


