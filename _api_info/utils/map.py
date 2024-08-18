def map_link(loc):
    if loc:
        latitude, longitude = loc.split(',')
        google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
    else:
        google_maps_url = None
    return google_maps_url
