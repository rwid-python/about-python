#Tutorial, how to use package from pypl
#Request can use for scrap/grab website

import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'

try:
    response = requests.get(url)
    print(f"Success ! Code : {response.status_code}")
    #print(f"Content : {response.text}")
    bs = BeautifulSoup(response.text, features="html.parser")
    print(f'Result BS {url}')
    print(f'Get Title : {bs.title.string}')
except Exception as e:
    print(f"There is an error {e}")

print("===End Program===")