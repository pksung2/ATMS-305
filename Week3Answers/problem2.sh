#!/bin/bash

# Create a bash script which will take a filename as its first 
# argument and create a Universal Time Coordinate (UTC) dated copy of 
# the file. eg. if our file was named file.txt it would create a copy 
# such as 2017-01-30_22:45:00_netID.txt, where the date and your 
# netID and time are determined from the current time automatically. 
# (To achieve this you will probably want to play with command 
# substitution, create variables from output from the command date)

echo Give me a file.
read thing
if [ -e $thing ]
then
	date1=`date +%Y-%m-%d`
	date2=`date +%H:%M:%S`
#	echo $date1
#	echo $date2
	echo "$date1"_"$date2"_"$USER".txt
	cp $thing "$date1"_"$date2"_"$USER".txt
else
	echo That is not an existing file. Try again.
fi
