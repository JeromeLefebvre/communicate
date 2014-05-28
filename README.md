communicate
===========

The website is currently at:
http://whispering-springs-9434.herokuapp.com

A kivy app and Heroku hosted website

Some of the first few steps in setting things up:
Some notes on installation required for the website:
virtualenv --no-site-packages communicate
source communicate/bin/activate
pip3 install flask
python hello.py
ctrl-c # to quit python
mkdir templates
git init
Create heroku account
download heroku toolbelt 

add https://github.com/github/gitignore/blob/master/Python.gitignore  to your .gitignore
pip3 install gunicorn
echo "web: gunicorn hello:app">Procfile
foreman start
pip3 freeze>requirements.txt
heroku create  #essentially creates your remote repository on heroku

git add .
git commit -m " initial"


On Heroku:
* Issues with keys: https://devcenter.heroku.com/articles/keys
* Python on heroku tutorial: https://devcenter.heroku.com/articles/getting-started-with-python
* Where to download heroku tool-belt: https://dashboard.heroku.com/apps
* Changing to python3: https://devcenter.heroku.com/articles/python-runtimes
* A nifty gitignore for python: https://github.com/github/gitignore/blob/master/Python.gitignore
* The website: http://young-tor-5782.herokuapp.com
* Clearing logs: http://stackoverflow.com/questions/5558289/clear-heroku-logs-command

On Database:
* On using Redis http://flask.pocoo.org/snippets/73/

On Flask:
* Some logging issues: http://flask.pocoo.org/docs/errorhandling/
* Running flask locally: http://flask.pocoo.org/docs/quickstart/
* Flask tutorial http://flask.pocoo.org/docs/tutorial/

For Kivy:
* Installing pip locally http://stackoverflow.com/questions/2915471/install-a-python-package-into-a-different-directory-using-pip

On Virtual environments (ignore the command easy_install, use pip instead):
* http://jamie.curle.io/blog/installing-pip-virtualenv-and-virtualenvwrapper-on-os-x/
* http://simononsoftware.com/virtualenv-tutorial/
* http://iamzed.com/2009/05/07/a-primer-on-virtualenv/
