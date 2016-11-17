#! /bin/bash

############################
# PURPOSE: 
#	This script produces a directory that contains the pickled files 
# 		containing the samples of input signal, noise, and signal+noise  for a
# 		signal

# DEPENDENCIES:
# 	This script invokes psk_sample_generator.py 

# DATE:
# 	Nov 17 2016
############################

NOISE_AMP=(.01 .005 .0025 .00125) # produces SNR=(-3 0 3 10)
ntrials=(2 4 16 64 128 256 512 1024 2048 4096)

for noise_amp in ${NOISE_AMP[*]} ; do
	for trial in ${ntrials[*]} ; do
		python  psk_sample_generator.py $noise_amp 2048 $trial
	done
done

