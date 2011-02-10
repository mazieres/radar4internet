import os
import sys
import glob

if not os.path.isdir(sys.argv[1]):
	print "dir only, bro ;)"
	exit(1)

lst_file = glob.glob("%s/*" % sys.argv[1])
lst_file.sort()

for each in lst_file:

	if os.path.isfile(each):

		myfile = open(each , 'r')
		norm_file = open("%s.norm" % each , 'w')
		col1_max = 0
		col2_max = 0
		count = 0

		for line in myfile.readlines():

			i = int(line.split()[0])
			j = int(line.split()[1])

			if i > col1_max:
				col1_max = i

			if j > col2_max:
				col2_max = j

		myfile.close()	
		myfile = open(each, 'r')

		for line in myfile.readlines():

			i = float(line.split()[0])	
			j = float(line.split()[1])
			norm_file.write("%f %f\n" % ((i/col1_max),(j/col2_max)))

		norm_file.close()

