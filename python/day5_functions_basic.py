def run_test(test_name):
	print(f"Running test: {test_name}")

run_test("login")
run_test("logout")
run_test("checkout")


def run_test(test_name):
    if test_name == "payment":
        print(f"{test_name}: FAIL")
    else:
        print(f"{test_name}: PASS")

tests = ["login", "logout", "payment"]

for test in tests:
    run_test(test)
