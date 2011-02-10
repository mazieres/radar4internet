#!/bin/sh
#
# autocum.sh
# AM
#

if [ -f "$1" ]
then
	output_file="$(echo $1 | sed 's/.dat/.cum/')"
	touch $output_file 
	/bin/cat $1 | /usr/bin/sort -k1,1nr | /usr/bin/awk '{sum += $2; print $1, sum;}' > $output_file
fi

if [ -d "$1" ]
then
	for i in $1/*; do
		output_file="$(echo $i | sed 's/.dat/.cum/')"
		/usr/bin/touch $output_file
		/bin/cat $i | /usr/bin/sort -k1,1nr | /usr/bin/awk '{sum += $2; print $1, sum;}' > $output_file
	done
fi


