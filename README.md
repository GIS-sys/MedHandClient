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
curl -X POST http://localhost:8080/new_data -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"ax": 1, "ay": 2, "az": 4, "gx": 1, "gy": 2, "gz": 4}'
```

2) or JS:
```
fetch("http://localhost:8080/new_data", {method: "POST", body: '{"ax": 1, "ay": 2, "az": 4, "gx": 1, "gy": 2, "gz": 4}', headers: {
  "Content-type": "application/json; charset=UTF-8"
}}).then((json) => console.log(json));
```

Port is taken from config.py

# Compile

- Ubuntu: ./compilation/compile_ubuntu.sh

- Windows: ./compilation/compile_wine.sh

