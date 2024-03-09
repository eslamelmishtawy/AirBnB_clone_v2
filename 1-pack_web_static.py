#!/usr/bin/python3

from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    # Create the directory versions if it does not exist
    local("mkdir -p versions")
    # Format the current time and date as a string
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    # The name of the archive
    archive_path = "versions/web_static_{}.tgz".format(now)
    # Create the archive using the local command
    result = local("tar -cvzf {} web_static".format(archive_path))
    
    if result.failed:
        return None
    return archive_path

