docker build -t wine_python -f compilation/Dockerfile_wine_python . && \
    docker build -t medhand_build -f compilation/Dockerfile_build .
    docker run -it medhand_build
