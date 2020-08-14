import requests
def geturl(url):
    res = requests.get(url,allow_redirects=False)
    url = res.headers.get('location')
    return url
