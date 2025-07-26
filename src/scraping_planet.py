import requests

class ScrapingPlanet:

    def __init__(self, root_url='https://www.planetpayment.com/tmr-api') -> None:
        self.root_url = root_url

    def run_scraping(self, docId: str) -> str:

        try:
            response = requests.get(self.root_url + '?taxform=' + docId)

            # check response
            if response.status_code != 200:
                print('Something went wrong processing GET:',
                      response.status_code)
                return []

            return response.content

        except Exception as e:
            return {'error': "Something went wrong processing POST"}
