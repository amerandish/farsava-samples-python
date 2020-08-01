import time
from base64 import b64encode

import websocket

api_configs = {
    "baseUrl": 'wss://api.amerandish.com/v1',
    "actionUrl": '/speech/asrlive',
    "authKey": '<YOUR_API_KEY>',
}
file_path = '<YOUR_WAV_FILE_PATH>'

# Buffer Chunk size
BUFFER_CHUNK = 100 * 1000
# Buffer Sending Interval
BUFFER_INTERVAL = 1


def on_message(ws, message):
    print('message', message)


def on_open(ws):
    print('open')
    # read file
    with open(file_path, "rb") as file_data:
        # encode as base64
        base64_data = b64encode(file_data.read())
        for index in range(0, len(base64_data), BUFFER_CHUNK):
            print("send", index, index+BUFFER_CHUNK)
            # send as binary
            ws.send(base64_data[index: index+BUFFER_CHUNK], opcode=websocket.ABNF.OPCODE_BINARY)
            time.sleep(BUFFER_INTERVAL)


def on_close(ws):
    print('close')


def on_error(ws, error):
    print('error', error)


def main():
    try:
        url = api_configs.get("baseUrl") + api_configs.get("actionUrl") + "?jwt=" + api_configs.get("authKey")
        wss = websocket.WebSocketApp(url, on_close=on_close, on_error=on_error, on_message=on_message, on_data=on_message)
        wss.on_open = on_open
        wss.run_forever()
    except Exception as err:
        # other exceptions
        print(err)


main()
