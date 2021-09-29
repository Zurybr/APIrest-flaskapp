# APIrest-flaskapp
App for test how flask works
## Where do we start? 🚀

_These instructions will allow you to get a copy of the project running on your local machine for development and testing purposes._

## Pre requirements 📋
<hr/>

_Before starting we need to install the following dependencies.
Also you need to install <a href="https://www.python.org/downloads/">python</a>_


```console
user@host$ sudo apt install python3-virtualenv python3-venv
//or 
user@host$ pip install virtualenv
```
## Installation 🔧

We need to create a virtual environment for python

_go to the root folder of the project and run the following commands_
```console
user@host$ virtualenv venv
user@host$ source venv/bin/activate
```

_We will be inside the python virtual environment, now we have to install the project dependencies_

```console
(venv)user@host$ pip install -r requirements.txt
```
### Start project 
_It would only be necessary to execute the project_

```console

(venv)user@host$ python3 app.py runserver

//if you are inside windows
(venv)user@host$ python app.py runserver


```
### close virtual environment
> If you want, you can close virtual environment

```console
(venv)user@host$ deactivate
```
<hr/>

## this app is only for educational purpose
