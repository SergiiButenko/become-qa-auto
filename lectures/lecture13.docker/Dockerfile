FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app
# Install git, python3, pip3
RUN apt update && apt install -y --no-install-recommends python3 && \
  apt install python3-pip idle3 -y && \
  pip3 install --no-cache-dir --upgrade pip 
COPY . .
ENTRYPOINT [ "sh", "/app/entrypoint.sh" ]