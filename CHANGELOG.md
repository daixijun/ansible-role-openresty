# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## [0.2.0](https://github.com/daixijun/ansible-role-openresty/compare/v0.1.3...v0.2.0) (2020-04-23)


### ⚠ BREAKING CHANGES

* openresty_vhosts 变量中移除 `locations`, 统一通过 `extra_parameters` 来配置

### Features

* 添加 upstream 支持 ([7d81c48](https://github.com/daixijun/ansible-role-openresty/commit/7d81c488cdd0fd3b80b8191d77c7ee7cfbf46c53))

### [0.1.3](https://github.com/daixijun/ansible-role-openresty/compare/v0.1.2...v0.1.3) (2020-04-22)


### Bug Fixes

* 移除 centos6 支持 ([36d45a0](https://github.com/daixijun/ansible-role-openresty/commit/36d45a00872279031489ff1b058ca941b4fddf16))
