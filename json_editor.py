import re, json

data = []
d = {}

# "/home/apluser/Desktop/data/data.json"
for line in open("/home/apluser/Desktop/data/data.json", 'r'):
	json.loads(line)
	edit = line.replace('[',' ')
	edit = edit.replace(']',' ')
	print(edit)
	print()

	# l = edit.split(',')
	# index = [i for i,s in enumerate(l) if 'requestip' in s]
	# part1, part2 = l[index[0]].split(':')
	# request_ip = part2.replace('"'," ").strip() # retrieve ip
	# loc_ip = ipapi.location(request_ip)
	# latitude = loc_ip.get('latitude')
	# longitude = loc_ip.get('longitude')

	# if not latitude or not longitude:
	# 	continue

	# add new fields to object, but need a list format to 
	# append new data
	l = edit.split(',')
	index = [i for i,s in enumerate(l) if 'requestip' in s]
	part1, part2 = l[index[0]].split(':')
	lat = "-22.323"


	edit = ','.join(l)
	d = json.loads(edit)
	d['latitude'] = lat
	print(d)
	#convert list back to 	
	
	data.append(str(d))
	break
	
print("Adding to new JSON file!")	
with open("/home/apluser/Desktop/data/d.json", 'w') as outfile:
	json.dump(d,outfile)
	# for i in range(0,len(data)):
	# 	ser_data = json.loads(data[i])
	# 	json.dump(ser_data,outfile)
	
