import os
import requests

def get_page_info(url, headers = None, proxies = None):
    """
        Gets the page data and the status of code of the givin url 
        If no header is specified a random header wil be chosen to make
        the reqeust.
        The data will be returned as a tuple
    """
    try:
        r = requests.get(url, headers = headers, proxies = proxies)
        return (r.status_code, r.content, r.text)
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema):
        raise InvalidUrl
    except requests.exceptions.ProxyError:
        raise InvalidProxie


class InvalidProxie(Exception):
    """Raised when trying to make a request with a invalid proxie"""
    pass

class InvalidUrl(Exception):
    """Raised when trying to make a request to a invalid url, usually missing http"""
    pass


if __name__ == "__main__":
    proxies = {
        'http': 'http://10.10.1.10:3128',
        'https': 'http://10.10.1.10:1080',
    }
    try:
        get_page_info("http://www.stockx",proxies=proxies)
    except InvalidUrl:
        print("Invalid URL")
    except InvalidProxie:
        print("Proxie not working")