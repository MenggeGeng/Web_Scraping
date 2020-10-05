import requests
from bs4 import BeautifulSoup
import time

def webscrape():
    with open("web_scrape.txt", 'w')as wc:
        for i in range(0,50):
            try:
                resp = requests.get('http://3.95.249.159:8000/random_company').text
            except:
                print('cURL failed')
            else:
                soup = BeautifulSoup(resp, 'html.parser')
                for li in soup.find_all('li'):
                    if("Name: " in li.text):
                        wc.write(str(li.text))
                        wc.write('\n')
                    if("Purpose: " in li.text):
                        wc.write(str(li.text))
                        wc.write('\n\n')
            time.sleep(0.1)

if __name__ == "__main__":
    webscrape()
