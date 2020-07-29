from bs4 import BeautifulSoup
from pathlib import Path
import requests
import json
import csv
import os

agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
web = "https://www.kishorkanthabd.com/e-kishorkantha"
button_class = '.vc_btn'
flip_class = '.real3dflipbook'
flip_data = 'data-flipbook-options'
url_property = 'href'
file_folder = 'kishorekantha/'
csv_file = 'volumes.csv'


def fetch_all_pages(link):
    print('Fetching All Downloadable Pages')
    page = requests.get(link, headers=agent)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.select(button_class)
    web_url = []
    for result in results:
        url = result.get(url_property)
        if len(str(url)) > 1:
            web_url.append(str(url))
    print('Fetched All Downloadable Pages!')
    return web_url


def get_pdf_list(url_list):
    pdf = []
    count = 0
    for url in url_list:
        page = requests.get(url, headers=agent)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find("meta", property="og:title")
        results = soup.select(flip_class)
        count += 1
        print('Parsing ' + title["content"])
        for result in results:
            html = result.get(flip_data)
            parsed = json.loads(html)
            content = {
                'title': title["content"],
                'pdfUrl': parsed['pdfUrl']
            }
            pdf.append(content)
    return pdf


def generate_csv(pdf_list):
    print('Generating CSV File')
    keys = pdf_list[0].keys()
    with open(csv_file, 'w', encoding="utf-8", newline='') as f:
        w = csv.DictWriter(f, keys)
        w.writeheader()
        w.writerows(pdf_list)
    print('CSV File Generated!')


def read_csv():
    print('Reading CSV File')
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        result = []
        for row in reader:
            k, v = row
            result.append({'title': k, 'pdfUrl': v})
        return result[1:]


def download_pdf(complete_list):
    os.mkdir(file_folder)
    for item in complete_list:
        title = item['title']
        url = item['pdfUrl']
        path = file_folder + title + '.pdf'
        f_name = Path(path)
        if len(url) > 0:
            print('Downloading ' + title)
            response = requests.get(url, headers=agent)
            f_name.write_bytes(response.content)
    print('Download Complete!')


def kishor():
    # scrap website and get web pages
    web_pages = fetch_all_pages(web)

    # get pdf list from fetched web pages
    all_pdf = get_pdf_list(web_pages)

    # generate csv for future use
    generate_csv(all_pdf)

    # read csv
    full_downloadable_list = read_csv()

    # download pdf
    download_pdf(full_downloadable_list)
