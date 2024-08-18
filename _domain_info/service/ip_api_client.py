import requests


def ip_api(ip_or_domain):
    response = requests.get(f"http://ip-api.com/json/{ip_or_domain}")
    return response.json()
