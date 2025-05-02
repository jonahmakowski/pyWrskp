from webbrowser import open as web_open
from urllib.parse import quote


def open_webpage(page, https=True):
    if https:
        web_open("https://" + page)
    else:
        web_open(page)


def google_search(query):
    base_url = "www.google.com/search?q="
    final_url = base_url + quote(query)
    open_webpage(final_url)
    return final_url
