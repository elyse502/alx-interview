# 0x06. Star Wars API
The `“0. Star Wars Characters”` project requires you to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with several key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.

# Concepts Needed✴️:
1. **HTTP Requests in JavaScript:**
    * Understanding how to make HTTP requests to external services using the `request` module or alternatives like `fetch` in Node.js.
    * [A Complete Guide to Making HTTP Requests in Node.js](https://www.memberstack.com/blog/node-http-request)

2. **Working with APIs:**
    * Understanding the basics of RESTful APIs and how to interact with them.
    * Parsing JSON data returned by APIs.
    * [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)

3. **Asynchronous Programming:**
    * Managing asynchronous operations with callbacks, promises, and async/await syntax.
    * Handling API response data asynchronously.
    * [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

4. **Command Line Arguments in Node.js:**
    * Using the `process.argv` array to access command-line arguments passed to a Node.js script.
    * [How to Parse Command Line Arguments in Node.js](https://tecadmin.net/how-to-parse-command-line-arguments-in-nodejs/)

5. **Array Manipulation and Iteration:**
    * Iterating over arrays and manipulating data structures to format and display character names.
    * [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

By familiarizing yourself with these concepts and resources, you will be able to efficiently retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API, demonstrating your ability to work with external APIs and manage asynchronous code in JavaScript.

# Additional Resources 🧰
[Mock Technical Interview](https://www.youtube.com/watch?v=bmqZ5AhNr3g)


# Requirements 🏛️
## General🧵
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 10.14.x)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/node`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be `semistandard` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
* All your files must be executable
* The length of your files will be tested using `wc`
* You are not allowed to use `var`

# More Info ℹ️
## **Install Node 10**
```groovy
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
## **Install semi-standard**

[Documentation](https://github.com/standard/semistandard)
```groovy
$ sudo npm install semistandard --global
```
## **Install `request` module and use it**

[Documentation](https://github.com/request/request)
```groovy
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

# Tasks 📃
## 0. Star Wars Characters: [0-starwars_characters.js](0-starwars_characters.js)
Write a script that prints all characters of a Star Wars movie:

* The first positional argument passed is the Movie ID - example: `3` = “Return of the Jedi”
* Display one character name per line **in the same order as the “characters” list in the `/films/` endpoint**
* You must use the [Star wars API](https://swapi-api.alx-tools.com/)
* You must use the `request` module
```groovy
alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$
```

<div align="center">

# Reference 📚

# Hello @Cohort 13 👋🏽 - Sometimes we do laugh too, with the `Star Wars API` project! 👇🏽
</div>

🎬 **Ignite Your Fan Projects**: Dive into the Star Wars galaxy with this script! Whether you're analyzing your favorite characters, hosting trivia showdowns, or crafting epic character profiles, the possibilities are as endless as the stars in the sky.

🌐 **Master Data Integration**: Elevate your web development and data analysis skills by learning how to access and process data from APIs. With this script, you'll unlock the power of data manipulation and unleash your creativity in the digital realm.

🚀 **Embark on Your Learning Journey**: Take a leap into the world of APIs! This script provides hands-on practice with essential programming skills like making HTTP requests and parsing JSON data, paving the way for your future coding adventures.

---

<div align="center">

# 📓 About the given Task above 📔
</div>

## Encountering such Error bellow 🐛
The error message `"Cannot find module 'request'"` indicates that the **`'request'`** module is not found when attempting to run the script **0-starwars_characters.js.** This could happen due to several reasons:

**1. Missing Installation:** Although you installed the 'request' module globally using sudo npm install request --global, it seems that the script 0-starwars_characters.js is unable to find the module. This might happen if the script is not in the same environment where the global modules are installed.

**2. Environment Configuration:** Sometimes, the global npm modules might not be available in the current environment or PATH. Ensure that the NODE_PATH environment variable is properly set to include the directory where global npm modules are installed.

## To troubleshoot and fix the issue, you can try the following steps:

* Verify that the 'request' module is indeed installed globally by running `npm list -g request`.
* Check the permissions and ownership of the global npm modules directory. Ensure that it is accessible to the user running the script.
* Double-check the `NODE_PATH` environment variable to make sure it includes the directory where global npm modules are installed.
* If the script is intended to be run in a specific project directory, consider installing the `'request'` module locally within that project using **`npm install request`**.

After taking these steps, try running the script again to see if the issue is resolved.



