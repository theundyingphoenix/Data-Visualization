import re, json
import ipapi

data = []

# "/home/apluser/Desktop/data/data.json"
for line in open("/home/apluser/Desktop/data/data1.json", 'r'):
	json.loads(line)
	edit = line.replace('[',' ')
	edit = edit.replace(']',' ')
	data.append(edit)


print("Adding to new JSON file!")	
with open("/home/apluser/Desktop/data/tt.json", 'w') as outfile:
	for i in range(0,len(data)):
		ser_data = json.loads(data[i])
		json.dump(ser_data,outfile)
	
