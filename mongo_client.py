import pymongo, sys, re

# client = pymongo.MongoClient('localhost', 27017)
# db = client['web_data']
# collection = db['test1']

# read in airport codes
f = open("/home/apluser/Desktop/airport_codes.txt", 'r')


# match codes to a country and city
d = {}
line = f.readline()
while line:
	
	sp = line.split("(")
	sp[1] = sp[1][:-2]
	d[sp[0]] = sp[1]
	line = f.readline()

#print(d)

