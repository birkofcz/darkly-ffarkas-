# SQL injection scenario 1

In a random PHP web application, we connect to the database and use MySQL syntax to interact with it:
 ``` php
$database = new mysqli("localhost", "root", "password", "users");
$query = "select * from category";
$result = $database->query($query);
 ```

A user can perform a search to look for data in the database. The search input is passed to the web application as follows:
``` php
$input =  $_POST['findData'];
$query = "select * from category where items like '%$input'";
$result = $database->query($query);
```

If the input is not properly validated, user input may be directly incorporated into the SQL query and misinterpreted as code rather than a string. For example, if a user inputs <code>random</code>, the query becomes:
``` sql
select * from category where items like '%random'
```

Without proper sanitization, an attacker can inject additional SQL code by including a single quote (') to terminate the user-input field and then append malicious SQL code. For instance, if the user searches for <code>1'; DROP TABLE items;</code>, the query becomes:
``` sql
select * from category where items like '%1'; DROP TABLE items;'
```

This SQL injection will cause a syntax error:
``` sql
Error: near line 1: near "'": syntax error
```

The error occurs because of the unclosed single quote (') at the end of the query. This issue can be mitigated by commenting out the remaining part of the SQL code using <code>-- -</code>:
``` sql
select * from category where items like '%1'; DROP TABLE items; -- -'
```

Once executed, this query will delete the <code>items</code> table, causing significant damage to the web application.
