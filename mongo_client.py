import pymongo, sys, re
import pandas as pd 
import requests
import lxml.html as lh

url='https://www.nationsonline.org/oneworld/IATA_Codes/airport_code_list.htm'

#Create a handle, page, to handle the contents of the website
page = requests.get(url)

#Store the contents of the website under doc
doc = lh.fromstring(page.content)

#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

#print [len(T) for T in tr_elements[:12]]
 
tr_elements = doc.xpath('//tr')

#Create empty list
col=[]
i=0
l = ['','City/Airport', 'Country', 'IATA']

for t in tr_elements[1]:
    i+=1
    name = l[i]
    #print '%d:"%s"'%(i,name)
    col.append((name,[]))
    
#Since first row is the header, data is stored on the second row onwards
for j in range(1,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    
    #If row is not of size 10, the //tr data is not from our table 
    if len(T)!=3:
        continue
    
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1   

# Dictionary with 3 keys City/Airport, Country, and IATA
Dict = {title:column for (title,column) in col}

# code = "MIAC3-C1"
# print "Searching dictionary to find "+code+" location..."
# key = 'IATA'
# for i in range(0,len(Dict[key])):
# 	#print "Searching "+str(i)+" ..."
# 	if Dict[key][i] in code:
# 		print "Match found!"+" "+code+" = "+Dict[key][i]
# 		print "This is in "+Dict['City/Airport'][i]+", "+Dict['Country'][i]	

client = pymongo.MongoClient('localhost', 27017)
db = client['web_data']
collection = db['test1']

for doc in collection.find():
	loc = doc['location']
	# code should be the data's location
	code = loc
	print "Searching dictionary to find "+loc+" location..."
	key = 'IATA'
	for i in range(0,len(Dict[key])):
		#print "Searching "+str(i)+" ..."
		if Dict[key][i] in code:
			print "Match found!"+" "+code+" = "+Dict[key][i]
			print "This is in "+Dict['City/Airport'][i]+", "+Dict['Country'][i]	
			break
	




# # read in airport codes
# f = open("/home/apluser/Desktop/airport_codes.txt", 'r')


# # match codes to a country and city
# d = {}
# line = f.readline()
# while line:
# 	sp = line.split("(")
# 	sp[1] = sp[1][:-2]
# 	d[sp[0]] = sp[1]
# 	line = f.readline()

# # now cross-examine the dictionary with the db
# for doc in collection.find():
# 	loc = doc['location']
# 	print("Searching dictionary for %s." % loc)
# 	for i in d.keys():
# 		if re.search(loc, d[i]):
# 			print("Found a match! %s & %s" % (loc,d[i]))
