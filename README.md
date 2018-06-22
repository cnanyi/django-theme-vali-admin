Django-vali
------------
- platform Backend part built using the `Django`,
- replace default admin templates using `Vali Admin`
![screenshoot](https://github.com/cnanyi/django-vali/blob/master/image.png?raw=true)
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
    # the vali-admin themes  default, blue, purple, green,brown
    'theme': 'default',
    'dashboard': {'name': '主面板', 'url': '/admin/'},
    # the order for applist  default, registry
    # display applist by group: True
    #  e.g. {group: True}
    # default check decorators  vali.decorator.vali_models_group on ModelAdmin
    #  * otherwize use group_marker in verbose_name_plural, (will be deprecated in future version 0.2.0)*
    #  * e.g.  {group: True, group_marker : '-'}
    #    verbose_name_plural = system-user
    #  * display the model "user" in group "system"
    'applist': {"order": "registry", "group": True},
    # default: //maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css
    # 'font_awesome_url': 'font-awesome-4.7.0/css/font-awesome.min.css',
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
