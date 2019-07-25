*django-admin startproject \<projectname\>* <- can be used to initialize a new project

*python manage.py runserver* <- can be used to run the local server 

manage.py code should never be changed. It's a Django administration file. 
Used to run the server, do migrations etc.

wsgi.py should also not be changed.

settings.py contains code specific to the project, here customization can be done about the structure.

urls.py does url directing. What happens when a certain URL gets entered.

To create a virtual env, then you'd first install virtualenv. 
Then to create a virtual env you'd use *virtualenv \<env name\>*.

To activate the venv, you'd use *source \<venv name\>/bin/activate*.

To deactivate, you'd use *deactivate*.

It's better to have the templates folder under your app folder.
To create an app use *python manage.py startapp \<app name\>*

*python manage.py makemigrations* checks if there are any changes to the models that have 
to be applied to the DB and creates a migration file.

*python manage.py migrate* applies all the migrations to the DB.

*python manage.py createsuperuser* to create an admin user with which to login from the admin page.