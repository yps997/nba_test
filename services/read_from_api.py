import requests

#Sending a request to receive data from an API
def get_data_from_api(url, params=None):
    try:
        response = requests.get(url, params=params)

        response.raise_for_status()

        return response.json()

    except requests.RequestException as error:
        print(f"Something didn't work when sending the request: {error}")
        return None

