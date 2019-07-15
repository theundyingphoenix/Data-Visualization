
import requests
import lxml.html as lh
import pandas as pd

def str_bracket(word):
    '''Add brackets around second term'''
    list = [x for x in word]
    for char_ind in range(1, len(list)):
        if list[char_ind].isupper():
            list[char_ind] = ' '+list[char_ind]
        fin_list = ''.join(list).split(' ')
        length = len(fin_list)
        if length>1:
            fin_list.insert(1,'(')
            fin_list.append(')')
        return ' '.join(fin_list)

def str_break(word):
    '''Break strings at upper case'''
    list = [x for x in word]
    for char_ind in range(1, len(list)):
        if list[char_ind].isupper():
            list[char_ind] = ' ' + list[char_ind]
        fin_list = ''.join(list).split(' ')
    return fin_list



url='https://www.nationsonline.org/oneworld/IATA_Codes/airport_code_list.htm'

#Create a handle, page, to handle the contents of the website
page = requests.get(url)

#Store the contents of the website under doc
doc = lh.fromstring(page.content)

#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

print [len(T) for T in tr_elements[:12]]
 
tr_elements = doc.xpath('//tr')

#Create empty list
col=[]
i=0
l = ['','City/Airport', 'Country', 'IATA code']



for t in tr_elements[1]:
    i+=1
    name = l[i]
    print '%d:"%s"'%(i,name)
    col.append((name,[]))
    

#For each row, store each first element (header) and an empty list
# for t in tr_elements[0]:
#     i+=1
#     name=t.text_content()
#     print '%d:"%s"'%(i,name)
#     col.append((name,[]))


#Since first row is the header, data is stored on the second row onwards

# num_breaks = 0
# for t in range(1,len(tr_elements)):
#     T = tr_elements[t]
#     line = ""
#     for tt in T.iterchildren():
#         data = tt.text_content()
#         if len(data)<2 or 'XYZ' in data:
#             num_breaks+=1
#             break
#         print data
# print num_breaks
num_breaks = 0
for j in range(1,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    
    #If row is not of size 10, the //tr data is not from our table 
    if len(T)!=3:
        num_breaks+=1
        continue
    
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        #Check if row is empty
        print data    
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1
print num_breaks
print [len(C) for (title,C) in col]        

Dict = {title:column for (title,column) in col}
df = pd.DataFrame(Dict)

#print df.head()

#df['Name']=df['Name'].apply(str_bracket)
#df['Type']=df['Type'].apply(str_break)

#print df.head()

df.to_json('Codes.json')


df = pd.read_json('Codes.json')
df = df.set_index(['City/Airport'])
#print df.tail()