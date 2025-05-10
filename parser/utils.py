from urllib.parse import urlparse

import validators


def validate_url(input_url):
    if validators.url(input_url) and len(input_url) < 255:
        return True
    return False

def normalize_url(url):
    parsed_url = urlparse(url)
    normalized_scheme = parsed_url.scheme.lower()
    normalized_host = parsed_url.hostname.lower()
    return f"{normalized_scheme}://{normalized_host}"

def write_to_file(data):
    with open("links.txt", 'w', encoding='utf-8') as file:
        file.write("\n".join(data))
