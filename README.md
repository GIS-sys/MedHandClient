Run locally

0) has python and pip installed

1) pip install -r requirements.txt

2) python main.py

3) curl -X POST http://localhost:8080/position -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"x": 1, "y": 2, "z": 4}'

Compile for windows (TODO for linux)

./scripts/compile.sh


cd /home/gordei/.wine/drive_c/users/gordei/Temp
wine pyinstaller --hidden-import uvicorn C:/users/gordei/Temp/main.py
wine dist/main/main.exe
