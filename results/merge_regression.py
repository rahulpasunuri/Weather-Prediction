reg=[]
orig = open("../arff/ids_test.txt","r")
val={}
act=[]

mean_sent = "0.05,0.24,0.31,0.23,0.17,0.73,0.09,0.13,0.05"

mean_string = "0.02,0.1,0.01,0.12,0.04,0.0,0.28,0.0,0.08,0.11,0.04,0.15,0.15,0.02,0.05"
mean = mean_string.split(',')

other = open("../varsha.csv","r").readlines()
other_val={}
print other[0]
other=other[1:]
for l in other:
	words=l.strip().split(',')
	id_num = words[0].strip()
	other_val[id_num] = ",".join(words[:10])

for i in range(15):
	f = open("individual/test_"+str(i)+".arff","r")
	act.append(f)

for i in range(15):
	#f = open("regression_values/res"+str(i)+".csv","r")
	f = open("regression_values/res"+str(i)+".csv","r")
	reg.append(f)
	
lines = orig.readlines()

for l in lines:
	id_num=l.split(',')[0].replace('"',"")
	val[id_num.strip()] = [0 for i in range(15)]
	

for i in range(15):
	pred = reg[i].readlines()
	pred=pred[1:]
	act_lines = act[i].readlines()
	act_lines = act_lines[7:]	
	
	#print len(act_lines),len(pred)
	#continue
	for j in range(len(act_lines)):
		id_num = act_lines[j].split(',')[0].strip()
		pred_val = pred[j].split(',')[2]
		
		if pred_val == '?':
			pred_val= str(mean[i])#TODO
			#pred_val='0'
			
		val[id_num][i]=float(pred_val)

curr=10
#0->236
#1->236
#2->236

for id_num in other_val:
	if id_num in val:
		val_str = [str(x) for x in val[id_num]]
		#now_temp = ",".join(['0' for i in range(9)])
		now_temp=mean_sent
		#print id_num+",",",".join(val_str) 
		#print id_num+","+now_temp,",",",".join(val_str) 
		
		temp = [x for x in mean]
		temp[curr] = val[id_num][curr]
		print other_val[id_num],",",",".join([str(x) for x in temp]) 
		#print other_val[id_num],",",",".join(val_str) 
	else:
		temp=",".join(["0" for i in range(15)])		
		#print id_num,",",mean_string
		print other_val[id_num],",",mean_string

orig.close()
for f in reg:
	f.close()
	

