# 0x11. Python - Network #1

## TASKS

### 0. What's my status? #0
Write a Python script that fetches https://alx-intranet.hbtn.io/status

<ul>
<li>You must use the package urllib</li>
<li>You are not allowed to import any packages other than urllib</li>
<li>The body of the response must be displayed like the following example (tabulation before -)</li>
<li>You must use a with statement</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$
</code></pre>


### 1. Response header value #0
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

<ul>
<li>You must use the packages urllib and sys</li>
<li>You are not allow to import packages other than urllib and sys</li>
<li>The value of this variable is different for each request</li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
<li>You must use a with statement</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
guillaume@ubuntu:~/0x11$
</code><pre>


### 2. POST an email #0
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

<ul>
<li>The email must be sent in the email variable</li>
<li>You must use the packages urllib and sys</li>
<li>You are not allowed to import packages other than urllib and sys</li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
<li>You must use the with statement</li>
</ul>

Please test your script in the sandbox provided, using the web server running on port 5000

<pre><code>
guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$
</code></pre>


### 3. Error code #0
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

<ul>
<li>You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code</li>
<li>You must use the packages urllib and sys</li>
<li>You are not allowed to import other packages than urllib and sys</li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
<li>You must use the with statement</li>
</ul>

Please test your script in the sandbox provided, using the web server running on port 5000

<pre><code>
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$
</code></pre>


### 4. What's my status? #1
Write a Python script that fetches https://alx-intranet.hbtn.io/status

<ul>
<li>You must use the package requests</li>
<li>You are not allow to import packages other than requests</li>
<li>The body of the response must be display like the following example (tabulation before -)</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$
</code></pre>


### 5. Response header value #1
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header

<ul>
<li>You must use the packages requests and sys</li>
<li>You are not allow to import other packages than requests and sys</li>
<li>The value of this variable is different for each request</li>
<li>You don’t need to check script arguments (number and type)</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
guillaume@ubuntu:~/0x11$
</code></pre>


### 6. POST an email #1
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

<ul>
<li>The email must be sent in the variable email</li>
<li>You must use the packages requests and sys</li>
<li>You are not allowed to import packages other than requests and sys</li>
<li>You don’t need to error check arguments passed to the script (number or type)</li>
</ul>

Please test your script in the sandbox provided, using the web server running on port 5000

<pre><code>
guillaume@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$
</code></pre>


### 7. Error code #1
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

<ul>
<li>If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code</li>
<li>You must use the packages requests and sys</li>
<li>You are not allowed to import packages other than requests and sys</li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
</ul>

Please test your script in the sandbox provided, using the web server running on port 5000

<pre><code>
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$
</code></pre>


### 8. Search API
Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

<ul>
<li>The letter must be sent in the variable q</li>
<li>If no argument is given, set q=""</li>
<li>If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name></li>
<li>Otherwise:
<ul><li>Display Not a valid JSON if the JSON is invalid</li>
<li>Display No result if the JSON is empty</li></ul></li>
<li>You must use the package requests and sys</li>
<li>You are not allowed to import packages other than requests and sys</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x11$ ./8-json_api.py 
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py a
[8446] amnirqhtfjq
guillaume@ubuntu:~/0x11$ ./8-json_api.py 2
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py b
[7094] bmofakakhke
guillaume@ubuntu:~/0x11$
</code></pre>


### 9. My GitHub!
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

<ul>
<li>You must use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)</li>
<li>The first argument will be your username</li>
<li>The second argument will be your password (in your case, a personal access token as password)</li>
<li>You must use the package requests and sys</li>
<li>You are not allowed to import packages other than requests and sys</li>
<li>You don’t need to check arguments passed to the script (number or type)</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun
2531536
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd
None
guillaume@ubuntu:~/0x11$
</code></pre>

