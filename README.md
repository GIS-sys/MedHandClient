# Run locally

0) has python and pip installed

1) pip install -r requirements.txt

2) python main.py

3) Test via:

```
curl -X POST http://localhost:8080/position -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"x": 1, "y": 2, "z": 4}'
```
or
```
fetch("http://localhost:8080/position", {method: "POST", body: '{"x":100,"y":2000,"z":4}', headers: {
  "Content-type": "application/json; charset=UTF-8"
}}).then((json) => console.log(json));
```

# Compile for windows (TODO for linux)

./scripts/compile.sh

