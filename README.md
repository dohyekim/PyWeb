# PyWeb
Flask with Python
<hr>

This repository contains source codes to practice creating my own personal blog. <br>
To visit and look around how I made it, visit [here](https://github.com/dohyekim/PyWeb/tree/master/helloflask). <br>
<br>
If you click "here", you can see three directories.<br>
<hr>
For "static" directory, I have static files: html, css, js files that I got from mdBootstrap.<br>
For "templates" directory, I have html templates to construct pages for my blog. It also contains macro functions and include files that I used.<br>
For "utils" directory, I have filter functions to manipulate data from view files to html templates.<br>
<br>
<hr>
In "views.py", there are routers and functions including register, login, create a new post, create session/cookie.<br>
In "forms.py", there are classes used to create Register/Login/Post form with flask_wtf/wtforms module.<br>
In "init_db.py", there is a function to connect python with database. (I used MySQL here.)  <br>
In "models.py", there are classes to make it possible to use tables from MySQL in flask.<br>
