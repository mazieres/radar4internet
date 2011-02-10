#
# this script parses and hashes "out" files of radar
# AM 20/05/2010
#

import gzip
import sys
import os

#os.system('rm /home/mazieres/outputs/parse_hash_*')



deb = int(sys.argv[1])
fin = int(sys.argv[2]) 
pas = int(sys.argv[3])

gauche = deb
droite = deb + pas   

os.mkdir("/home/mazieres/outputs/japon_parse_hash_%d_%d_%d" % (deb, fin, pas))

count = 0

while count <= ((fin - deb) / pas):
	
	freq_ip = {}
	yx = {}

	for i in range(gauche, droite):
#		myfile = gzip.open("/home/mazieres/data_test/out_%d.gz" % i, 'r')
		myfile = gzip.open("/home/mazieres/data_radar/japon/out_%d.gz" % i, 'r')	

		djvu = set()
		
		for line in myfile.readlines():

			ip = line.split()[0]
			if ip != '*' and ip not in djvu: 
				djvu.add(ip)
				freq_ip[ip] = freq_ip.get(ip, 0) + 1

	for ip in freq_ip:
		v = freq_ip[ip]
		yx[v] = yx.get(v, 0) + 1	

	outfile = open("/home/mazieres/outputs/japon_parse_hash_%d_%d_%d/parse_hash_%06d_%d.dat" % (deb, fin, pas, gauche, droite),'w')
		
	for app in yx:
		outfile.write("%d %d\n" % (app, yx[app]))
		
	outfile.close()

	gauche = droite
	droite += pas
	count += 1

print "Done, %d hashes were parsed" % count


