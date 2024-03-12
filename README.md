
0) has python and pip installed

1) pip install -r requirements.txt

2) uvicorn app:app --host 0.0.0.0 --port 8080

3) curl -X POST http://localhost:8080/position -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"x": 1, "y": 2, "z": 4}'

