# SQL injection scenario 2

Consider the following administrator login page:
 ```
login    [         ]
password [         ]
 ```

Our goal is to log in as the admin user without knowing the existing password. After trying the <code>admin:admin</code> credentials, the query would look like this:
``` sql
SELECT * FROM logins WHERE username='admin' AND password = 'admin';
```

The page takes in the credentials and uses the <code>AND</code> operator to select records matching the given username and password. If the MySQL database returns matched records, the credentials are valid, so the PHP code evaluates the login attempt as true. If the condition evaluates to true, the admin record is returned, and our login is validated. To disrupt the query, we can use a single quote (') as the username:
``` sql
SELECT * FROM logins WHERE username=''' AND password = 'admin';
```

This results in:
```
Error: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'admin" at line 1
```

To bypass authentication, we need the query to always return true, regardless of the username and password entered. We can achieve this by abusing the <code>OR</code> operator in our SQL injection. An example of a condition that will always return true is <code>'1'='1'</code>. To incorporate this into the query, we use <code>admin' OR '1'='1</code> as our input, so the database receives:

``` sql
SELECT * FROM logins WHERE username='admin' or '1'='1' AND password = 'admin';
```

This query will return true and grant us access.
