#!/bin/bash
cd "$(dirname "$0")"/..
# build
docker build -t ubuntu_pyinstaller -f compilation/ubuntu.pyinstaller.Dockerfile . && \
docker build -t ubuntu_medhand_build -f compilation/ubuntu.build.Dockerfile . && \
# fetch artefact
mkdir -p target/ && \
(rm -r target/target_ubuntu || echo "") && \
(docker container rm ubuntu_medhand || echo "") && \
docker create -it --name=ubuntu_medhand ubuntu_medhand_build && \
docker cp ubuntu_medhand:/src/medhand/dist/main target/target_ubuntu && \
# zip artefact
(rm target/target_ubuntu.zip || echo "") && \
zip -r target/target_ubuntu.zip target/target_ubuntu/
# run
# docker run -p 8080:8080 -it ubuntu_medhand_build
