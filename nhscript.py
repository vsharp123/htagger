from bs4 import BeautifulSoup
import requests
import argparse


def print_info(page_id: int, site: str):
    try:
        data = soupify(fetch_website(manga(page_id, site)))
    except AttributeError:
        print(f"Requested manga not found on {site}. \n")
        return

    print(f'{site}\nYour url: {manga(page_id, site)}\n{data}\n')


def manga(page: int, source: str):
    """Returns the correct URL for the given source"""
    if source == 'nhentai':
        return f"https://nhentai.net/g/{page}"
    elif source == '9hentai':
        return f"https://9hentai.com/g/{page}"
    elif source == 'nyahentai':
        return f"https://nyahentai.com/g/{page}"


def fetch_website(url: str):
    """Loading website and returning the HTML"""
    return requests.get(url).text


def soupify(soup):
    """Parses HTML into readable format via BeautifulSoup"""
    return BeautifulSoup(soup, 'html.parser')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("manga_id", help="ID of the manga.", type=int)
    data = parser.parse_args()
    manga_id = str(data.manga_id)

    if not manga_id.isnumeric():
        print(f'moolah ({manga_id}) is not numeric')
        exit()
    for x in {'nyahentai', '9hentai', 'nhentai'}:
        print_info(manga_id, x)
