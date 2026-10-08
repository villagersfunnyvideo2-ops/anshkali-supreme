FROM kalilinux/kali-rolling

ENV DEBIAN_FRONTEND=noninteractive

# Update repository lists and install required GUI dependencies
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
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Allow passwordless sudo for background commands
RUN echo "root ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

WORKDIR /app
COPY . /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8080

CMD ["/entrypoint.sh"]
