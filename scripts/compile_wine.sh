# build
docker build -t wine_pyinstaller -f compilation/wine.pyinstaller.Dockerfile . && \
docker build -t wine_medhand_build -f compilation/wine.build.Dockerfile . && \
# fetch artefact
mkdir -p target/ && \
(rm -r target/target_wine || echo "") && \
(docker container rm wine_medhand || echo "") && \
docker create -it --name=wine_medhand wine_medhand_build && \
docker cp wine_medhand:/src/medhand/dist/main target/target_wine && \
# zip artefact
(rm target/target_wine.zip || echo "") && \
zip -r target/target_wine.zip target/target_wine/
# run
# docker run -p 8080:8080 -it wine_medhand_build
