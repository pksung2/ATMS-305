#!/bin/bash

echo  Where do you think you\'re going?
read -p 'Your Answer: ' $answer

if [ $answer == 'home' ]
then
	echo Good.
else
	echo I'm coming with.
fi

