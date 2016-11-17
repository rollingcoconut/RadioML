#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Nov  9 21:56:48 2016
##################################################
# PURPOSE: This script produces pickled files  each containing three arrays (signal, noise,
#           input signal+noise) that are samples of a PSK signal with AWGN

# USAGE: ./psk_sample_generator.py noise_amp no_trials 
# DATE: Nov 17, 2016
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy
import time, sys, argparse
import pickle
    
class top_block(gr.top_block):

    def __init__(self, noise_amp, ndata):
        gr.top_block.__init__(self, "Top Block")

        ##################################################
        # Variables
        ##################################################
        self.signal_gain = signal_gain = 0.01
        self.samp_rate = samp_rate = 32000
        self.noise_amplitude = noise_amplitude = noise_amp  #noise_amplitude = noise_amp 
        self.ndata =  ndata 

        ##################################################
        # Blocks
        ##################################################
        self.digital_psk_mod_0 = digital.psk.psk_mod(
          constellation_points=4,
          mod_code="gray",
          differential=True,
          samples_per_symbol=2,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.s2v_signal = blocks.stream_to_vector(gr.sizeof_gr_complex, self.ndata)
        self.s2v_noise = blocks.stream_to_vector(gr.sizeof_gr_complex, self.ndata)
        self.s2v_sn = blocks.stream_to_vector(gr.sizeof_gr_complex, self.ndata)
        self.blocks_probe_signal_and_noise = blocks.probe_signal_vc(self.ndata)
        self.blocks_probe_noise_only = blocks.probe_signal_vc(self.ndata)
        self.blocks_probe_signal_only = blocks.probe_signal_vc(self.ndata)       
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_vcc((signal_gain, ))
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, 1000)), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noise_amplitude, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.analog_noise_source_x_0, 0), (self.s2v_noise, 0), (self.blocks_probe_noise_only, 0))    
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.s2v_sn, 0), (self.blocks_probe_signal_and_noise, 0))    
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_add_xx_0, 0))   
        self.connect((self.blocks_multiply_const_vxx_3, 0),  (self.s2v_signal, 0), (self.blocks_probe_signal_only, 0)) 
        self.connect((self.blocks_throttle_0, 0), (self.digital_psk_mod_0, 0))    
        self.connect((self.digital_psk_mod_0, 0), (self.blocks_multiply_const_vxx_3, 0))    

    def get_signal_gain(self):
        return self.signal_gain

    def set_signal_gain(self, signal_gain):
        self.signal_gain = signal_gain
        self.blocks_multiply_const_vxx_3.set_k((self.signal_gain, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_noise_amplitude(self):
        return self.noise_amplitude

    def set_noise_amplitude(self, noise_amplitude):
        self.noise_amplitude = noise_amplitude
        self.analog_noise_source_x_0.set_amplitude(self.noise_amplitude)


def main(top_block_cls=top_block, options=None):
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("noise_amp", help="amplitude of noise, ex. 0.01. Signal gain is 0.01, and sample rate is 3200", type=float)
    parser.add_argument("ndata", help="number of consecutive samples collected at a time, ex. 2048", type=int)
    parser.add_argument("ntrials", help="number of trials, ex. 2", type=int)
    args = parser.parse_args()

    tb = top_block_cls(args.noise_amp, args.ndata)
    tb.start()

    try:
        ntrials=args.ntrials
        
        noise_matrix = numpy.ndarray(shape=(ntrials, tb.ndata), dtype=complex)
        signal_matrix = numpy.ndarray(shape=(ntrials, tb.ndata), dtype=complex)
        signal_and_noise_matrix = numpy.ndarray(shape=(ntrials, tb.ndata), dtype=complex)
        
        signal_power = 0
        threshold = 1e-16
        while signal_power < threshold:
            # Read in samples to discard, because they'll be all zero the first time
            sn = (tb.blocks_probe_signal_and_noise.level())
            noise = (tb.blocks_probe_noise_only.level())
            signal = (tb.blocks_probe_signal_only.level())      
            signal_power = sum(numpy.abs(signal)**2)/len(signal)

        for i in range(ntrials):
          sn = (tb.blocks_probe_signal_and_noise.level())   
          noise = (tb.blocks_probe_noise_only.level())                      
          signal = (tb.blocks_probe_signal_only.level())  

          noise_matrix[i] = noise
          signal_matrix[i] = signal
          signal_and_noise_matrix[i] = signal_matrix[i] + noise_matrix[i]

            
          signal_power = sum(numpy.abs(signal)**2)/len(signal)
          noise_power = sum(numpy.abs(noise)**2)/len(signal)
          # Computed SNR: 
          # print(10*numpy.log10(signal_power/noise_power))

          expected_SNR = numpy.log2(tb.signal_gain/tb.noise_amplitude)*6 -3 
          time.sleep(max(tb.ndata/tb.samp_rate, .1))                      

       # pickle the matrixes
        P = [ noise_matrix, signal_matrix, signal_and_noise_matrix]
        str_SNR=  str(abs(int(expected_SNR)))
        if expected_SNR < 0: 
            str_SNR= "neg" + str_SNR
        filename = str_SNR + "db_" + str(ntrials) + "trials"
        pickle.dump( P, open(filename+ ".p" , "wb"))
          
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()