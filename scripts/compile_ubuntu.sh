# build
docker build -t ubuntu_pyinstaller -f compilation/ubuntu.pyinstaller.Dockerfile . && \
docker build -t ubuntu_medhand_build -f compilation/ubuntu.build.Dockerfile . && \
# fetch artefact
(docker container rm ubutnu_medhand || echo "") && \
docker create -it --name=ubutnu_medhand ubuntu_medhand_build && \
docker cp ubutnu_medhand:/src/medhand/dist ./target
# zip artefact
rm target.zip
zip -r target.zip target/
# run
docker run -p 8080:8080 -it ubuntu_medhand_build
