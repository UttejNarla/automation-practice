status_code = 200

if status_code == 200:
	print("PASS")
elif status_code == 400 or status_code == 500:
	print("FAIL")
else:
	print("UNKNOWN STATUS")

