#!/bin/sh
#To compile these the machiner library as a dynamic shared library, do

gcc -c -Wall -Werror -fpic state.c 
gcc -shared -o libstate.so state.o

# to comile the main program for basic tests

gcc -Wall -o mains mains.c -L ./ -lstate

# Remember to set the LD_LIBRARY_PATH so that loader can find the location of
# share library for proper execution of mains.
# gcc will generate several warnnigs for the main program. I just wrote it to
# perform some basic tests and I knew what I was doing so I ignored these warnings.

export LD_LIBRARY_PATH=`pwd`:$LD_LIBRARY_PATH
