FROM ubuntu:latest
RUN apt-get -y update && apt-get -y install python3.8 && apt-get -y install curl && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && apt-get install -y zip && apt-get install -y unzip && unzip awscliv2.zip && ./aws/install
VOLUME ["/home/dell/.aws"]
