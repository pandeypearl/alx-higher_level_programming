# 0x10. Python - Network #0

## TASKS

### 0. cURL body size
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

<ul>
<li>The size must be displayed in bytes</li>
<li>You have to use curl</li>
</ul>

Please test your script in the sandbox provided, using the web server running on port 5000

<pre><code>
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$
</code></pre>


### 1. cURL to the end
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

<ul>
<li>Display only body of a 200 status code response</li>
<li>You have to use curl</li>
</ul>

Please test your script in the sandbox provided, using the web server running on port 5000

<pre><code>
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$
</code></pre>


### 2. cURL Method
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

<ul>
<li>You have to use curl</li>
</ul>

Please test your script in the sandbox provided, using the web server running on port 5000

<pre><code>
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$
</code></pre>


### 3. cURL only methods
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

<ul>
<li>You have to use curl</li>
</ul>

Please test your script in the sandbox provided, using the web server running on port 5000

<pre><code>
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$
</code></pre>


### 4. cURL headers
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

<ul>
<li>A header variable X-School-User-Id must be sent with the value 98</li>
<li>You have to use curl</li>
</ul>

Please test your script in the sandbox provided, using the web server running on port 5000

<pre><code>
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
guillaume@ubuntu:~/0x10$
</code></pre>


### 5. cURL POST parameters
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

<ul>
<li>A variable email must be sent with the value test@gmail.com</li>
<li>A variable subject must be sent with the value I will always be here for PLD</li>
<li>You have to use curl</li>
</ul>

Please test your script in the sandbox provided, using the web server running on port 5000

<pre><code>
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$
</code></pre>


### 6. Find a peak
Technical interview preparation:

<ul>
<li>You are not allowed to google anything</li>
<li>Whiteboard first</li>
</ul>

Write a function that finds a peak in a list of unsorted integers.

<ul>
<li>Prototype: def find_peak(list_of_integers):</li>
<li>You are not allowed to import any module</li>
<li>Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)</li>
<li>6-peak.py must contain the function</li>
<li>6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)</li>
<li>Note: there may be more than one peak in the list</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt 
2 6-peak.txt
guillaume@ubuntu:~/0x10$
</code></pre>

