FROM kalilinux/kali-rolling

# System Dependencies & Kali Desktop Setup
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    xfce4 \
    xfce4-goodies \
    tightvncserver \
    novnc \
    websockify \
    python3 \
    python3-tk \
    python3-pip \
    curl \
    git \
    sox \
    libsox-fmt-all \
    sudo \
    && apt-get clean

# Working Directory & Setup App
WORKDIR /app
COPY . /app

# Startup Script Configure
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8080

CMD ["/entrypoint.sh"]
