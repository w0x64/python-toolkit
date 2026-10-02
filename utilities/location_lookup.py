import geocoder

def get_location():
    location = input("Enter the location: ")
    g = geocoder.arcgis(location)
    latlng = g.latlng
    if latlng:
        print(f"Latitude and Longitude for {location}: {latlng}")
    else:
        print(f"Unable to determine latitude and longitude for {location}.")

if __name__ == "__main__":
    get_location()
    input("Press Enter to close...")
