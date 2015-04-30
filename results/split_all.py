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

skip=0
for l in train:
	skip=skip+1

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
		out[j-length+15].write(line+str(val)+"\n")
	
for f in out:
	f.close()
