#!/usr/bin/env bash
# Config server

# Update and install Nginx if it is not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create the required directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, remove if it exists
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
# First, let's prepare the configuration snippet to include in the Nginx config
sudo sed -i '/^}/i \    location /hbnb_static {\n\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Test Nginx configuration for syntax errors
sudo nginx -t

# Restart Nginx to apply the changes
sudo service nginx restart
