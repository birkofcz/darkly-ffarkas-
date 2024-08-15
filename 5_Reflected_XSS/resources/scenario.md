# Reflected XSS scenario

Imagine a web application with a search feature. Users can enter a search query, which is then included in the search results page.
- The search page has a search form where users can submit a query.
- The search query is included directly in the response HTML without proper sanitization or escaping.

```
user1 --> submits malicious input --> GET request
                    |                      |
        URL is sent to the victim          SERVER <-- reflect --> HTML with malicious script
                    |                           |
user2 --> clicks on the malicious link --> GET request --> HTML gets rendered
```

The attacker crafts a malicious URL with a script injected into the query parameter:
``` html
http://example.com/search?query=<script>alert('This is a reflected XSS attack!');</script>
```
When a user clicks on the malicious link or is tricked into visiting it, the server responds with the search results page that includes the query as part of the HTML:
``` html
<div class="search-results">
  <p>You searched for: <script>alert('This is a reflected XSS attack!');</script></p>
</div>
```
