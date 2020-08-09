from geopy.geocoders import ArcGIS
import pandas

geoService = ArcGIS()

addrLocation = geoService.geocode("3666 21st St, San Francisco, CA 94114, USA")

print("Latitude: " + str(addrLocation.latitude))
print("Longitude: " + str(addrLocation.longitude))

######
superMarketData = pandas.read_csv("supermarkets.csv")
#City,State,Country
superMarketData["Full_Address"] = superMarketData["Address"] + " , " + superMarketData["City"] +  " , " + superMarketData["State"] + " , " + superMarketData["Country"]

superMarketData["Location"] = superMarketData["Full_Address"].apply(geoService.geocode)

superMarketData["Latitude"] = superMarketData["Location"].apply(lambda loc : loc.latitude if loc is not None else None)

superMarketData["Longitude"] = superMarketData["Location"].apply(lambda loc : loc.longitude if loc is not None else None)

superMarketData.drop("Full_Address", axis=1, inplace=True)

print(superMarketData)