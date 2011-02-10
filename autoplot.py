import os
import sys
import glob

path_dir = os.path.abspath(sys.argv[1])

if os.path.isfile(path_dir):
	print "dir only, bro !"
	exit(1)


os.mkdir("%s/plots" % path_dir)

tex_file = open('%s/plots/main.tex' % path_dir, 'w')

tex_file.write('\\documentclass{article}\n')
tex_file.write('\\usepackage{graphicx}\n')
tex_file.write('\\begin{document}\n')

lst_dir = os.listdir(path_dir)

#lst_cum = glob.glob(


for each in lst_dir:

	plot_file = open('%s/plots/%s.plot' % (path_dir, each), 'w')

	plot_file.write('set term postscript eps enhanced\n')
	plot_file.write('set output \"%s/plots/%s.eps\"\n' % (path_dir, each))
	plot_file.write('plot \"%s/%s\"\n' % (path_dir, each))

	plot_file.close()

for each in glob.glob("%s/plots/*.plot" % path_dir):
#	print each
	os.system("gnuplot %s" % each)
	
	
lst_cum = glob.glob("%s/plots/*.cum.eps" % path_dir)
lst_cum.sort()
#print len(lst_cum)

lst_dat = glob.glob("%s/plots/*.dat.eps" % path_dir)
lst_dat.sort()
#print len(lst_dat)

lst_cum_norm = glob.glob("%s/plots/*.cum.norm.eps" % path_dir)
lst_cum_norm.sort()
#print len(lst_cum_norm)

lst_dat_norm = glob.glob("%s/plots/*.dat.norm.eps" % path_dir)
lst_dat_norm.sort()
#print len(lst_dat_norm)


tex_file = open('%s/plots/main.tex' % path_dir, 'a')

for each in range(len(lst_cum)):

	tex_file.write('\\includegraphics{%s}\n' % lst_cum[each])
	tex_file.write('\\includegraphics{%s}\n' % lst_dat[each]) 



#	if each % 5 == 0 and each != 0:
#		for i in range((each - 5), each):
#		tex_file.write('\\includegraphics{%s}\n' % lst_cum_norm[i])
#		tex_file.write('\\includegraphics[%s}



tex.file.write('\\end{document}\n')

tex_file.close()	






#for each in xrange(len(lst_cum)):
		
#	cum_file = open("%s", "a")
#	cum_file.write("", "")	


