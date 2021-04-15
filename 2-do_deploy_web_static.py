#!/usr/bin/python3
"""Fabric script that distributes an archive
to your web servers, using the function do_deploy"""

from fabric.api import local, put, env, run
from os import path
env.hosts = ['35.196.233.214', '35.237.121.210']
env.user = "ubuntu"


def do_deploy(archive_path):
    """function to distribute an archive to web server"""
    if not (path.exists(archive_path)):
        return False
    try:
        put(archive_path, "/tmp/")
        name = archive_path.split('/')[1].split('.')[0]
        run("mkdir -p /data/web_static/releases/{}".format(name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}"
            .format(name, name))
        run("rm /tmp/{}.tgz".format(name))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        return True
    except:
        return False
