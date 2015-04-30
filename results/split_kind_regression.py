train = open("../train.csv","r").readlines()
train = train[1:]
special = ['(', ')', '#', '$', '%', '*', '@', '!', "{", "}", ':', "=", '~', '\\']
out=[]
for i in range(15):
	f = open("individual/train_"+str(i)+".arff","w")
	out.append(f)


#add the arff headers..
for f in out:
	f.write('@relation \'kind_pruned\'\n\n')	
	#f.write('@attribute id numeric\n') 
	f.write('@attribute tweet string\n') 
	f.write('@attribute city string\n')
	f.write('@attribute Class numeric\n\n')
	f.write('@data\n')


cat = [ 
[5,9,15],
[8,11],
[1,2,10],
[6,12,14],
[3,4,13],
[7]
]

'''
1) humid+wind+other

2) ice+snow

3) clounds+rain+cold

4) storms+hurricane+tornado

5) dry+sun+hot

6) I can't tell

'''
skip=0
count_outliers=0
for l in train:
	skip=skip+1
	#if skip>100:
	#	break
	words = l.split(",")	
	#line = words[0].replace("\"","")
	line=""
	#get the tweet..
	i = l.find(",")
	l=l[i+2:]
	
	i= l.find("\"")		
	line=line+"\""+l[:i+1]+", "
	
	l=l[i+3:]
	
	i= l.find("\"")
	line=line+"\""+l[:i+1]+", "
	l=l[i+3:]
	
	#skip city information for now..
	#i= l.find("\"")
	#line=line+"\""+l[:i+1]+", "
	
	#case-sensitive approach
	line=line.lower()
	for c in special:
		line = line.replace(c, '')
	
	length = len(words)
	totalMax = 0
	#get the kind values..
	cat_max = [0 for i in range(6)]	
	cat_avg = [0 for i in range(6)]	
	kind=[]
	for j in range(length-15,length):
		val = float(words[j].replace("\"",""))
		kind.append(val)
		isFound=False		
		for i in range(len(cat)):						
			if j-length+16 in cat[i]:				
				cat_avg[i] = cat_avg[i]+val
				isFound=True
				if val > cat_max[i]:
					cat_max[i] =val
					if val > totalMax:
						totalMax = val		
				break

	max_avg = 0
	winner = -1
	for i in range(len(cat)):
		cat_avg[i] = cat_avg[i]/len(cat[i])
		if max_avg < cat_avg[i] and cat_max[i]==totalMax:
			max_avg=cat_avg[i] 
	
	
	count =0
	for i in range(len(cat)):
		if cat_max[i] == totalMax:
			count = count+1
	isOutlier = False	
	
	if count==1:	
		for i in range(len(cat)):
			if cat_max[i] == totalMax:
				winner = i+1
				count = count+1
		
	else:
		count_outliers=0
		
		for i in range(len(cat)):
			if cat_avg[i] == max_avg and cat_max[i]==totalMax:
				winner = i+1
				count=count+1
		
			if count!=1:
				#count_outliers=count_outliers+1		
				isOutlier = True
	
	
	if isOutlier == False:		
		for c in cat[winner-1]:
			#print line,kind[c-1]
			out[c-1].write(line+str(kind[c-1])+"\n")

for f in out:
	f.close()
