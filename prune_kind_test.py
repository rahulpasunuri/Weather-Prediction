#fileName = "train.csv"
fileName = "test.csv"

print '@relation \'kind_pruned\''
print
#print '@attribute id numeric'
print '@attribute tweet string' 
print '@attribute city string'
print '@attribute \'Class\' {\'1\', \'2\', \'3\', \'4\', \'5\', \'6\'}'
print
print '@data'


id_file=open("ids_test.txt","w")

f = open(fileName, "r")
lines=f.readlines()
f.close()
#skip the header line
lines= lines[1:]

special = ['(', ')', '#', '$', '%', '*', '@', '!', "{", "}", ':', "=", '~', '\\', '/']
skip=0
te = ""

skip_list = [2626]

for l in lines:
	skip=skip+1
	#if skip>3000:
	#	break
	words = l.split(",")	
	id_num = words[0]
	#line = words[0].replace('"',"")+","
	line=""
	#get the tweet..
	i = l.find(",")
	l=l[i+2:]
	
	i= l.find("\"")		
	line=line+"\""+l[:i+1]
	line=line.replace(",","")
	line = line.replace("\"","")
	l=l[i+3:]
	
	i= l.find("\"")
	tata = l[:i+1].replace(",","")
	tata=tata.replace("\"","")
	#line=line+"\""+tata+", "
	l=l[i+3:]
	
	line = "\""+line+"\""+","+"\""+tata+"\""+","
	#print line
	#continue
	#case-sensitive approach
	line=line.lower()
	for c in special:
		line = line.replace(c, '')
	line = line+"?"
	
	if skip not in skip_list:
		try:
			line=line.replace("\n","")
			line.decode('utf-8')
			print line
			id_file.write(id_num.replace("\"","")+"\n")
		except UnicodeError:
			#print line
			continue
		
	#te = line.replace("\n","")

id_file.close()
