FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y wget gnupg software-properties-common apt-utils && \
    dpkg --add-architecture i386 && \
    wget -nc https://dl.winehq.org/wine-builds/winehq.key && \
    apt-key add winehq.key && \
    apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main' && \
    apt update && \
    add-apt-repository -y ppa:cybermax-dexter/sdl2-backport && \
    apt install -y winehq-devel winetricks xvfb

RUN wget https://www.python.org/ftp/python/3.11.5/python-3.11.5-arm64.exe && \
    WINEPREFIX=~/.wine64 WINARCH=win64 winetricks corefonts win10

RUN (Xvfb :0 -screen 0 1024x768x16 &) && \
    DISPLAY=:0.0 WINEPREFIX=~/.wine64 wine cmd /c python-3.11.5-arm64.exe /quiet PrependPath=1 InstallAllUsers=1

COPY ./run.sh ./
ENTRYPOINT ["/bin/bash"]
CMD ["./run.sh"]
