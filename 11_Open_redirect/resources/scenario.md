# Open redirect scenario

You have a web application for an online store. The application includes a feature that allows users to login and then be redirected to a specific page (e.g., a user profile or dashboard) after a successful login. The URL for redirection is provided as a parameter in the query string.

``` html
http://example.com/login?redirect_url=example-home.com
```
After the user logs in, the application redirects them to the URL specified in the <code>redirect_url</code> parameter without validating it. An attacker could craft a URL with a redirect parameter pointing to a malicious site:
``` html
http://example.com/login?redirect_url=http://example.org/dashboard
```
The attacker might send this link to users via email or social media, claiming it’s a special offer or important update. The malicious site could be a phishing site designed to capture the user’s credentials, personal information, or other sensitive data. The user may believe it is a legitimate security measure and re-enter their login details for verification, providing the attacker with unauthorized access to their account.
