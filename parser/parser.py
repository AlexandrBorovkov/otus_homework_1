import requests
from bs4 import BeautifulSoup

from parser.utils import validate_url


def get_links(norm_url, urls_set):
    headers = {
        'user-agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/101.0.4951.67 Safari/537.36'
        ),
        'x-requested-with': 'XMLHttpRequest',
    }
    result_set = set()
    for link in urls_set:
        try:
            response = requests.get(link, headers=headers, timeout=3)
            response.raise_for_status()
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            links_set = {
                link['href']
                for link in soup.find_all(
                    'a',
                    href=lambda x: (
                        not x.startswith(norm_url)
                        and validate_url(x)
                    )
                )
            }
            result_set.update(links_set)
        except Exception:
            continue
    return result_set
