# 0x06. Star Wars API
# Requirements 🏛️
## General🧵
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 10.14.x)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/node`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be `semistandard` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons](https://github.com/standard/semistandard) on top. Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
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
</div>

# Hello @Cohort 13 👋🏽 - Sometimes we do laugh too, with the Star Wars API project! 👇🏽 

🎬 **Ignite Your Fan Projects**: Dive into the Star Wars galaxy with this script! Whether you're analyzing your favorite characters, hosting trivia showdowns, or crafting epic character profiles, the possibilities are as endless as the stars in the sky.

🌐 **Master Data Integration**: Elevate your web development and data analysis skills by learning how to access and process data from APIs. With this script, you'll unlock the power of data manipulation and unleash your creativity in the digital realm.

🚀 **Embark on Your Learning Journey**: Take a leap into the world of APIs! This script provides hands-on practice with essential programming skills like making HTTP requests and parsing JSON data, paving the way for your future coding adventures.






