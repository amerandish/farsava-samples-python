
# Farsava - ASR Api

First create an `API KEY` [here](https://panel.amerandish.com/)

## install dependencies

```bash
pip install -r requirements.txt
```

## configs
```python
api_configs = {
  "baseUrl": 'https://api.amerandish.com/v1',
  "actionUrl": '/speech/asr',
  "authKey": '<YOUR_API_KEY>',
}

filePath = '<YOUR_WAV_FILE_PATH>'
```

## run

```bash
python3 main.py
```

