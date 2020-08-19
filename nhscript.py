from bs4 import BeautifulSoup
import requests
import argparse

def print_info(soup, url, site_name):
    try:
        print(site_name)
        print("Your url:" + url)
        print(soup.find(id='tags').text)
    except AttributeError:
        print("Not found on " + site_name)


while True:
    parser = argparse.ArgumentParser()
    parser.add_argument("manga_id", help="ID of the manga.", type=int)
    data=parser.parse_args()    
    moolah = str(data.manga_id)
        
    if moolah.isnumeric():
        urlnh = "https://nhentai.net/g/" + moolah
        url9h = "https://9hentai.com/g/" + moolah
        urlnyh = "https://nyahentai.com/g/" + moolah

        # fetching stuff
        matternh = requests.get(urlnh).text
        matter9h = requests.get(url9h).text
        matternyh = requests.get(urlnyh).text

        # brewing some soup
        soupnh = BeautifulSoup(matternh, 'html.parser')
        soup9h = BeautifulSoup(matter9h, 'html.parser')
        soupnyh = BeautifulSoup(matternyh, 'html.parser')

        # printing...wish me luck
        print_info(soupnh, urlnh, "nhentai")
        print_info(soup9h, url9h, "9hentai")
        print_info(soupnyh, urlnyh, "nyahentai")
        break
