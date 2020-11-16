import requests
from html2text import html2text


def det_page(filename):
    try:
        page = requests.get(filename).text
        return html2text(page)
    except:
        return 'ERROR'