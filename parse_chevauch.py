
import gzip
import sys
import os
import collections


def parse_chevauch(deb, fin, pas):
	
	os.mkdir("/home/mazieres/outputs/japon_parse_chevauch_%d_%d_%d" % (deb, fin, pas))

	gauche = deb
#	print "gauche =", gauche
	canne = deb + (pas / 2)
#	print "canne =", canne
	droite = deb + pas
#	print "droite =", droite

	freq_ip_0 = {}
	freq_ip_1 = {}
	freq_ip = {}
	yx = {}

	for i in range(gauche, canne):

#		print "i =", i
#		myfile = gzip.open("/home/mazieres/data_test/out_%d.gz" % i, 'r')

		myfile = gzip.open("/home/mazieres/data_radar/japon/out_%d.gz" % i, 'r')
		djvu = set()

#		print myfile

		for line in myfile.readlines():

#			print ip
			ip = line.split()[0]
			if ip != '*' and ip not in djvu:
				djvu.add(ip)
				freq_ip_0[ip] = freq_ip_0.get(ip, 0) + 1

#	print "freq_ip_0 =", freq_ip_0		

#	gauche  = canne
#	print "gauche =", gauche
#	canne += (pas / 2)
#	print "canne =", canne

#	count = 1
#	a = 0
#	b = 0

	
	while droite <= fin:

		yx = {}

#		freq_ip = {}			
		 
#		if count % 2 != 0:
#			a = canne
#			print "a = canne =", a
#			b = droite
#			print "b = droite =", b

#		if count % 2 == 0:
#		gauche += (pas/2)
#		droite += (pas/2)
#			print "droite =", droite
#		canne += (pas/2)
#			a = gauche
#			print "a = gauche =", a
#			b = canne
#			print "b = canne =", b

		for i in range(canne, droite):

			myfile = gzip.open("/home/mazieres/data_radar/japon/out_%d.gz" % i, 'r')
#			myfile = gzip.open("/home/mazieres/data_test/out_%d.gz" % i, 'r')

			djvu = set()

			for line in myfile.readlines():

#				print line
				ip = line.split()[0]
				if ip != '*' and ip not in djvu:
					djvu.add(ip)
					freq_ip_1[ip] = freq_ip_1.get(ip, 0) + 1


#		print "freq_ip_1 =", freq_ip_1

#		freq_ip = freq_ip_0.copy()
#		freq_ip.update(freq_ip_1)

### http://bpaste.net/show/7033/ ###

		freq_ip = collections.defaultdict(int)
		for d in (freq_ip_0, freq_ip_1):
			for k, v in d.iteritems():
				freq_ip[k] += v

####################################

#		print "freq_ip =", freq_ip

		for ip in freq_ip:
			v = freq_ip[ip]
			yx[v] = yx.get(v, 0) + 1

		outfile = open("/home/mazieres/outputs/japon_parse_chevauch_%d_%d_%d/parse_%06d_%d.dat" % (deb, fin, pas, (droite-pas), droite), 'w')
#		print "Wrinting parse_chevauch_%d_%d ..." % ((droite - pas), droite)

		for app in yx:
			outfile.write("%d %d\n" % (app, yx[app]))
#			print "%d %d\n" % (app, yx[app])

		outfile.close()			
			
		freq_ip_0 = {}
		freq_ip_0 = freq_ip_1.copy()
		freq_ip_1 = {}
#		print "freq_ip_0 =", freq_ip_0 		
			
#		if count % 2 == 0:
		gauche += (pas / 2)
#		print "gauche =", gauche
		canne += (pas / 2)	
#		print "canne =", canne					
		droite += (pas / 2)
#		print "droite =", droite

#		count += 1

	
	print "Done."

parse_chevauch(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
