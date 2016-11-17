#! /bin/bash

############################
# PURPOSE: 
#	This script produces a directory that contains the pickled files 
# 		containing the 256 samples of input signal, noise, and signal+noise  for a
# 		signal

# DEPENDENCIES:
# 	This script invokes psk_sample_generator.py 

# DATE:
# 	Nov 17 2016
############################
ntrials=128
NOISE_AMP=(.01 .005 .0025 .00125) 
SNR=(-3 0 3 10)
ndata=(64 128 256 512 1024 2048 4096)

for noise_amp in ${NOISE_AMP[*]} ; do
	for sample_quant in ${ndata[*]} ; do
		echo "create_picked.sh: ${SNR[i]}"
		python  psk_sample_generator.py $noise_amp $ntrials $sample_quant
	done
done

