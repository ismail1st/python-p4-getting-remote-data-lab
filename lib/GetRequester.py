import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Sends a GET request to the URL and returns the raw response content (bytes).
        """
        response = requests.get(self.url)
        return response.content  # return the raw response body

    def load_json(self):
        """
        Calls get_response_body() and converts the JSON bytes to Python data (list/dict).
        """
        raw_data = self.get_response_body()
        return json.loads(raw_data)  # parse JSON and return as Python object
