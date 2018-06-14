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
    # 'theme': 'default',  #  other choice: default, blue, purple, brown, green

    # the order for applist:  default, registry
    # 'default' use django's default behavior
    # 'registry' use the sequence of register() in admin.py, (admin_site._registry)
    # display applist by group, use mark in verbose_name_plural,
    # e.g.  verbose_name_plural = system-user
    # display the model "user" in group "system"
    'applist': {"order": "registry", "group": False, "group_marker": "-"},
}
```

- find more info for style customize at [pratikborsadiya' blog ](https://pratikborsadiya.in/blog/vali-admin/)


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
-(done) support more theme support
-(done) app/model orders
-(done) app/model groups
- ...
