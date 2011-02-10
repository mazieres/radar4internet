#!/bin/bash
#
# autoplot.sh
# AM
#

if [ -f "$1" ]
then
	echo "set term postscript eps enhanced" > $1.plot
	echo "set output \"$1.eps\"" >> $1.plot
	echo "set title \"$1\"" >> $1.plot
	echo "plot \"$1\"" >> $1.plot
	
	gnuplot $1.plot &
fi

if [ -d "$1" ]
then

	mkdir $PWD/$1plots

	echo "\\documentclass{article}" > $1/plots/main.tex
	echo "\\usepackage{graphicx}" >> $1/plots/main.tex
	echo "\\begin{document}" >> $1/plots/main.tex
	
	for i in $1*.dat $1*.cum; do

		if [ -f "$i" ]
		then
			echo "set term postscript eps enhanced" > $i.plot
			echo "set output \"$PWD/$i.eps\"" >> $i.plot
			echo "plot \"$PWD/$i\"" >> $i.plot
	
			mv $i.plot $1/plots/
	
		fi

	done

#
#	for i in $1*.norm; do
#
#		if [ -f "$i" ]
#		then
#			if [ "$((pouet % 5))" = 0 ]
#			then
#
#			fi
#
#		((pouet++))	
#		fi		
#

	for i in $1/plots/*.plot; do

		gnuplot $i

	done
	
	mv $1/*.eps $1/plots/

	cd $1plots

	for i in ./*.eps; do		
		
		echo "" >> main.tex	
		echo "\includegraphics{$i}" >> main.tex		
		echo "" >> main.tex
		echo "$(echo "$1plots/$i" | sed 's/_/\\_/g' | sed 's/\.\///g')">> main.tex
		echo "" >> main.tex
	done

	echo "\\end{document}" >> main.tex

	latex main.tex


fi
