"""

    download nes games from romsmode.com
    downloads the zip file and unzips into nes

    which can be directly loaded to emulators

 """

import requests
import threading
import re
from bs4 import BeautifulSoup
from zipfile import ZipFile

BASE_URL = "https://romsmode.com/roms/nintendo/"

def download(thread_name, page_start, page_end):
    """ download page by page from start-end """

    for i in range(page_start, page_end):

        response = requests.get(BASE_URL+str(i))
        html_doc = response.text
        soup = BeautifulSoup(html_doc, "html.parser")
        game_links = []

        for link in soup.find_all('a'):

            if re.search(r"https://romsmode.com/roms/nintendo/\d*[a-zA-Z]+" ,link.get('href')):
                game_url = link.get('href').split('/')
                url = '/'.join(game_url[:3]+['download']+game_url[3:])
                game_links.append(url)

        for url in game_links:

            response = requests.get(url)
            html_doc = response.text

            game_name = url.split('/')[-1]

            soup = BeautifulSoup(html_doc,"html.parser")
            for w in soup.findAll('a',{'class':'wait__link'}):

                try:
                    print(f"""{thread_name}:{i}:{game_name}:downloading """, end='')
                    zip_file_link = w.get('href')
                    response = requests.get(zip_file_link)

                    with open(game_name+".zip",'wb') as f:
                        f.write(response.content)

                    print("extracting ", end='')
                    with ZipFile(game_name+'.zip','r') as f:
                        f.extractall('nes')

                    print(" finished")
                except:
                    print()
                    print(game_name + " download failed")


thread_array = []

for t in range(0,15):
    t_obj = threading.Thread(target=download, args=('t'+str(t),t*10+1,(t+1)*10+1))
    thread_array.append(t_obj)


for t in thread_array:
    t.start()

for t in thread_array:
    t.join()


print("--- finished ---")
