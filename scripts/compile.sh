# build
docker build -t wine_python -f compilation/Dockerfile_wine_python . && \
docker build -t medhand_build -f compilation/Dockerfile_build . && \
# fetch artefact
docker create -it --name=medhand medhand_build && \
docker cp medhand:/src/medhand/dist ./target
# run
docker run -p 8080:8080 -it medhand_build
