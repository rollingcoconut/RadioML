#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Nov 27 18:38:58 2016
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time
import numpy

class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        gr.top_block.__init__(self, "Top Block")

        parser=OptionParser(option_class=eng_option)
        parser.add_option("-N", "--name", type="string", default="test",
                          help="Experiment name (to include in file name).")
        parser.add_option("-n", "--ndata", type="int", default=128,
                          help="Number of data samples to collect at a time.")
        parser.add_option("-t", "--ntrials", type="int", default=128,
                          help="Number of trials to run.")
        parser.add_option("-a", "--args", type="string", default="",
                          help="UHD device address args [default=%default]")
        parser.add_option("", "--spec", type="string", default="A:0 A:0",
                          help="Subdevice of UHD device where appropriate")
        parser.add_option("-A", "--antenna", type="string", default=None,
                          help="select Rx Antenna where appropriate")
        parser.add_option("-s", "--samp-rate", type="eng_float", default=1e6,
                          help="set sample rate (bandwidth) [default=%default]")
        parser.add_option("-f", "--freq", type="eng_float", default=2e9,
                          help="set frequency to FREQ [default=%default]", metavar="FREQ")
        parser.add_option("-g", "--rx-gain", type="eng_float", default=0,
                          help="set gain in dB (default is zero)")

        (options, args) = parser.parse_args()

        ##################################################
        # Variables
        ##################################################
	self.name = options.name
	self.ndata = options.ndata
	self.ntrials = options.ntrials
        self.samp_rate = options.samp_rate 
        self.rx_gain = options.rx_gain 
        self.freq = options.freq 

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(device_addr=options.args, stream_args=uhd.stream_args('fc32'))

        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)
	self.s2v = blocks.stream_to_vector(gr.sizeof_gr_complex, self.ndata)
        self.blocks_probe_signal_vx_0 = blocks.probe_signal_vc(self.ndata)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.s2v, 0), (self.blocks_probe_signal_vx_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)
        	

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        ntrials=tb.ntrials
        ndata=tb.ndata

        signal_matrix = numpy.ndarray(shape=(ntrials, ndata), dtype=complex)

        signal_power = 0
        threshold = 1e-16
        while signal_power < threshold:
            # Read in samples to discard, because they'll be all zero the first time
            signal = (tb.blocks_probe_signal_vx_0.level())
            signal_power = sum(numpy.abs(signal)**2)/len(signal)
	time.sleep(5)
        for i in range(ntrials):
            signal = (tb.blocks_probe_signal_vx_0.level())
	    signal_matrix[i] = signal
            signal_power = sum(numpy.abs(signal)**2)/len(signal)
	    print(i, signal_power, len(signal))
            time.sleep(max(tb.ndata/tb.samp_rate, .1))

        sigfilename = "samples_" + tb.name + "_" + str(ndata) + "_" + str(ntrials) + "_rcv"
        numpy.save(sigfilename, signal_matrix)


    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
 
