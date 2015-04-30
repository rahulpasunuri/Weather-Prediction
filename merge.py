f1=open("varsha.csv","r")

lines= f1.readlines()
f1.close()

temp = ",".join(['0' for i in range(15)])
print lines[0].strip()
lines=lines[1:]

for l in lines:
	words=l.strip().split(',')
	print ",".join(words[:10]),",","0.02,0.1,0.01,0.12,0.04,0.0,0.28,0.0,0.08,0.11,0.04,0.15,0.15,0.02,0.05"
