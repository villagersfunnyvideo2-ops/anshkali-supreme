#!/bin/bash

USER=root
HOME=/root
export USER HOME

# Background apt update for Kali tools
apt-get update -y &

mkdir -p ~/.vnc
echo "anshkali" | vncpasswd -f > ~/.vnc/passwd
chmod 600 ~/.vnc/passwd

# Start VNC Display
vncserver :1 -geometry 1280x720 -depth 24

# Launch Python Suite
DISPLAY=:1 python3 /app/anshkali_app.py &

# Start Web Server
/usr/share/novnc/utils/novnc_proxy --vnc localhost:5901 --listen 8080
