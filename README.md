# daemon

A theme for django admin


## Requirements

Django == 1.10


## Installation

1. clone the master branch in your project directory

```shell
$ git clone https://github.com/rxtfeng/daemon.git
```

2. add `daemon` in `INSTALL_APPS` before the `django.contrib.admin`

```python
INSTALLED_APPS = [
    ......
    'daemon',
    'django.contrib.admin',
    ......
]
```

## Screenshots

![](https://github.com/rxtfeng/daemon/blob/master/screenshots/admin_03.PNG)
![](https://github.com/rxtfeng/daemon/blob/master/screenshots/admin_06.PNG)
![](https://github.com/rxtfeng/daemon/blob/master/screenshots/admin_10.PNG)
![](https://github.com/rxtfeng/daemon/blob/master/screenshots/admin_11.PNG)
![](https://github.com/rxtfeng/daemon/blob/master/screenshots/admin_17.PNG)
![](https://github.com/rxtfeng/daemon/blob/master/screenshots/admin_19.PNG)
![](https://github.com/rxtfeng/daemon/blob/master/screenshots/admin_20.PNG)

[More Screenshots](https://github.com/rxtfeng/daemon/tree/master/screenshots)


## TODO

- [ ] improve changelist_form
