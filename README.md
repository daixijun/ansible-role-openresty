# daixijun.openresty

[![Build Status](https://github.com/daixijun/ansible-role-openresty/workflows/build/badge.svg)](https://github.com/daixijun/ansible-role-openresty/actions)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-daixijun.openresty-660198.svg?style=flat)](https://galaxy.ansible.com/daixijun/openresty/)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/daixijun/ansible-role-openresty?sort=semver)](https://github.com/daixijun/ansible-role-openresty/tags)

Ansible安装配置OpenResty

## 环境要求

- RHEL/Centos 6+
- Ansible 2.5+

## 变量

参考[defaults](defaults/main.yml)

## 依赖

None

## 示例

```yaml
- hosts: servers
  roles:
    - { role: daixijun.openresty }
```

## License

BSD

## 维护者

- Xijun Dai <daixijun1990@gmail.com>
