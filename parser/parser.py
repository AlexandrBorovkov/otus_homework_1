import requests

from bs4 import BeautifulSoup
from parser.utils import validate_url


def get_links(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.encoding = 'utf-8'
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        links_list = [link['href'] for link in soup.find_all('a', href=validate_url)]
        return links_list
    except Exception:
        return None
