
# Farsava - ASR live Api (WebSocket)

First create an `API KEY` [here](https://panel.amerandish.com/)

## install dependencies

```bash
pip install -r requirements.txt
```

## configs
```python
api_configs = {
    "baseUrl": 'wss://api.amerandish.com/v1',
    "actionUrl": '/speech/asrlive',
    "authKey": '<YOUR_API_KEY>',
}
file_path = '<YOUR_WAV_FILE_PATH>'
```

## run

sync
```bash
python3 main.py
```
async
```bash
python3 main.async.py
```

