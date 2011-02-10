#
# this script parses and hashes "out" files of radar
# AM 20/05/2010
#

import gzip
import sys
import os


def parse_add(deb, fin, pas):

	os.mkdir("/home/mazieres/outputs/japon_parse_add_%d_%d_%d" % (deb, fin, pas))

	gauche = deb
	droite = deb + pas

	chrono = 0
	
	freq_ip = {}
#	yx = {}

	for i in range(deb, fin+1):
#		print i	
		myfile = gzip.open("/home/mazieres/data_radar/japon/out_%d.gz" % i, 'r')
#		myfile = gzip.open("/home/mazieres/data_radar/japon/out_%d.gz" % i, 'r')

		djvu = set()
		
		for line in myfile.readlines():
#			print line
			ip = line.split()[0]
			if ip != '*' and ip not in djvu: 
				djvu.add(ip)
				freq_ip[ip] = freq_ip.get(ip, 0) + 1

		myfile.close()

#		print "Passe", i
#		for ip in freq_ip:
#			print ip, freq_ip[ip]


		if (i-deb) % pas == pas-1:

		#	print i
			yx = {}

			for ip in freq_ip:
				v = freq_ip[ip]
				yx[v] = yx.get(v, 0) + 1	

			outfile = open("/home/mazieres/outputs/japon_parse_add_%d_%d_%d/parse_hash_%06d.dat" % (deb, fin, pas, i),'w')

		
		
			for app in yx:
				outfile.write("%d %d\n" % (app, yx[app]))
		
			outfile.close()

		if (i-deb) % pas != pas-1 and i == fin:

			yx = {}	
			for ip in freq_ip:
				v = freq_ip[ip]
				yx[v] = yx.get(v, 0) + 1

			outfile = open("/home/mazieres/outputs/japon_parse_add_%d_%d_%d/parse_hash_%06d.dat" % (deb, fin, pas, i), 'w')	

			for app in yx:
				outfile.write("%d %d\n" % (app, yx[app]))

			outfile.close()
	

	print "Done."

parse_add(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))

