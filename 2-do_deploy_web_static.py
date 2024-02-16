#!/usr/bin/python3
"""Fabric Script that distributes an archives"""
from fabric.api import *
import os

env.hosts = ['54.173.223.112', '3.80.135.235']

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        archive_name = os.path.basename(archive_path)
        archive_name_no_ext = archive_name.split('.')[0]
        release_path = '/data/web_static/releases/{}'.format(archive_name_no_ext)

        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, release_path))
        run('rm /tmp/{}'.format(archive_name))
        run('mv {}/web_static/* {}/'.format(release_path, release_path))
        run('rm -rf {}/web_static'.format(release_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_path))

        return True
    except:
        return False
