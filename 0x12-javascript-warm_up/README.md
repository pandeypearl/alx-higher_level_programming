# 0x12. JavaScript - Warm up

## Tasks

### 0. First constant, first print
Write a script that prints "JavaScript is amazing":

<ul>
<li>You must create a constant variable called myVar with the value "JavaScript is amazing"</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$
</code></pre>


### 1. 3 languages
Write a script that prints 3 lines:

<ul>
<li>The first line: "C is fun"</li>
<li>The second line: "Python is cool"</li>
<li>The third line: "JavaScript is amazing"</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$
</code></pre>


### 2. Arguments
Write a script that prints a message depending of the number of arguments passed:

<ul>
<li>If no arguments are passed to the script, print "No argument"</li>
<li>If only one argument is passed to the script, print "Argument found"</li>
<li>Otherwise, print "Arguments found"</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
</ul>

Reference: <a href="https://intranet.alxswe.com/rltoken/5kTYi3rxb6KM1_pivm-tXg">process.argv</a>

<pre><code>
guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/0x12$
</code></pre>


### 3. Value of my argument
Write a script that prints the first argument passed to it:

<ul>
<li>If no arguments are passed to the script, print "No argument"</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<li>You are not allowed to use length</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
School
guillaume@ubuntu:~/0x12$
</code></pre>


### 4. Create a sentence
Write a script that prints two arguments passed to it, in the following format: " is "

<ul>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$
</code></pre>


### 5. An Integer
Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

<ul>
<li>If the argument can’t be converted to an integer, print "Not a number"</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<li>You are not allowed to use try/catch</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/0x12$
</code></pre>


### 6. Loop to languages
Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

<ul>
<li>The first line: "C is fun"</li>
<li>The second line: "Python is cool"</li>
<li>The third line: "JavaScript is amazing"</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<li>You are not allowed to use any if/else statement</li>
<li>You can use only one console.log</li>
<li>You must use a loop (while, for, etc.)</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$
</code></pre>


### 7. I love C
Write a script that prints x times "C is fun"

<ul>
<li>Where x is the first argument of the script</li>
<li>If the first argument can’t be converted to an integer, print "Missing number of occurrences"</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<li>You can use only two console.log</li>
<li>You must use a loop (while, for, etc.)</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$
</code></pre>


### 8. Square
Write a script that prints a square

<ul>
<li>The first argument is the size of the square</li>
<li>If the first argument can't be converted to an integer, print "Missing size"</li>
<li>You must use the character X to print the square</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
<li>You must use a loop (while, for, etc.)</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js School
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$
</code></pre>

### 9. Add
Write a script that prints the addition of 2 integers

<ul>
<li>The first argument is the first integer</li>
<li>The second argument is the second integer</li>
<li>You have to define a function with this prototype: function add(a, b)</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ ./9-add.js 
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$
</code></pre>


### 10. Factorial
Write a script that computes and prints a factorial

<ul>
<li>The first argument is integer (argument can be cast as integer) used for computing the factorial</li>
<li>Factorial of NaN is 1</li>
<li>You must do it recursively</li>
<li>You must use a function</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ ./10-factorial.js 
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$
</code></pre>


### 11. Second biggest!
Write a script that searches the second biggest integer in the list of arguments.

<ul>
<li>You can assume all arguments can be converted to integer</li>
<li>If no argument passed, print 0</li>
<li>If the number of arguments is 1, print 0</li>
<li>You must use console.log(...) to print all output</li>
<li>You are not allowed to use var</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$
</code></pre>


### 12. Object
Update this script to replace the value 12 with 89:

<ul>
<li>You are not allowed to use var</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$
</code></pre>


### 13. Add file
Write a function that returns the addition of 2 integers.

<ul>
<li>The function must be visible from outside</li>
<li>The name of the function must be add</li>
<li>You are not allowed to use var</li>

<a href="https://intranet.alxswe.com/rltoken/1k6VPdLchwtGubOfPyGL1Q">Tip</a>

<pre><code>
guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$
</code></pre>


## Advanced Tasks

### 14. Const or not const
Write a file that modifies the value of myVar to 333

<pre><code>
guillaume@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$
</code></pre>


### 15. Call me Moby
Write a function that executes x times a function.

<ul>
<li>The function must be visible from outside</li>
<li>Prototype: function (x, theFunction)</li>
<li>You are not allowed to use var</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$
</code></pre>


### 16. Add me maybe
Write a function that increments and calls a function.

<ul>
<li>The function must be visible from outside</li>
<li>Prototype: function (number, theFunction)</li>
<li>You are not allowed to use var</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$
</code></pre>


### 17. Increment object
Update this script by adding a new function incr that increments the integer value.

<ul>
<li>You are not allowed to use var</li>
</ul>

<pre><code>
guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$
</code></pre>

