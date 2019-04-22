import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_openresty_installed(host):
    pkg = host.package('openresty')

    assert pkg.is_installed


def test_openresty_running_and_enabled(host):
    srv = host.service("openresty")

    assert srv.is_running
    assert srv.is_enabled


def test_openresty_http_listening(host):
    s = host.socket("tcp://0.0.0.0:80")

    assert s.is_listening


def test_openresty_https_listening(host):
    s = host.socket("tcp://0.0.0.0:443")

    assert s.is_listening


def test_openresty_vhost(host):
    vhost = host.file(
        "/usr/local/openresty/nginx/conf/vhost.d/www.example.com.conf")

    assert vhost.exists
    assert vhost.is_file


def test_openresty_log_directory(host):
    d = host.file("/var/log/nginx")

    assert d.exists
    assert d.is_directory
    assert d.user == "nginx"
    assert d.group == "nginx"


def test_openresty_web_directory(host):
    d = host.file("/usr/share/nginx/")

    assert d.exists
    assert d.is_directory
    assert d.user == "nginx"
    assert d.group == "nginx"
