# Page d'API chanson !
# https://genius.com/api/artists/142940/songs?page=2&sort=popularity

import requests
from pprint import pprint
from bs4 import BeautifulSoup


def extract_lyrics(url):
    r = requests.get(url)
    print(r.status_code)
    if r.status_code != 200:
        return []

    with open('log.txt','wb')  as f:
        f.write(r.content)


    # pprint(r.content)
    print('ok')
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup)  >>>> OK !
    lyrics = soup.find("div", class_="Lyrics__Container-sc-1ynbvzw-6 jYfhrf")
    pprint(lyrics)

def get_all_urls():

    next_page = 1
    page_number = 1
    links = list()
    
    while next_page:
        if next_page == 1:
            r = requests.get((f"https://genius.com/api/artists/142940/songs?page={page_number}&sort=popularity"))
            if r.status_code == 200:

                response = r.json().get('response', {})
                next_page = response.get('next_page')

                songs = response.get('songs')
                links.extend([song.get('url') for song in songs])
                #pprint(links)

                page_number += 1
                # print(next_page)
    print(len(links))



extract_lyrics(url='https://genius.com/Zazie-parmi-les-sirenes-lyrics')