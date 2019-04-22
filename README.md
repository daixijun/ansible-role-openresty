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

```yaml
openresty_proxy_timeout: 10
openresty_keepalive_timeout: 60
# 是否允许不通过域名，直接使用IP地址进行访问
openresty_allow_non_servername: false
openresty_log_path: /var/log/nginx/

openresty_vhosts: []
# - server_name: www.baidu.com
#   enable_ssl: false
#   index: main.html
#   document_root: /usr/share/nginx/www.baidu.com/
#   enable_fpm: true
#   extra_parameters:

```

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