test = "checkout"

if test == "checkout":
	print(f"{test} FAILED")
	for attempt in range (1,4):
		print(f"Retry {attempt} for {test}")
