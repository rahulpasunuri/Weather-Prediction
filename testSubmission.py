def failed(l):
	print "Some thing Failed in: ", l
	exit()

fileName = "sampleSubmission.csv"

f = open(fileName, "r")
lines = f.readlines()
f.close()

skipLine = True

for l in lines:
	#skip the first line which just has the column names..
	if skipLine == True:
		skipLine = False
		continue
		
	w = l.split(',')
	
	if len(w) != 25:
		failed(l)
	
	#get s's
	s1 = float(w[1])
	s2 = float(w[2])
	s3 = float(w[3])
	s4 = float(w[4])
	s5 = float(w[5])
	
	#get w's
	w1 = float(w[6])
	w2 = float(w[7])
	w3 = float(w[8])
	w4 = float(w[9])
	
	if s1+s2+s3+s4+s5 !=1:
		failed(l)
	
	if w1+w2+w3+w4 !=1:
		failed(l)
	 
	
	
	
