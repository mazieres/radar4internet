#!/bin/sh

if [ -d "$1" ]
then
	for i in $1/*.cum; do
##		head_cum_file=$i.head
##		/usr/bin/touch $head_cum_file
		nb_l=$(wc -l $i | gawk '{print $1}')
		nb_l_head=$((($nb_l * 10)/100))
		head -n$nb_l_head $i > $i.10pc-head
	done

#	for i in $1/*.cum.norm; do
#		nb_l=$(wc -l $i | gawk '{print $1}')
#		nb_l_head=$((($nb_l * 10)/100))
#		head -n$nb_l_head $i > $i.10pc-head
#	done
fi


		
