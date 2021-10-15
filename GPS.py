from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
# address is a String e.g. 'UAE, Germany'
# addressdetails=True does the magic and gives you also the details
location = geolocator.geocode("Dubai, UAE", addressdetails=True)

print(str(location.raw).encode(encoding="UTF-8"))
