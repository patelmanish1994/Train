#Program to fetch the data of the trains
#IT WORKS FINE ON PYTHON 3.4 and above


import bs4 as bs
import urllib.request

import sys
link=[]

for i in range(0,6):
	l="https://www.cleartrip.com/trains/list?page="+str(i)
	link.append(l)
r=[]
def fetch_data(link):
	
	i=0
	thepage=urllib.request.urlopen(link).read()
	data=bs.BeautifulSoup(thepage,"lxml")
	
	for table in data.findAll("tr"):
		trains=""	
		for data in table.findAll("td"):			
			trains=trains+" "+data.text+" " # one cell data in string format
			
		i+=1
		print(trains)
	
	r.append(i)
	
for i in range(1,6):
	
	fetch_data(link[i])
	
print("Operation Complete")

print("total train details fetched:",sum(r))










	
