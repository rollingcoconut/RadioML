# RadioML

Dec 12 : Have a groove going in the library so will be working from here; please
email if  I should come to lab to discuss anything. I've made a modular function
to plot {M2,M4} vs SNR and am working on to plot k_a vs k_w. By end of today
should  have plots for these things (hopefully SVR estimator features as well).

Dec 13: (email accessible working from cafe till 10pm): 
Now:  ρ_M2M4
After: wil plot 46, β, and ρ_svr

(tonight) will be working on designing a policy, how to test
that policy on our synthesized  data (step  8 of list) 


*OBSERVATION: I addressed the following, and have made some observations in my
notebook (fyi thanks for your email; it was super helpful!)

(what I addressed today so far) we should be computing the moment 128 times, one
for each trial.



Nov 29: parts 3,4 done for new samples (running into trouble with density SNR plots;
formula I use for computing SNR (10log10(sP/nP)) is 3db off
	
	- notebook is easier to navigate with code cleaned up
	- notebook is consistent


/3. Modify your notebook so that you read in a pickled array for a given SNR, rather
than generating the signal and noise samples yourself. (Don't create a new
notebook; just edit the existing one that we have been working with.) Push to
Github.

\4. In that notebook, create those three figures - the scatter plot of average
power, the density plot of average power, and the density plot of SNR - for each
of the SNRs. Are the "noise" and "signal+noise" classes easily separable using
"average received power" as the feature? Explain. Push to Github.


\5. Now look at alternative features on which to classify. Consider the M2M4
estimator, explain (in your notebook):

* What is the intuition behind the 2nd moment of a signal? behind the 4th
moment? What is the kurtosis of both the noise and signal(defined in the paper as k_a and k_w)?

* What is the expected value of the 2nd moment of the M-PSK signal? of the
noise? Go through the derivation in the paper, explain. Repeat for 4th
moment. You may find it helpful to plot the distribution of the samples
themselves (density plot) for the signal and noise, respectively, and
point out what these tell us about M2 and M4.

* Compute the 2nd and 4th moments of the M-PSK signal and of the
noise. Are they consistent with your expectation (from the previous
point)? 


M2 = np.mean(abs(signal)**2)

M4 = np.mean(abs(signal)**4)


\6. Repeat step 5, with the terms in the SVR estimator: the expression in equation
46, β, and ρ_svr.

\7. How do each of the following vary with SNR: M2, M4, k_a, k_w, ρ_M2M4, the
expression in equation 46, β, and ρ_svr. (You can make a line plot with markers,
where SNR varies along the horizontal axis)

\8. Based on what you have learned from 5, 6, 7, which of the following do you think
might be useful features with which to try and distinguish (classify)
signal+noise and noise-only classes? M2, M4, k_a, k_w, ρ_M2M4, the expression in
equation 46, β, and ρ_svr, some other combination of these?
