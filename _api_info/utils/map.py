def map_link(loc):
    latitude, longitude = loc.split(',')
    google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
    return google_maps_url
