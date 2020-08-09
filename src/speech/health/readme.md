
# Farsava - Health Api

First create an `API KEY` from [here](https://panel.amerandish.com/)

## install dependencies

```bash
pip install -r requirements.txt
```

## configs
```python
api_configs = {
  "baseUrl": 'https://api.amerandish.com/v1',
  "actionUrl": '/speech/healthcheck',
  "authKey": '<YOUR_API_KEY>',
}
```

## run

```bash
python3 main.py
```

