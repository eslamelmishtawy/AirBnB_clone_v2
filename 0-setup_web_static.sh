#!/usr/bin/env bash
#configure servers

if [ ! -x /usr/sbin/nginx ]; then
	sudo apt-get update
	sudo apt-get install nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    <h1>Testing Nginx configuration <h1>
  </body>
</html>" > /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]; then
	rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R /data/ ubuntu:ubuntu
sudo chmod -R 755 /data/

sudo sed -i '48 i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n'

sudo service nginx restart
