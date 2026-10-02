import geocoder

def get_location():
    g = geocoder.ipinfo('me')
    latlng = g.latlng
    if latlng:
        print(f"Latitude and Longitude: {latlng}")
    else:
        print("Unable to determine latitude and longitude.")

if __name__ == "__main__":
    get_location()
    input("Press Enter to close...")
