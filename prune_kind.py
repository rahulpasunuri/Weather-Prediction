fileName = "train.csv"
#fileName = "test.csv"

f = open(fileName, "r")
lines=f.readlines()
f.close()
#skip the header line
lines= lines[1:]

for l in lines:
	words = l.split(",")	
	line = ""
	#get the tweet..
	i = l.find(",")
	l=l[i+2:]
	
	i= l.find("\"")		
	line=line+"\""+l[:i+1]+", "
	
	l=l[i+3:]
	
	i= l.find("\"")
	line=line+"\""+l[:i+1]+", "
	l=l[i+3:]
	
	i= l.find("\"")
	line=line+"\""+l[:i+1]+", "
	
	length = len(words)
	#get the kind values..
	for i in range(length-24,length):
		if i != length-1:
			line = line + words[i].replace("\"","")+", "
		else:
			line = line+words[i].replace("\"","")
	print line.replace("\n","") 
	
