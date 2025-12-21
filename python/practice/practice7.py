test = "checkout"
failed_test = ["checkout"]

if test in failed_test:
	print(f"{test} FAILED")
	for attempt in range (1,4):
		print(f"Retry {attempt} for {test}")
