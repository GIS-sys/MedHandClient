FROM wine_pyinstaller
WORKDIR /wine/drive_c/src/

COPY requirements.txt ./
RUN wine pip install -r requirements.txt

COPY medhand/ medhand/
RUN cd medhand && wine pyinstaller --hidden-import uvicorn C:/src/medhand/main.py

CMD ["wine", "medhand/dist/main/main.exe"]