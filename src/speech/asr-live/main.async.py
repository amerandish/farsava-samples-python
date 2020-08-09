from base64 import b64encode
import asyncio
import aiohttp

api_configs = {
    "baseUrl": 'wss://api.amerandish.com/v1',
    "actionUrl": '/speech/asrlive',
    "authKey": '<YOUR_API_KEY>',
}
file_path = '<YOUR_WAV_FILE_PATH>'

# Buffer Chunk size
BUFFER_CHUNK = 16 * 1000
# Buffer Sending Interval
BUFFER_INTERVAL = 0.01


def message_handler(data):
    print(data)


async def consumer_handler(websocket):
    print('consumer')
    async for message in websocket:
        if message.type in (aiohttp.WSMsgType.CLOSED, aiohttp.WSMsgType.ERROR):
            # you can store your state
            break
        try:
            msg = message.json()
            message_handler(msg)
        except:
            pass
    await websocket.close()


async def producer_handler(websocket, base64_data):
    print('producer')
    for index in range(0, len(base64_data), BUFFER_CHUNK):
        await websocket.send_bytes(base64_data[index:index + BUFFER_CHUNK])
        await asyncio.sleep(BUFFER_INTERVAL)
    await websocket.send_str('close')


async def main():
    url = api_configs.get("baseUrl") + api_configs.get("actionUrl") + "?jwt=" + api_configs.get("authKey")
    with open(file_path, 'rb') as file_handler:
        data_binary = file_handler.read()
    base64_data = b64encode(data_binary)
    loop = asyncio.get_event_loop()
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(url) as ws:
            consumer_task = loop.create_task(consumer_handler(ws))
            producer_task = loop.create_task(producer_handler(ws, base64_data))
            done, pending = await asyncio.wait(
                [consumer_task, producer_task],
                return_when=asyncio.ALL_COMPLETED)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
