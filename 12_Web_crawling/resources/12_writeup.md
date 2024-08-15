# Web crawling
- a process of automatically browsing and indexing content from websites
- a robots.txt file tells crawlers which URLs they can access on the site - this is mainly used to avoid overloading the site with requests
- https://www.zenrows.com/blog/web-crawler-python#prerequisites

<b>keywords</b>: guess (hidden file)<br>
<b>attacked site</b>: http://borntosec.42/.hidden/

## Exploit
Upon running <code>nmap</code> with the IP address of the server, we discover a <code>robots.txt</code> file that disallows two entries:
``` shell
└─$ nmap -sVC borntosec.42 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-07 19:27 EDT
Nmap scan report for borntosec.42 (192.168.56.106)
Host is up (0.00070s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.4.6 (Ubuntu)
|_http-title: BornToSec - Web Section
| http-robots.txt: 2 disallowed entries 
|_/whatever /.hidden
|_http-server-header: nginx/1.4.6 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.62 seconds
```
When accessing <code>http://borntosec.42/.hidden</code>, we find the site contains many subsites, each with a <code>README</code> file. One of these files likely contains the flag. Instead of manually checking each file, we create a Python script to automate the crawling process:
``` shell
└─$ python3 crawler.py http://192.168.56.106/.hidden/ README flag

       / _ \
     \_\(_)/_/     Starting crawler at http://192.168.56.106/.hidden/
      _//o\\_      looking for file README containing keyword 'flag'
       /   \

Checking http://192.168.56.106/.hidden/whtccjokayshttvxycsvykxcfm/vsjtwjnsblouvdzmhzwwfiwimv/xhytouigdvshzvldngdskfmkpf/README
```
After some time, a match is found, and we receive the flag:
``` shell
     MATCH FOUND!

Contents of README at http://192.168.56.106/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README: 
Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
```
## Flag
d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466
