import requests
from requests.exceptions import HTTPError

apiConfig = {
    "baseUrl": 'https://api.amerandish.com/v1',
    "actionUrl": '/speech/healthcheck',
    "authKey": '<YOUR_API_KEY>',
}


def main():
    try:
        url = apiConfig.get("baseUrl") + apiConfig.get("actionUrl")
        result = requests.get(url, headers={
            'Authorization': f'bearer {apiConfig.get("authKey")}',
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
