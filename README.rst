Django-vali
------------
- platform Backend part built using the `Django`_ ,
- And replace default admin templates using `Vali Admin`_
- At the moment the software is in alpha version.
- python documentation will coming later.

Requirements
------------

django >= 1.10

How to use
----------
- Install with pip
code ::
    $ pip install django-vali

- Add `vali` to your `INSTALLED_APPS` setting like this:

code ::
    INSTALLED_APPS = (
        'vali',
        'django.contrib.admin',
        ...
    )

- Create your local_settings.py and put your database connection settings there. Then build django database:

code ::
    $ ./manage.py runserver

- Point your browser to http://localhost:8000


License
--------
This project is licensed under the [MIT](LICENSE) License

.. _`Django`: http://djangoproject.com/
.. _`Vali Admin`: https://github.com/pratikborsadiya/vali-admin

