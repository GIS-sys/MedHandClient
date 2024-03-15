# build
docker build -t wine_pyinstaller -f compilation/wine.pyinstaller.Dockerfile . && \
docker build -t wine_medhand_build -f compilation/wine.build.Dockerfile . && \
# fetch artefact
(rm -r ./target_wine || echo "") && \
(docker container rm wine_medhand || echo "") && \
docker create -it --name=wine_medhand wine_medhand_build && \
docker cp wine_medhand:/src/medhand/dist ./target_wine
# zip artefact
rm target_wine.zip
zip -r target_wine.zip target_wine/
# run
# docker run -p 8080:8080 -it wine_medhand_build
