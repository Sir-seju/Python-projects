#!/bin/bash

# Starts ssh

/usr/sbin/sshd


# Starts php process in background
poetry shell && sleep 3

cd /webapp

gunicorn -b 0.0.0.0:5000 app:app

# Starts nginx daemon

nginx -g 'daemon off;'

service nginx restart
