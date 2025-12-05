# jenkins/builder/Dockerfile
FROM jenkins/inbound-agent:latest

USER root

RUN apt-get update && \
    apt-get install -y git build-essential rpm dpkg-dev fakeroot make curl && \
    rm -rf /var/lib/apt/lists/*

USER jenkins
