#!/usr/bin/python3
from fabric.api import env, run, put, local
from os.path import exists

env.hosts = ['54.197.21.242', '34.239.107.56']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/rsa_id'


def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if not exists(archive_path):
        return False

    # Extract the file name from the archive path and the base directory name
    file_name = archive_path.split("/")[-1]
    base_dir = file_name.split(".")[0]

    # Upload the archive
    upload_path = "/tmp/{}".format(file_name)
    if put(archive_path, upload_path).failed:
        return False

    # Create directory to unpack the archive
    release_dir = "/data/web_static/releases/{}/".format(base_dir)
    if run("mkdir -p {}".format(release_dir)).failed:
        return False

    # Unpack the archive
    if run("tar -xzf {} -C {}".format(upload_path, release_dir)).failed:
        return False

    # Delete the archive from the server
    if run("rm {}".format(upload_path)).failed:
        return False

    # Delete the symbolic link and create a new one
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s {} /data/web_static/current".format(release_dir)).failed:
        return False

    print("New version deployed!")
    return True
