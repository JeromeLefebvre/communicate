communicate
===========

A kivy app and Heroku hosted website

Some notes on instalation

virtualenv 702flask⁄
source 702flask/bin/activate
pip3 install flask
python hello.py
ctrl-c # to quit python
mkdir templates
git init
# Create heroku account
# download heroku toolbelt
# https://github.com/github/gitignore/blob/master/Python.gitignore add this to your gitignore
pip3 install gunicorn
echo "web: gunicorn hello:app">Procfile
foreman start
pip3 freeze>requirements.txt
heroku create  #essentially creates your remote repository on heroku

git add .
git commit -m " initial"

Local instal of packages for Kivy:



Extra links:
Issues with keys
https://devcenter.heroku.com/articles/keys
Python tutorial:
https://devcenter.heroku.com/articles/getting-started-with-python
Where to download thigns:
https://dashboard.heroku.com/apps
Changing to python3:
https://devcenter.heroku.com/articles/python-runtimes
A nifty gitignore for python:
https://github.com/github/gitignore/blob/master/Python.gitignore
Some notes on what virtualenv is:
http://jamie.curle.io/blog/installing-pip-virtualenv-and-virtualenvwrapper-on-os-x/
The website:
http://young-tor-5782.herokuapp.com
On using Redis
http://flask.pocoo.org/snippets/73/
Clearing logs:
http://stackoverflow.com/questions/5558289/clear-heroku-logs-command
Running flask locally:
http://flask.pocoo.org/docs/quickstart/
Flask tutorial
http://flask.pocoo.org/docs/tutorial/
Installing pip locally
http://stackoverflow.com/questions/2915471/install-a-python-package-into-a-different-directory-using-pip

Some logging issues
http://flask.pocoo.org/docs/errorhandling/
