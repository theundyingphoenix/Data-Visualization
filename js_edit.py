import re, json
import pymongo
#from ip2geotools.databases.noncommercial import DbIpCity

	
client = pymongo.MongoClient('localhost', 27017)
db = client['w_data']
collection = db['test_a']

# time = 0
# denom = collection.count_documents({})
# for doc in collection.find():
# 	ip = doc['requestip']
# 	city = doc['City']
# 	print(ip+"  "+city)
# 	try:
# 		response = DbIpCity.get(ip, api_key='free')
# 	except:
# 		pass
# 	print(response.region)
# 	latitude = response.latitude
# 	longitude =  response.longitude
# 	collection.update_one({'_id': doc['_id']}, {'$push': {'latitude': latitude}}, upsert = True)
# 	collection.update_one({'_id': doc['_id']}, {'$push': {'longitude': longitude}}, upsert = True)
# 	print("--Entry added--")

# 	n = float(time) / float(denom)
# 	decimal = n*100
# 	print("%d%%" % decimal)
# 	time+=1 

print("--Starting operations--")
collection.update({}, {'$unset': {'latitude':1}}, multi=True)
print("--First done--")
collection.update({}, {'$unset': {'longitude':1}}, multi=True)
print("--Second done--")
# collection.update({}, {'$unset': {'xforwardedfor':1}}, multi=True)
# print("--Third done--")
# collection.update({}, {'$unset': {'encryptedfields':1}}, multi=True)
# print("--Fourth done--")
# collection.update({}, {'$unset': {'filestatus':1}}, multi=True)
# print("--First done--")

# data = []
# # "/home/apluser/Desktop/data/data.json"
# for line in open("/home/apluser/Desktop/data1/w_d.json", 'r'):
# 	json.loads(line)
# 	edit = line.replace('[',' ')
# 	edit = edit.replace(']',' ')
# 	data.append(edit)


# print("Adding to new JSON file!")	
# with open("/home/apluser/Desktop/data1/ttt.json", 'w') as outfile:
# 	for i in range(0,len(data)):
# 		ser_data = json.loads(data[i])
# 		json.dump(ser_data,outfile)