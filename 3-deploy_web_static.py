#!/usr/bin/python3
"""
Script that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import local, put, env, run
from os import path
from datetime import datetime
env.hosts = ['35.196.233.214', '35.237.121.210']
env.user = "ubuntu"


def do_pack():
    """
    Compress before sending
    """
    # create folder it doesn’t exist
    local("mkdir -p versions")
    # create the name of file in str format from datetime.now
    name = "web_static_" + datetime.strftime(datetime.now(),
                                             "%Y%m%d%H%M%S") + ".tgz"
    try:
        local("tar -czvf ./versions/{} ./web_static" .format(name))
        return name
    except Exception:
        return None


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
    except Exception:
        return False


def deploy():
    """
    Full deployment
    """
    try:
        name = do_pack()
        do_deploy(name)
        return True
    except Exception:
        return False
