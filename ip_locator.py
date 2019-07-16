import re, json
import ipapi

data = []
d = {}

count = 0
# "/home/apluser/Desktop/data/data.json"
for line in open("/home/apluser/Desktop/data/data.json", 'r'):
	json.loads(line)
	edit = line.replace('[',' ')
	edit = edit.replace(']',' ')
	

	d = json.loads(line)
	request_ip = d['requestip']
	loc_ip = ipapi.location(request_ip)
	print(loc_ip)
	lat = loc_ip.get('latitude')
	longitude = loc_ip.get('longitude')

	print(longitude)
	print(lat)
	if not lat or not longitude:
		continue
	break
	# # add new fields to object, but need a list format to 
	# # append new data
	d['latitude'] = lat
	d['longitude'] = longitude
	
	print(count)
	if count == 100:
		break
	count+=1
	
print("Adding to new JSON file!")	
with open("/home/apluser/Desktop/data/d.json", 'w') as outfile:
	json.dump(d,outfile)
	
