FROM ubuntu:20.04

ARG WINE_VERSION=winehq-stable
ARG PYTHON_VERSION=3.11.5
ARG PYINSTALLER_VERSION=6.5.0
ARG PYTHON_DIR=Python311

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHON_DIR $PYTHON_DIR

# we need wine for this to work, so we'll use the PPA
RUN set -x \
    && dpkg --add-architecture i386 \
    && apt-get update -qy \
    && apt-get install --no-install-recommends -qfy gpg-agent rename apt-transport-https software-properties-common winbind cabextract wget curl zip unzip xvfb xdotool x11-utils xterm \
    && wget -nv https://dl.winehq.org/wine-builds/winehq.key \
    && apt-key add winehq.key \
    && add-apt-repository 'https://dl.winehq.org/wine-builds/ubuntu/' \
    && apt-get update -qy \
    && apt-get install --install-recommends -qfy $WINE_VERSION \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && wget -nv https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks \
    && chmod +x winetricks \
    && mv winetricks /usr/local/bin

# wine-gecko
RUN mkdir -p /usr/share/wine/gecko
RUN curl -o /usr/share/wine/gecko/wine_gecko-2.47-x86.msi http://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86.msi
RUN curl -o /usr/share/wine/gecko/wine_gecko-2.47-x86_64.msi http://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86_64.msi

# wine settings
ENV WINEARCH win64
ENV WINEDEBUG fixme-all
ENV WINEPREFIX /wine

# xvfb settings
ENV DISPLAY :0
RUN set -x \
    && echo 'Xvfb $DISPLAY -screen 0 1024x768x24 &' >> /root/.bashrc

# windows 10 environment
RUN set -x \
    && winetricks -q win10

# PYPI repository location
ENV PYPI_URL=https://pypi.python.org/
# PYPI index location
ENV PYPI_INDEX_URL=https://pypi.python.org/simple

# install python in wine, using the msi packages to install, extracting
# the files directly, since installing isn't running correctly.

RUN set -x \
    && for msifile in `echo core dev exe lib path pip tcltk tools`; do \
        wget -nv "https://www.python.org/ftp/python/$PYTHON_VERSION/amd64/${msifile}.msi"; \
        wine msiexec /i "${msifile}.msi" /qb TARGETDIR=C:/$PYTHON_DIR; \
        rm ${msifile}.msi; \
    done \
    && cd /wine/drive_c/$PYTHON_DIR \
    && echo 'wine '\''C:\'$PYTHON_DIR'\python.exe'\'' "$@"' > /usr/bin/python \
    && echo 'wine '\''C:\'$PYTHON_DIR'\Scripts\easy_install.exe'\'' "$@"' > /usr/bin/easy_install \
    && echo 'wine '\''C:\'$PYTHON_DIR'\Scripts\pip.exe'\'' "$@"' > /usr/bin/pip \
    && echo 'wine '\''C:\'$PYTHON_DIR'\Scripts\pyinstaller.exe'\'' "$@"' > /usr/bin/pyinstaller \
    && echo 'wine '\''C:\'$PYTHON_DIR'\Scripts\pyupdater.exe'\'' "$@"' > /usr/bin/pyupdater \
    && echo 'assoc .py=PythonScript' | wine cmd \
    && echo 'ftype PythonScript=c:\'$PYTHON_DIR'\python.exe "%1" %*' | wine cmd \
    && while pgrep wineserver >/dev/null; do echo "Waiting for wineserver"; sleep 1; done \
    && chmod +x /usr/bin/python /usr/bin/easy_install /usr/bin/pip /usr/bin/pyinstaller /usr/bin/pyupdater \
    && (pip install -U pip || true) \
    && rm -rf /tmp/.wine-*

ENV W_DRIVE_C=/wine/drive_c
ENV W_WINDIR_UNIX="$W_DRIVE_C/windows"
ENV W_SYSTEM64_DLLS="$W_WINDIR_UNIX/system32"
ENV W_TMP="$W_DRIVE_C/windows/temp/_$0"

# install pyinstaller
RUN /usr/bin/pip install pyinstaller==$PYINSTALLER_VERSION

# put the src folder inside wine
RUN mkdir /src/ && ln -s /src /wine/drive_c/src
VOLUME /src/
RUN mkdir -p /wine/drive_c/tmp
