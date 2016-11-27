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
SNR=("-3.0" "0.0" "3.0" "10.0")
ndata=(64 128 256 512 1024 2048 4096)

mkdir -p "samples"

for snr in ${SNR[*]} ; do
	for sample_quant in ${ndata[*]} ; do
		python  psk_sample_generator.py $snr $ntrials $sample_quant
		mv samples_"$snr"db_"$sample_quant"_"$ntrails"_signal.npy samples
		mv samples_"$snr"db_"$sample_quant"_"$ntrails"_noise.npy samples
		mv samples_"$snr"db_"$sample_quant"_"$ntrails"_sn.npy samples
	done
done

