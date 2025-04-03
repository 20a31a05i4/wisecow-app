FROM ubuntu:22.04

# Install ALL required packages with symlinks
RUN apt-get update && \
    apt-get install -y cowsay fortune netcat-openbsd && \
    ln -sf /usr/games/cowsay /usr/bin/cowsay && \
    ln -sf /usr/games/fortune /usr/bin/fortune && \
    ln -sf /usr/bin/nc.openbsd /usr/bin/nc && \
    apt-get clean

# Copy and prepare script (fix line endings)
COPY wisecow.sh /app/
RUN sed -i 's/\r$//' /app/wisecow.sh && \
    chmod +x /app/wisecow.sh

WORKDIR /app
EXPOSE 4499
CMD ["./wisecow.sh"]