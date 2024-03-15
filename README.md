# Stucture

TODO

# Run locally

## Prerequisites

- has python>=3.8 and pip3 installed

## Run

```bash
pip install -r requirements.txt
python medhand/main.py
```

## Test

1) either bash:
```bash
curl -X POST http://localhost:8080/position -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"x": 1, "y": 2, "z": 4}'
```

2) or JS:
```
fetch("http://localhost:8080/position", {method: "POST", body: '{"x":100,"y":2000,"z":4}', headers: {
  "Content-type": "application/json; charset=UTF-8"
}}).then((json) => console.log(json));
```

# Compile

- Ubuntu: ./compilation/compile_ubuntu.sh

- Windows: ./compilation/compile_wine.sh

