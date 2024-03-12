#FROM scottyhardy/docker-wine
FROM ubuntu:20.04

COPY ./install_python.sh ./
RUN /install_python.sh

COPY ./run.sh ./
ENTRYPOINT ["/bin/bash"]
CMD ["./run.sh"]
