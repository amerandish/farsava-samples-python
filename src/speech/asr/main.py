from base64 import b64encode
import requests
from requests.exceptions import HTTPError


api_configs = {
    "baseUrl": 'https://api.amerandish.com/v1',
    "actionUrl": '/speech/asr',
    "authKey": '<YOUR_API_KEY>',
}
file_path = '<YOUR_WAV_FILE_PATH>'


def main():
    try:
        url = api_configs.get("baseUrl") + api_configs.get("actionUrl")
        with open(file_path, "rb") as file_data:
            base64_data = b64encode(file_data.read()).decode("utf8")
            payload = {
                "config": {
                    "audioEncoding": 'LINEAR16',
                    "sampleRateHertz": 16000,
                    "languageCode": 'fa',
                    "maxAlternatives": 1,
                    "profanityFilter": True,
                    "asrModel": 'default',
                    "languageModel": 'general',
                },
                "audio": {
                    "data": base64_data,
                },
            }
            result = requests.post(url, json=payload, headers={
                'Authorization': f'bearer {api_configs.get("authKey")}',
                'Content-Type': 'application/json'
            })
            if result.status_code == 200:
                # success result
                print("Success", result.json())
            else:
                # other http status codes
                result.raise_for_status()
    except HTTPError as http_err:
        # http error
        print(f'HTTP error occurred: {http_err}, response: {http_err.response.json()}')
    except Exception as err:
        # other exceptions
        print(err)


main()
