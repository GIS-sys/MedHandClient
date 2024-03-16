FROM ubuntu_pyinstaller
WORKDIR /src/

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY medhand/ medhand/
RUN cd medhand && pyinstaller --hidden-import uvicorn --hidden-import=pynput.keyboard._xorg --hidden-import=pynput.mouse._xorg /src/medhand/main.py

CMD ["ls", "medhand/"]
