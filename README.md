# It is resume project using django that name is [resumeproject](https://techstarmahesh.pythonanywhere.com/).
## This project used django framework and it is using bootstrap for design.


# in this project i am using
    [1]: # Language: django
    [2]: # Language: bootstrap
    [3]: # Language: markdown
    [4]: # Language: html
    [5]: # Language: css
    [6]: # Language: javascript
    [7]: # Language: python

# First of all create a Project

```bash
django-admin startproject resume
```

# Run these command to create some apps

```bash
python manage.py startapp core
python manage.py startapp edu
python manage.py startapp services
```

# Create a repository

```bash
git init

git status

git add .

git commit -m "initial Commit"

git remote add origin https://github.com/techstarMahesh/Resume-using-django.git

git push origin main
```

# Go to this repository for any help

https://github.com/techstarMahesh/Resume-using-django

<aside>
💡 That’s great you are awesome

</aside>

# To host python anywhere

## Get all install package

```bash
pip freeze
```

## Make a another file of all packages

```bash
pip freeze >> requerments.txt
```

### Go to [Python anywhere](https://www.pythonanywhere.com/)

and then create new account and login upload files and then open console and then open bash and run this commands

```bash
mkvirtualenv ms --python=python3.8

workon ms

pip install django or pip install -r reqerment.txt

```

```bash
# wsi file of setting
import os
import sys
#
## assuming your django settings file is at '/home/techstarmahesh/mysite/mysite/settings.py'
## and your manage.py is is at '/home/techstarmahesh/mysite/manage.py'
path = '/home/techstarmahesh/resumeproject'
if path not in sys.path:
    sys.path.append(path)
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'resumeproject.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## Do changes in setting.py

```bash
dbug = False
allow host ['*']

```
