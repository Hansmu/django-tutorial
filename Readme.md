*django-admin startproject \<projectname\>* <- can be used to initialize a new project

*python manage.py runserver* <- can be used to run the local server 

manage.py code should never be changed. It's a Django administration file. 
Used to run the server, do migrations etc.

wsgi.py should also not be changed.

settings.py contains code specific to the project, here customization can be done about the structure.

urls.py does url directing. What happens when a certain URL gets entered.