Django-vali is a admin theme 
platform. Back end part built using the `Django`_ CBV (Class Based Views),
And the front end built using `Vali Admin`_
boostrap admin panel front end framework. At the moment the software is in alpha version.
python and bower packaging and also documentation will coming soon. Now you can just clone it and run from the source directory.
There is example project and app under the myapp and myproject folders, you can play with.

Requirements
------------

django >= 1.10

How to run
----------

This section assumes your are running some debian like linux OS, your current directory is a project root

- Install requirements if you have no installed them:

.. code:: sh

    $ sudo pip install django


- Add `vali` to your `INSTALLED_APPS` setting like this:
.. code:: sh
    INSTALLED_APPS = (
        'vali',
        'django.contrib.admin',
        ...
    )

- Create your local_settings.py and put your database connection settings there. Then build django database:

.. code:: sh

    $ ./manage.py makemigrations
    $ ./manage.py migrate
    $ ./manage.py createsuperuser
    $ ./manage.py runserver

- Point your browser to http://localhost:8000


.. _`Django`: http://djangoproject.com/
.. _`Vali Admin`: https://github.com/pratikborsadiya/vali-admin

## License

This project is licensed under the [MIT](LICENSE) License