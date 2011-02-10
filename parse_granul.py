import gzip
import sys
import os

deb = int(sys.argv[1])
fin = int(sys.argv[2]) 
pas = int(sys.argv[3])
granul = int(sys.argv[4])

gauche = deb
droite = deb + pas   

os.mkdir("/home/mazieres/outputs/enix_parse_granul_%d_%d_%d" % (deb, fin, pas))

count = 0

while droite <= fin :
	
	freq_ip = {}
	yx = {}

	for i in range(gauche, droite):
		myfile = gzip.open("/home/mazieres/data_radar/enix/out_%d.gz" % i, 'r')	

		djvu = set()
		
		for line in myfile.readlines():

			ip = line.split()[0]
			if ip != '*' and ip not in djvu: 
				djvu.add(ip)
				freq_ip[ip] = freq_ip.get(ip, 0) + 1

	for ip in freq_ip:
		v = freq_ip[ip]
		yx[v] = yx.get(v, 0) + 1	

	outfile = open("/home/mazieres/outputs/enix_parse_granul_%d_%d_%d/parse_granul_%06d_%d.dat" % (deb, fin, pas, gauche, droite),'w')
		
	for app in yx:
		outfile.write("%d %d\n" % (app, yx[app]))
		
	outfile.close()

	gauche += granul
	droite += granul



