
from bs4 import BeautifulSoup
import requests


class AirBnbSearch:
    def __init__(self, **kwargs):
        self.location = kwargs['location'].replace(', ', '--').replace(' ', '-')
        self.check_in = kwargs['check_in']
        self.check_out = kwargs['check_out']
        self.n_of_rooms = kwargs['n_of_rooms']
        self.n_of_adults = kwargs['n_of_adults']
        self.max_price = kwargs['max_price']
        self.url = None
        self.results = []

    def create_url(self):
        airbnb_url = 'https://www.airbnb.com/s/'
        self.url = f'{airbnb_url}{self.location}/homes?tab_id=home_tab&' \
                   f'query={self.location}&' \
                   f'date_picker_type=calendar&checkin={self.check_in}' \
                   f'&checkout={self.check_out}&' \
                   f'adults={self.n_of_adults}&price_max={self.max_price}&' \
                   f'min_bedrooms={self.n_of_rooms}&zoom_level=11&superhost=true'
        return self.url

    def collect_search_data(self):
        header = {
        'Accept-Language':  'en-US'
        }
        response = requests.get(self.url, headers=header, timeout=5)
        response.raise_for_status()
        html_data = response.text
        soup = BeautifulSoup(html_data, 'html.parser')
        rental_cards = soup.find_all(name='div', attrs={'data-testid': 'card-container'})
        self.create_results(rental_cards)

    def create_results(self, rental_cards):
        for card in rental_cards:
            try:
                score = card.find(name='span', class_='t5eq1io').get('aria-label').split()[0]
            except AttributeError:
                pass
            else:
                if not card.find(name='span', class_='s1j07bg1') and score != 'New':
                    name = card.find(name='span', attrs={'data-testid': 'listing-card-name'}).text
                    price_spans = card.find_all(name='span', class_='a8jt5op')
                    price = price_spans[-2].text.split()[0]
                    url = f"https://www.airbnb.com/{card.find(name='a').get('href')}"
                    self.results.append(RentalInfo(name, price, score, url))


class RentalInfo:

    def __init__(self, name, price, score, url):
        self.name = name
        self.price = price
        self.score = score
        self.url = url
