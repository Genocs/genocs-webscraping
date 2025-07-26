import requests
from bs4 import BeautifulSoup

# regex module
import re

# json module
import json

class ScrapingLanghevini:

    def __init__(self, root_url='https://www.langhevini.it') -> None:
        self.root_url = root_url

    def run_scraping(self, page: str) -> str:

        print('Scraping Langhe Vini')
        print('Page:', page)

        try:
            html_response = requests.get(self.root_url + '/produttori/?cpage='+page+'#contenuto')

            # check response
            if html_response.status_code != 202:
                print('Something went wrong processing GET:',
                      html_response.status_code)
                return []
            
            # read file locally
            with open('page_2.txt', 'r') as file:
                file_content = file.read()

            soup = BeautifulSoup(file_content, 'html.parser')

            # get the partners
            partners = soup.find_all('div', attrs={
                'class': 'ogni-socio'})          
#
            res_list = []

            # Cicle through the partners
            for partner in partners:

                # Create an empty dictionary to store data
                socio_data = {}

                # Company name with type
                azienda_p = partner.find('p', class_='socio-azienda')
                socio_data['company_name'] = azienda_p.text.strip()[:-6]  # Remove "(Socio)"

                # Address information
                indirizzo_p = partner.find('p', class_='socio-indirizzo')
                address_parts = indirizzo_p.find_all('span')[1:]
                socio_data['address'] = ' '.join(part.text.strip() for part in address_parts)

                # Extract ZIP, locality, and province
                zip_code = address_parts[0].text.strip()
                locality = address_parts[1].text.strip()
                province = address_parts[2].text.strip()

                socio_data['zip_code'] = zip_code
                socio_data['locality'] = locality
                socio_data['province'] = province

                # Website information
                sito_p = partner.find('p', class_='socio-sito')

                if(sito_p == None):
                    socio_data['website'] = ''
                else:
                    website_a = sito_p.find('a')
                    socio_data['website'] = website_a['href']

                # Convert the dictionary to JSON
                json_data = json.dumps(socio_data, indent=4)  # Indent for readability

                res_list.append(socio_data)

            return res_list

        except Exception as e:
            return {'error': "Something went wrong processing POST" + e}
