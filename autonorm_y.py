import os
import sys
import glob
import shutil

path = os.path.abspath(sys.argv[1])

if not os.path.isdir(path):
	print "dir only, bro ;)"
	exit(1)


lst_file = glob.glob("%s/*.dat" % path)
lst_file.sort()

os.mkdir("%s/video" % path)
os.mkdir("%s/video/plots" % path)
os.mkdir("%s/video/pngs" % path)

# NORM

for each in lst_file:

	if os.path.isfile(each):

		myfile = open(each , 'r')
		norm_file = open("%s.norm" % each , 'w')
		y_max = 0

		for line in myfile.readlines():

			y = int(line.split()[1])
				
			if y > y_max:
				y_max = y

		myfile.close()	
		myfile = open(each, 'r')

		for line in myfile.readlines():
			
			x = float(line.split()[0])
			y = float(line.split()[1])
			norm_file.write("%d %f\n" % (x , (y/y_max)))

	norm_file.close()

lst_normfile = glob.glob("%s/*.dat.norm" % path)
lst_normfile.sort()
#print lst_normfile

# ILLUSTRATION

allfile = open("%s/video/plots/all" % path, 'w')
allfile.write("100 0.7\n")
allfile.write("400 0.7\n")
allfile.close()

eventfile = open("%s/video/plots/event" % path, 'w')
eventfile.write("385 0.7\n")
eventfile.write("365 0.7\n")
eventfile.close()

# PLOT

for each in lst_normfile:

	if os.path.isfile("%s/video/plots/lefteye" % path):
		os.remove("%s/video/plots/lefteye" % path)

	if os.path.isfile("%s/video/plots/righteye" % path):
		os.remove("%s/video/plots/righteye" % path)
	
	file_name = each.split('/')[-1]
	lefteye = float(file_name.split('_')[2])
	righteye = file_name.split('_')[3]
	righteye = float(righteye.split('.')[0])

	lefteyefile = open("%s/video/plots/lefteye-%s" % (path, file_name), 'w')
	lefteyefile.write("%f 0.6\n" % (-(((lefteye-150)/2)-400)))
	lefteyefile.write("%f 0.8\n" % (-(((lefteye-150)/2)-400)))	
	lefteyefile.close()

	righteyefile = open("%s/video/plots/righteye-%s" % (path, file_name), 'w')
	righteyefile.write("%f 0.6\n" % (-(((righteye-150)/2)-400)))
	righteyefile.write("%f 0.8\n" % (-(((righteye-150)/2)-400)))
	righteyefile.close()

	plotfile = open("%s/video/plots/%s.plot" % (path , file_name), 'w')
	plotfile.write("set xlabel \"# rounds\"\n")
	plotfile.write("set ylabel \"# IPs\"\n")
	plotfile.write("set title \"\"\n")
	plotfile.write("plot \"%s\" noti\n" % each)
	plotfile.write("replot \"%s/video/plots/all\" w l noti\n" % path)
	plotfile.write("replot \"%s/video/plots/event\" w l lw 4 noti\n" % path)
	plotfile.write("replot \"%s/video/plots/lefteye-%s\" w l lw 2 lt 1 noti\n" % (path, file_name))
	plotfile.write("replot \"%s/video/plots/righteye-%s\" w l lw 2 lt 1 noti\n" % (path, file_name))
	plotfile.write("set terminal png\n")
	plotfile.write("set output \"%s/video/pngs/%s.png\"\n" % (path , file_name.split('.')[0]))	
	plotfile.write("replot\n")
	plotfile.close()

lst_plotfile = glob.glob("%s/video/plots/*.plot" % path)
lst_plotfile.sort()

for each in lst_plotfile:

	os.system("gnuplot %s" % each)

# ANTE

count = 0
while count <= 25:
	shutil.copy("%s/ante.png" % path, "%s/video/pngs/zante%06d.png" % (path, count))
	count += 1



# VIDEO

lst_vidfile = glob.glob("%s/video/pngs/*.png" % path)
lst_vidfile.sort()
lst_vidfile.reverse()

vidfile = open("%s/video/lst_pngs.txt" % path, 'w')

for each in lst_vidfile:
	
	vidfile.write("%s\n" % each)

vidfile.close()

os.system("mencoder mf://@%s/video/lst_pngs.txt -mf w=640:h=480:fps=4:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -oac copy -o %s/video/output.avi" % (path, path))

print "Done."
