pred = open("category_predictions.csv", "r").readlines()
pred=pred[1:]#skip header..

prune = open("../arff/kind_test.arff","r").readlines()
prune = prune[7:]

ids = open("../arff/ids_test.txt","r").readlines()

out=[]
for i in range(15):
	f = open("individual/test_"+str(i)+".arff","w")
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

count=0
for l in pred:
	l=l.strip()
	words = l.split(',')
	p = words[2]
	p = int(p.split(':')[0])
	
	l1=prune[count].strip()
	words = l1.split(",")	
	id_num = ids[count]
	
	line=words[0]+","+words[1]+","
	line.replace(".", " ")
	try:		
		line.decode('utf-8')
	except:
		count=count+1
		continue
		
	for c in cat:
		if p in c:			
			for index in c:
				string = id_num.strip()+","+line+"?\n"
				#string = line+"?\n"																				
				out[index-1].write(string)
				
	count=count+1


for f in out:
	f.close()
