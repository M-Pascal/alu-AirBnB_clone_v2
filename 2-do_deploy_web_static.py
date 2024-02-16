#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy:
"""
from fabric.api import *
import os


env.hosts = ["ubuntu@54.173.223.112", "ubuntu@3.80.135.235"]


def do_deploy(archive_path):
    """
    Prototype: def do_deploying on the both servers
    """
    if not os.path.exists(archive_path):
        return False
    archive = archive_path.split('/')[-1]
    filename_folder = archive.split('.')[0]
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{0}".format(filename_folder))
        run("tar -C /data/web_static/releases/{0} \
            -xzvf /tmp/{1}".format(filename_folder, archive))
        run("rm /tmp/{0}".format(archive))
        run("mv /data/web_static/releases/{0}/web_static/* \
            /data/web_static/releases/{1}/".format(filename_folder,
                                                   filename_folder))
        run("rm -rf \
            /data/web_static/releases/{0}/web_static".format(filename_folder))
        run("rm /data/web_static/current")
        run("ln -sf /data/web_static/releases/{0} \
            /data/web_static/current".format(filename_folder))
    except Exception:
        return False
    else:
        return True
