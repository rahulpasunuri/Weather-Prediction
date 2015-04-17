#this script file deletes all the columns except the kind columns
#this file is necessary to get some sort of statistics for the kind similarities..
#columns from 13-27 are the kind columns

import math

fileName = "train.csv"
delim = ','


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
		
	std[i] =math.sqrt(std[i]/n)
	
print std
	
minCorr = 10000
maxCorr = -10000		

for i in range(15):
	for j in range(i+1, 15):
		corr = 0;
		for row in k:
			corr = corr + (row[i]-mean[i])*(row[j]-mean[j])
		corr = corr/((n-1)*std[i]*std[j])
		
		if corr < minCorr:
			minCorr = corr
		if corr > maxCorr:
			maxCorr = corr
					
		print "Correlation between kind ",i,"kind ",j,"is ",corr
		
print "Minimum Correlation is ", minCorr
print "Max correlation is ",maxCorr
