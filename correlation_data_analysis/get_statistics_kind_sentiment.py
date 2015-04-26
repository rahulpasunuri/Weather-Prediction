#this script file deletes all the columns except the kind columns
#this file is necessary to get some sort of statistics for the kind similarities..
#columns from 13-27 are the kind columns

import math

fileName = "train.csv"
delim = ','

sent_name = {}
sent_name[0] = "I can't tell"
sent_name[1] = "Negative"
sent_name[2] = "Neutral"
sent_name[3] = "Positive"
sent_name[4] = "Not Related"

kind_name = {}
kind_name[0] = "clouds"
kind_name[1] = "cold"
kind_name[2] = "dry"
kind_name[3] = "hot"
kind_name[4] = "humid"
kind_name[5] = "hurricane"
kind_name[6] = "I can't tell"
kind_name[7] = "ice"
kind_name[8] = "other"
kind_name[9] = "rain"
kind_name[10] = "snow"
kind_name[11] = "storms"
kind_name[12] = "sun"
kind_name[13] = "tornado"
kind_name[14] = "wind"

f= open(fileName, 'r')

lines=f.readlines()
lines=lines[1:] #skip the first line(header).

f.close()

k=[]

#below vars hold the mean and std. deviation of the kind variables..
mean = []
std=[]

sent = []
sent_mean =[]
sent_std=[]
for i in range(5):
	sent_mean.append(0)
	sent_std.append(0)
	
for i in range(15):
	mean.append(0)
	std.append(0)
	
for l in lines:
	words=l.split(delim)
	row=[]
	s=[]
	l = len(words)
	
	for i in range(l-24,l-19):
		words[i] = words[i].replace("\"","")
		s.append(float(words[i]))
		sent_mean[i-l+24] = sent_mean[i-l+24]+float(words[i])
	sent.append(s)
					
	#get the last 15 columns..	
	for i in range(l-15,l):
		words[i] = words[i].replace("\"","")
		row.append(float(words[i]))
		mean[i-l+15] = mean[i-l+15]+float(words[i])
			
	k.append(row)
	
n=len(k)

#compute mean of all kinds.
for i in range(15):
	mean[i]=mean[i]/n
	
for i in range(5):
	sent_mean[i]=sent_mean[i]/n

#compute std. deviation for all kinds..
for i in range(15):
	for row in k:
		std[i] = std[i]+(row[i]-mean[i])*(row[i]-mean[i])
		
	#std[i] =math.sqrt(std[i]/n)
	std[i] =math.sqrt(std[i])
	
for i in range(5):
	for row in 	sent:
		sent_std[i] = std[i]+(row[i]-sent_mean[i])*(row[i]-sent_mean[i])
	sent_std[i] =math.sqrt(std[i])

minCorr = 10000
maxCorr = -10000		

minTuple = ()
maxTuple = ()

sort = []

for snum in range(5):
	sort=[]
	for j in range(15):
		corr = 0;
		for r in range(n):
			corr = corr + (sent[r][snum]-sent_mean[snum])*(k[r][j]-mean[j])
		corr = corr/(sent_std[snum]*std[j])
		
		sort.append((j,corr))
	
	#sort the list..
	for i in range(len(sort)):
		max_corr = -1000
		max_index=-1
		for j in range(i,len(sort)):
			if sort[j][1] > max_corr:
				max_corr = sort[j][1]
				max_index=j	 
		#swap i and max_index
		temp = sort[i]
		sort[i] = sort[max_index]
		sort[max_index] = temp
		
	#print the sorted list
	for s in sort:
		print "Correlation between ",sent_name[snum]," and ",kind_name[s[0]]," is ",s[1] 
	print
	print "-"*40
	print
	
