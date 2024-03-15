# build
docker build -t wine_pyinstaller -f compilation/wine.pyinstaller.Dockerfile . && \
docker build -t wine_medhand_build -f compilation/wine.build.Dockerfile . && \
# fetch artefact
(docker container rm wine_medhand || echo "") && \
docker create -it --name=wine_medhand wine_medhand_build && \
docker cp wine_medhand:/src/medhand/dist ./target
# zip artefact
rm target.zip
zip -r target.zip target/
# run
docker run -p 8080:8080 -it wine_medhand_build
