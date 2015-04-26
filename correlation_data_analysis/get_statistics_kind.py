#this script file deletes all the columns except the kind columns
#this file is necessary to get some sort of statistics for the kind similarities..
#columns from 13-27 are the kind columns

import math

fileName = "../train.csv"
delim = ','

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

for i in range(15):
	mean.append(0)
	std.append(0)
	
for l in lines:
	words=l.split(delim)
	row=[]
		
	l = len(words)
	
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

#compute std. deviation for all kinds..
for i in range(15):
	for row in k:
		std[i] = std[i]+(row[i]-mean[i])*(row[i]-mean[i])
		
	#std[i] =math.sqrt(std[i]/n)
	std[i] =math.sqrt(std[i])
	
	
minCorr = 10000
maxCorr = -10000		

minTuple = ()
maxTuple = ()

sort = []

for i in range(15):
	for j in range(i+1, 15):
		corr = 0;
		for row in k:
			corr = corr + (row[i]-mean[i])*(row[j]-mean[j])
		corr = corr/(std[i]*std[j])
		
		if corr < minCorr:
			minCorr = corr
			minTuple = (i,j)
		if corr > maxCorr:
			maxCorr = corr
			maxTuple = (i, j)		
		
		if corr <= 0:
			sort.append((i,j,corr))
			#print "Correlation between ",kind_name[i]," and ",kind_name[j]," is ",corr

#sort the list..
for i in range(len(sort)):
	max_corr = 1000
	max_index=-1
	for j in range(i,len(sort)):
		if sort[j][2] < max_corr:
			max_corr = sort[j][2]
			max_index=j	 
	#swap i and max_index
	temp = sort[i]
	sort[i] = sort[max_index]
	sort[max_index] = temp
	
'''	
for s in sort:
	print "Correlation between ",kind_name[s[0]]," and ",kind_name[s[1]]," is ",s[2]
'''		
		
mean_sort=[]		
		
for i in range(15):
	mean_sort.append((i,mean[i]))		
	
#sort the mean values..
for i in range(len(mean_sort)):
	max_corr = -1000
	max_index=-1
	for j in range(i,len(mean_sort)):
		if mean_sort[j][1] > max_corr:
			max_corr = mean_sort[j][1]
			max_index=j	 
	#swap i and max_index
	temp = mean_sort[i]
	mean_sort[i] = mean_sort[max_index]
	mean_sort[max_index] = temp
	
		
for m in mean_sort:
	print "Mean for ",kind_name[m[0]]," is ",m[1]
		
#print "Minimum Correlation is ", minCorr, kind_name[minTuple[0]],"\t",kind_name[minTuple[1]] 
#print "Max correlation is ",maxCorr,kind_name[maxTuple[0]],"\t",kind_name[maxTuple[1]]
