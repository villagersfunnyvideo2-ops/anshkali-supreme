#!/bin/bash

# VNC Configuration
USER=root
HOME=/root
export USER HOME

mkdir -p ~/.vnc
echo "anshkali" | vncpasswd -f > ~/.vnc/passwd
chmod 600 ~/.vnc/passwd

# Start VNC Server
vncserver :1 -geometry 1280x720 -depth 24

# Launch Python GUI App inside XFCE Session
DISPLAY=:1 python3 /app/anshkali_app.py &

# Launch noVNC Web Bridge on Port 8080
/usr/share/novnc/utils/novnc_proxy --vnc localhost:5901 --listen 8080
