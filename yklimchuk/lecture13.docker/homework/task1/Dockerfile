FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app
# Install git, python3, pip3
RUN apt update && apt install -y --no-install-recommends python3 && \
  apt install python3-pip idle3 -y && \
  pip3 install --no-cache-dir --upgrade pip 
RUN pip3 install pytest 
RUN pip3 install requests
COPY app/* ./
RUN pip3 install -r requirements.txt
EXPOSE 5002/tcp
EXPOSE 5002/udp
ENTRYPOINT [ "python3", "simple-app.py", "FOREGROUND" ]
