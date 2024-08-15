# Stored XSS scenario

Imagine a web application where users can post comments on a blog. The comments are stored in a database and then displayed to all users who visit the blog page.
- The blog page has a form where users can submit comments.
- The form submits the comment to the server, which stores it in the database.
- When the comment is displayed, it is retrieved from the database and rendered as HTML on the page.

```
user1 --> submits comment --> POST request
                              |
                          SERVER <-- store/fetch --> DATABASE
                              |
user2 --> visit page --> GET request --> HTML with comment gets rendered
```

The attacker submits a comment containign an injection or a malicious script and the web application does not sanitize or escape this input before storing it in the database:
``` html
<script>alert('This is a stored XSS attack!');</script>
```

When other users visit the blog page, the application retrieves the comment from the database and includes it directly in the HTML of the page:
``` html
<div class="comment">
  <script>alert('This is a stored XSS attack!');</script>
</div>
```

As the HTML is rendered in the user's browser, the script executes, displaying an alert box with the message "This is a stored XSS attack!"
