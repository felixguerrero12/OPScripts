from bs4 import BeautifulSoup
import requests
import sys

def download_vid(soup):
    for a in soup.findAll('video'):
        link = a.find('source')["src"]
        file_name = link.split('/')[-1]
        r = requests.get(link, stream=True)
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)


def main(argv):
    url = "https://www.cameo.com/emsmariee"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    download_vid(soup)


if __name__ == "__main__":
    sys.exit(main())
