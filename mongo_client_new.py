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
db = client['data']
collection = db['test1']

doc_count = collection.count_documents({})
numer = 0

for doc in collection.find():

	loc = doc['location']
	# code should be the data's location
	code = loc
	print "Searching dictionary to find "+loc+" location..."
	key = 'IATA'
	for i in range(0,len(Dict[key])):
		#print "Searching "+str(i)+" ..."
		if Dict[key][i] in code:
			city = Dict['City/Airport'][i]
			country = Dict['Country'][i]
			print "Match found!"+" "+code+" = "+Dict[key][i]
			print "This is in "+city+", "+country	
			# if it already exits, then skip
			collection.update_one({'_id': doc['_id']}, {'$push': {'City/Airport': city}}, upsert = True)
			collection.update_one({'_id': doc['_id']}, {'$push': {'Country': country}}, upsert = True)
			collection.update_one({'_id':doc['_id']}, {'$push': {'IATA': Dict[key][i]}}, upsert = True)
			break
	
	percent = float(numer) / float(doc_count)
	print "Percent done: "+str(percent*100)+"%"		
	numer+=1
	
print "Finished."



