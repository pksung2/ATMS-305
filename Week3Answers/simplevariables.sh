#!/bin/bash

declare -f var1 var2

echo Input variable 1
read var1
echo
echo Input variable 2
read var2
echo
if [[ $var1 -lt $var2 ]];
then
	echo "Your output is $((var1 + $var2))"
else
	echo You stink.
fi

echo
