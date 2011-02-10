import gzip
import sys

freq_ip = {}
yx = {}


for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
	myfile = gzip.open("/home/mazieres/data_radar/test/out_%d.gz" % i, 'r')
	
	djvu = set()
	
	for line in myfile.readlines():

		ip = line.split()[0]
		if ip != '*' and ip not in djvu: 
			djvu.add(ip)
			freq_ip[ip] = freq_ip.get(ip, 0) + 1

print freq_ip

'''
for ip in freq_ip:
	v = freq_ip[ip]
	yx[v] = yx.get(v, 0) + 1	

outfile = open("/home/mazieres/outputs/test_parse_all.dat", 'w')

for app in yx:
	outfile.write("%d %d\n" % (app, yx[app]))

outfile.close()
'''
