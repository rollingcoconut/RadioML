Almost finished with part 4; will get back to work Sunday evening
Spent Fri -Sun (nov20) at healthcare makerthon

# RadioML

Nov 29: (forgot I have an ML test tomorrow; will come in tomorrow Nov 29th afternoon 6-8pm) 

ACCOMPLISHED
* parts 4 for new samples : density plot of SNR added -- but it's a straight line, which sort 

TODO 
* part 5 (working here) 
 

3. Modify your notebook so that you read in a pickled array for a given SNR, rather
than generating the signal and noise samples yourself. (Don't create a new
notebook; just edit the existing one that we have been working with.) Push to
Github.

4. In that notebook, create those three figures - the scatter plot of average
power, the density plot of average power, and the density plot of SNR - for each
of the SNRs. Are the "noise" and "signal+noise" classes easily separable using
"average received power" as the feature? Explain. Push to Github.
Now look at alternative features on which to classify. Consider the M2M4
estimator, explain (in your notebook):

5. What is the intuition behind the 2nd moment of a signal? behind the 4th
moment? What is the kurtosis of each (defined in the paper as k_a and k_w)?
What is the expected value of the 2nd moment of the M-PSK signal? of the
noise? Go through the derivation in the paper, explain. Repeat for 4th
moment. You may find it helpful to plot the distribution of the samples
themselves (density plot) for the signal and noise, respectively, and
point out what these tell us about M2 and M4.
Compute the 2nd and 4th moments of the M-PSK signal and of the
noise. Are they consistent with your expectation (from the previous
point)? 
