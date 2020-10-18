#Tutorial, how to use package from pypl
#Request can use for scrap/grab website

import requests

url = 'https://detik.com'

try:
    response = requests.get(url)
    print(f"Success ! Code : {response.status_code}")
    print(f"Content : {response.text}")
except Exception as e:
    print(f"There is an error {e}")

print("===End Program===")