The programs in this language are called _scripts_. They can be written right in a web page’s HTML and run automatically as the page loads.
JavaScript can execute not only in the browser, but also on the server, or actually on any device that has a special program called [the JavaScript engine](https://en.wikipedia.org/wiki/JavaScript_engine).

The browser has an embedded engine sometimes called a “JavaScript virtual machine”.

Different engines have different “codenames”. For example:

- [V8](https://en.wikipedia.org/wiki/V8_(JavaScript_engine)) – in Chrome, Opera and Edge.
- [SpiderMonkey](https://en.wikipedia.org/wiki/SpiderMonkey) – in Firefox.
- …There are other codenames like “Chakra” for IE, “JavaScriptCore”, “Nitro” and “SquirrelFish” for Safari, etc.

The terms above are good to remember because they are used in developer articles on the internet. We’ll use them too. For instance, if “a feature X is supported by V8”, then it probably works in Chrome, Opera and Edge.

safe programming language : does not have low level accces ot memory or cpu like javascript

JavaScript’s capabilities greatly depend on the environment it’s running in. For instance, [Node.js](https://wikipedia.org/wiki/Node.js) supports functions that allow JavaScript to read/write arbitrary files, perform network requests, etc.


In-browser JavaScript can do everything related to webpage manipulation, interaction with the user, and the webserver.

For instance, in-browser JavaScript is able to:

- Add new HTML to the page, change the existing content, modify styles.
- React to user actions, run on mouse clicks, pointer movements, key presses.
- Send requests over the network to remote servers, download and upload files (so-called [AJAX](https://en.wikipedia.org/wiki/Ajax_(programming)) and [COMET](https://en.wikipedia.org/wiki/Comet_(programming)) technologies).
- Get and set cookies, ask questions to the visitor, show messages.
- Remember the data on the client-side (“local storage”).

## [What CAN’T in-browser JavaScript do?](https://javascript.info/intro#what-can-t-in-browser-javascript-do)

JavaScript’s abilities in the browser are limited to protect the user’s safety. The aim is to prevent an evil webpage from accessing private information or harming the user’s data.

Examples of such restrictions include:

- JavaScript on a webpage may not read/write arbitrary files on the hard disk, copy them or execute programs. It has no direct access to OS functions.
    
    Modern browsers allow it to work with files, but the access is limited and only provided if the user does certain actions, like “dropping” a file into a browser window or selecting it via an `<input>` tag.
    
    There are ways to interact with the camera/microphone and other devices, but they require a user’s explicit permission. So a JavaScript-enabled page may not sneakily enable a web-camera, observe the surroundings and send the information to the [NSA](https://en.wikipedia.org/wiki/National_Security_Agency).
    
- Different tabs/windows generally do not know about each other. Sometimes they do, for example when one window uses JavaScript to open the other one. But even in this case, JavaScript from one page may not access the other page if they come from different sites (from a different domain, protocol or port).
    
    This is called the “Same Origin Policy”. To work around that, _both pages_ must agree for data exchange and must contain special JavaScript code that handles it. We’ll cover that in the tutorial.
    
    This limitation is, again, for the user’s safety. A page from `http://anysite.com` which a user has opened must not be able to access another browser tab with the URL `http://gmail.com`, for example, and steal information from there.
    
- JavaScript can easily communicate over the net to the server where the current page came from. But its ability to receive data from other sites/domains is crippled. Though possible, it requires explicit agreement (expressed in HTTP headers) from the remote side. Once again, that’s a safety limitation.


what can in browser javascript can do
add html or read html
set cookies 
remember data on client side
identify user actions
send request over network to remote servers , download and upload files
get and set cookies
remember the data on client side


[The ECMA-262 specification](https://www.ecma-international.org/publications/standards/Ecma-262.htm)

[https://github.com/tc39/proposals](https://github.com/tc39/proposals)


[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)


[https://google.com/search?q=MDN+parseInt](https://google.com/search?q=MDN+parseInt)

## [Compatibility tables](https://javascript.info/manuals-specifications#compatibility-tables)

JavaScript is a developing language, new features get added regularly.

To see their support among browser-based and other engines, see:

- [https://caniuse.com](https://caniuse.com/) – per-feature tables of support, e.g. to see which engines support modern cryptography functions: [https://caniuse.com/#feat=cryptography](https://caniuse.com/#feat=cryptography).
- [https://kangax.github.io/compat-table](https://kangax.github.io/compat-table) – a table with language features and engines that support those or don’t support.


# hello world
JavaScript programs can be inserted almost anywhere into an HTML document using the `<script>` tag.

really old code methods
The `type` attribute: `<script type=…>`
The `language` attribute: `<script language=…>`
``` `` `<`script `` `type```` `=``"`text/javascript`"` ````>` ````<!-- ... //-->````` `` `</`script ```>` ````

external scripts
If we have a lot of JavaScript code, we can put it into a separate file.

Script files are attached to HTML with the `src` attribute:

````` ``` `` `<`script `` `src```` `=``"`/path/to/script.js`"` ````>` ``````` `` `</`script ```>` ```` `````

Here, `/path/to/script.js` is an absolute path to the script from the site root. One can also provide a relative path from the current page.

``` `` `<`script `` `src```` `=``"`https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.11/lodash.js`"` ````>` ``````` `` `</`script ```>` ````

To attach several scripts, use multiple tags:

```
<script srcc= "/js/script1.js"></script>
<script srcc= "/js/script2.js"></script>
```
The benefit of a separate file is that the browser will download it and store it in its [cache](https://en.wikipedia.org/wiki/Web_cache).

Other pages that reference the same script will take it from the cache instead of downloading it, so the file is actually downloaded only once.


if `src` is set, the script content is ignored.

A single `<script>` tag can’t have both the `src` attribute and code inside.

This won’t work:
```
<script src = "file.js>
	alert(1);
<script>
```

We must choose either an external `<script src="…">` or a regular `<script>` with code.
```
 <script src = "file.js>
<script>
script>
	alert(1);
<script>
```


The example above can be split into two scripts to work:


## code structure
## [Statements](https://javascript.info/structure#statements)

Statements are syntax constructs and commands that perform actions.
separated with semicolon ";"
```
alert('Hello, world!');alert('Hello, world!');
```


A semicolon may be omitted in most cases when a line break exists;
```
alert('Hello, world!')
alert('Hello, world!')
```

Here, JavaScript interprets the line break as an “implicit” semicolon. This is called an [automatic semicolon insertion](https://tc39.github.io/ecma262/#sec-automatic-semicolon-insertion).

There are cases when a newline does not mean a semicolon. For example:

```
alert(3 +
1
+ 2);
```

The code outputs `6` because JavaScript does not insert semicolons here.
**But there are situations where JavaScript “fails” to assume a semicolon where it is really needed.**

example
```

```
hello
```
alert("Hello")

[1, 2].forEach(alert);
```
error in console : TypeError: Cannot read properties of undefined (reading '2') 

this is interpreted as
```
alert("Hello")[1, 2].forEach(alert);
```



```

```

## comments

### one line comments

```
//this is single line comment and occcupies line on its own
alert("hello sangamesh")
alert("hello") //this comment follow statement
```


### multiline comments
```
/*
this is a multiline commment
*/
alert("hello")
```


HOTKEYS
 cmd + / (comments line in someeditiors)
 cmd + option + / (multiline omments)

nested cocmments are not supported
```
/*
 /* 
  nested comment 
 */
*/
```
error Unexpected token '*'

## strict mode
For a long time, JavaScript evolved without compatibility issues. New features were added to the language while old functionality didn’t change.

That had the benefit of never breaking existing code. But the downside was that any mistake or an imperfect decision made by JavaScript’s creators got stuck in the language forever.

This was the case until 2009 when ECMAScript 5 (ES5) appeared. It added new features to the language and modified some of the existing ones. To keep the old code working, most such modifications are off by default. You need to explicitly enable them with a special directive: `"use strict"`.

### Example: Assigning to Undeclared Variables

In non-strict mode (pre-ES5), JavaScript allows assigning a value to a variable without declaring it. This can lead to unintended global variables, which are considered bad practice.

#### Old Code (Non-Strict Mode)

javascript


```
`message = "Hello, world!";  // No 'var', 'let', or 'const' console.log(message);  // Outputs: "Hello, world!"`
```

This code works fine in non-strict mode. However, it's creating a global variable `message` because it's not declared with `var`, `let`, or `const`.

#### ES5 Strict Mode

When using strict mode, assigning to an undeclared variable results in an error:


```

`"use strict"; message = "Hello, world!";  // No 'var', 'let', or 'const' console.log(message);  // Throws an error: ReferenceError: message is not defined`
```

In strict mode, JavaScript throws a `ReferenceError` because `message` is not declared.

When you use a [developer console](https://javascript.info/devtools) to run code, please note that it doesn’t `use strict` by default.
to use strict on console

```
'use strict'; <Shift+Enter for a newline>
//  ...your code
<Enter to run>
```

for old browsers
```
(function() {
  'use strict';

  // ...your code here...
})()
```

for oop and modules use strict is done default no need to use
but for simpler code it is better to use


## variables

Variables are used to store this information.
A [variable](https://en.wikipedia.org/wiki/Variable_(computer_science)) is a “named storage” for data we can store name address and other data
To create a variable in JavaScript, use the `let` keyword.

```
let message ;
```

we can put some data into it by using the assignment operator `=`:

```
messaage = "hello" //store the string "hello" in the variable named message
```

The string is now saved into the memory area associated with the variable. We can access it using the variable name:

```
let message ;
message = "hello";
console.log(message)
```

to be concise wee can combine variable declaration and definition into one statement
```
let message = "hello";
console.log(message)
```

we can also declare multiple variable on single line
```
let user = "sangu" ,age = "24" , message = "hello";
```
For the sake of better readability, please use a single line per variable.

```
let user = "sangu";
let age = 24;
let message = "hello";
```

these are othervariants
```
let user = 'John',
  age = 25,
  message = 'Hello';
```

```
let user = 'John'
  , age = 25
  , message = 'Hello';
```

we can cchange value of variable as many times as we want
 value is changed, the old data is removed from the variable:

```
let message;

message = 'Hello!';

message = 'World!'; // value changed

alert(message);
```

We can also declare two variables and copy data from one into the other.

```
let hello = 'Hello world!';

let message;

// copy 'Hello world' from hello into message
message = hello;

// now two variables hold the same data
alert(hello); // Hello world!
alert(message); // Hello world!
```

Declaring twice triggers an error

A variable should be declared only once.

A repeated declaration of the same variable is an error:
```
let message = "This";

// repeated 'let' leads to an error
let message = "That"; // SyntaxError: 'message' has already been declared

```

in pure functional programming lagugage we can not change the value of variable once declared and we are forced to create a new one for other values

### variable naming
the variable should contain only letters numbers and $ and _
the first character can not be a number

camel case is used for variable with many words in it
words go one after another, each word except first starting with a capital letter: `myVeryLongName`.
special charecter an usedd as first ccharacter or whole name
let $ = 1
let _ = 1
is valid


hyphen (-) can not be used in. variable name

variable names are case sensitive

it is possible to use any language for variable name but convention is to use english for variable name

### reserved words
There is a [list of reserved words](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#Keywords), which cannot be used as variable names because they are used by the language itself.

For example: `let`, `class`, `return`, and `function` are reserved.

The code below gives a syntax error:
```
let let = 5; // can't name a variable "let", error!
let return = 5; // also can't name it "return", error!
```

Normally, we need to define a variable before using it. But in the old times, it was technically possible to create a variable by a mere assignment of the value without using `let`. This still works now if we don’t put `use strict` in our scripts to maintain compatibility with old scripts.

```
// note: no "use strict" in this example

num = 5; // the variable "num" is created if it didn't exist

alert(num); // 5
```

```
"use strict";

num = 5; // error: num is not defined
```

###  [Constants](https://javascript.info/variables#constants)

To declare a constant (unchanging) variable, use `const` instead of `let`: and They cannot be reassigned.

```
const myBirthday = '18.04.1982';
```


```
const myBirthday = '18.04.1982';

myBirthday = '01.01.2001'; // error, can't reassign the constant!
```

There is a widespread practice to use constants as aliases for difficult-to-remember values that are known before execution.

```
import math
const Pi = Math.PI
```

A variable name should have a clean, obvious meaning, describing the data that it stores.
it’s much easier to find information that is well-labelled. Or, in other words, when the variables have good names.
Please spend time thinking about the right name for a variable before declaring it. Doing so will repay you handsomely.

Some good-to-follow rules are:

- Use human-readable names like `userName` or `shoppingCart`.
- Stay away from abbreviations or short names like `a`, `b`, and `c`, unless you know what you’re doing.
- Make names maximally descriptive and concise. Examples of bad names are `data` and `value`. Such names say nothing. It’s only okay to use them if the context of the code makes it exceptionally obvious which data or value the variable is referencing.
- Agree on terms within your team and in your mind. If a site visitor is called a “user” then we should name related variables `currentUser` or `newUser` instead of `currentVisitor` or `newManInTown`.

Such programmers save a little bit on variable declaration but lose ten times more on debugging.
An extra variable is good, not evil.
Modern JavaScript minifiers and browsers optimize code well enough, so it won’t create performance issues. Using different variables for different values can even help the engine optimize your code.
Such programmers save a little bit on variable declaration but lose ten times more on debugging.
An extra variable is good, not evil.
Modern JavaScript minifiers and browsers optimize code well enough, so it won’t create performance issues. Using different variables for different values can even help the engine optimize your code.

We generally use upper case for constants that are “hard-coded”. Or, in other words, when the value is known prior to execution and directly written into the code.

In contrast, `age` is evaluated in run-time. Today we have one age, a year after we’ll have another one. It is constant in a sense that it does not change through the code execution. But it is a bit “less of a constant” than `birthday`: it is calculated, so we should keep the lower case for it.

```
const BIRTHDAY = '18.04.1982'; // make birthday uppercase?

const AGE = someCode(BIRTHDAY); // make age uppercase?
```




## data type
A value in JavaScript is always of a certain type. For example, a string or a number.
There are eight basic data types in JavaScript
We can put any type in a variable. For example, a variable can at one moment be a string and then store a number:

```
// no error
let message = "hello";
message = 123456;
```

Programming languages that allow such things, such as JavaScript, are called “dynamically typed”, meaning that there exist data types, but variables are not bound to any of them.

## [Number](https://javascript.info/types#number)

```
let n = 123;
n = 12.345;
```

The _number_ type represents both integer and floating point numbers.

There are many operations for numbers, e.g. multiplication `*`, division `/`, addition `+`, subtraction `-`, and so on.

Besides regular numbers, there are so-called “special numeric values” which also belong to this data type: `Infinity`, `-Infinity` and `NaN`.


