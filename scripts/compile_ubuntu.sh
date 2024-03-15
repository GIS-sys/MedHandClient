# build
docker build -t ubuntu_pyinstaller -f compilation/ubuntu.pyinstaller.Dockerfile . && \
docker build -t ubuntu_medhand_build -f compilation/ubuntu.build.Dockerfile . && \
# fetch artefact
(rm -r ./target_ubuntu || echo "") && \
(docker container rm ubutnu_medhand || echo "") && \
docker create -it --name=ubutnu_medhand ubuntu_medhand_build && \
docker cp ubutnu_medhand:/src/medhand/dist ./target_ubuntu
# zip artefact
rm target_ubuntu.zip
zip -r target_ubuntu.zip target_ubuntu/
# run
# docker run -p 8080:8080 -it ubuntu_medhand_build
