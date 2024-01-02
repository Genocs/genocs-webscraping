import requests
from bs4 import BeautifulSoup

# regex module
import re


class ScrapingBlobalBlue:

    def __init__(self, root_url='https://mcc.globalblue.com/autoTaxRefund') -> None:
        self.root_url = root_url

    def run_scraping(self, docId: str, purchaseAmount: float) -> str:

        try:
            results = []

            params = {
                'docId': docId,
                'purchaseAmount': purchaseAmount,
                'qSize': 10
            }

            response = requests.post(self.root_url, data=params)

            # check response
            if response.status_code != 200:
                print('Something went wrong processing POST:',
                      response.status_code)
                return results

            soup = BeautifulSoup(response.text, 'html.parser')

            # parse to get the second link
            second_link = soup.find_all('a', class_='alink')

            # get the link url
            second_url = second_link[0]['href']

            # call the second lunk
            response_second_link = requests.get(second_url)

            # check response second link
            if response_second_link.status_code != 200:
                print('Something went wrong processing POST:',
                      response.status_code)
                return results

            soup_second_link = BeautifulSoup(
                response_second_link.text, 'html.parser')

            table = soup_second_link.find('table', attrs={
                'class': 'u-full-width gb-table gp-table needs-stamp gb-table-override'})
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                # Get rid of empty values
                results.append([ele for ele in cols if ele])

            refund = soup_second_link.find(
                'h1', attrs={'class': 'purchase-amount'})

            results.append(['refund', refund.text.replace(
                "\n", "").replace("\r", "").replace("\t", "")])

            res = {
                'docId': results[1][1],
                'status': results[0][1],
                'shop': results[0][0],
                'purchaseAmount': re.sub(r'[A-Z\s+]', '', results[2][1]),
                'currency': re.sub(r'[0-9\.\s+]', '', results[2][1]),
                'refund': re.sub(r'[A-Z\s+]', '', results[5][1]),
                'date': results[3][1],
                'address': results[4][1]
            }

            return res

        except Exception as e:
            return {'error': "Something went wrong processing POST"}
