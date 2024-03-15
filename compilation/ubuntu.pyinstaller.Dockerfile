FROM ubuntu:20.04

ARG PYTHON_VERSION=3.8
ARG PYINSTALLER_VERSION=6.5.0

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    python${PYTHON_VERSION} \
    python3-pip

# install pyinstaller
RUN /usr/bin/pip install pyinstaller==$PYINSTALLER_VERSION
