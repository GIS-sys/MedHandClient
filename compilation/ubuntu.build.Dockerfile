FROM ubuntu_pyinstaller
WORKDIR /src/

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY medhand/ medhand/
RUN cd medhand && pyinstaller --hidden-import uvicorn /src/medhand/main.py

CMD ["ls", "medhand/"]
