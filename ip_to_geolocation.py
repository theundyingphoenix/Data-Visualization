'''Author: Kevin Honsaker
   Sponsor: APL
   Purpose: Translate IP's to geolocation'''

import pymongo
import ipapi


client = pymongo.MongoClient('localhost', 27017)
db = client['web_data']
collection = db['test1']

for doc in collection.find():
	request_ip = doc['requestip']

	loc_ip = ipapi.location(request_ip)
	latitude = loc_ip.get('latitude')
	longitude = loc_ip.get('longitude')

	if not latitude or not longitude:
		continue

	doc['latitude'] = longitude
	doc['longitude'] = latitude