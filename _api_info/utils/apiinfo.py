from django.conf import settings
from _api_info.utils.map import map_link
import requests


def ipinfo(ip):
    try:
        r = requests.get(f'https://ipinfo.io/{ip}?token={settings.IPINFOKEY}')
    except Exception as e:
        context = {
            "data":
                {},
            "message": f"connect to ipinfo Error: {e}",
            "status": 500
        }
        return context

    satus_code = r.status_code
    country = r.json().get('country')
    city = r.json().get('city')
    loc = r.json().get('loc')
    org = r.json().get('org')
    timezone = r.json().get('timezone')
    link = map_link(loc)
    context = {
        "data":
            {"ip": ip,
                "country": country,
                "city": city,
                "org": org,
                "timezone": timezone,
                "loc": loc,
                "link": link
             },
        "message": None,
        "status": satus_code
    }
    return context
