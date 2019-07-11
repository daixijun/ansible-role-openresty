Ansible Role: openresty
=========

[![Build Status](https://travis-ci.org/daixijun/ansible-role-openresty.svg?branch=master)](https://travis-ci.org/daixijun/ansible-role-openrety)

Web server openrety for Centos

Requirements
------------

- Centos 6
- Centos 7
- Ansible 2.5+

Role Variables
--------------

[默认参数](defaults/main.yml)

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - { role: daixijun.openresty }
```

License
-------

BSD

Author Information
------------------

Author: Xijun Dai
Email: daixijun1990@gmail.com
