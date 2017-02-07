#!/bin/bash

test1=Hello World
echo $test1

world="New Jersey"
test1="Hello $world"
echo $test1

world="New Jersey"
test1='Hello $world'
echo $test1

$ ls
README.mdSYLLABUS.mdHOMEWORK.md
$ files=$( ls )
$ echo $files
