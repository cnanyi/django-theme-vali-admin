Django-vali
------------
- platform Backend part built using the `Django`,
- replace default admin templates using `Vali Admin`

Requirements
------------

* django >= 2.0
* python >= 3.5

How to use
----------
- Install with pip

    $ pip install django-vali

- Add `vali` to your `INSTALLED_APPS` setting like this:
```
    INSTALLED_APPS = (
        'vali',
        'django.contrib.admin',
        ...
    )
```

- Config vali:
```
VALI_CONFIG = {
    # 'dashboard': {'name': '主面板', 'url': '/admin/'},
}
```
- run server
```
    $ ./manage.py runserver
```

- Point your browser to http://localhost:8000

Thanks
---
- [Django project ](http://djangoproject.com/)
- [Vali Admin](https://github.com/pratikborsadiya/vali-admin)


License
--------
This project is licensed under the [MIT](LICENSE) License

Todo
--------

- modify ValiRelatedFieldWidgetWrapper with Vali theme
- support more theme support
- app/model orders
- ...
