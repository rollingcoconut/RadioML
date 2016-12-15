# RadioML


Dec 14:  Times are a rolling along and I need to start with the ML part of
the project that I can tackle  successfully; here's a paper from China that uses
an SVM classifier to determine whether the sample classifies as noise or as noisy signal.

http://ieeexplore.ieee.org/document/6040028/

This is pretty much in line with what I can accomplish. What I'm going to do
(feel free to comment) is make two svm classifiers (they both should have better
predictive results than energy detection*) but one will be trained on the
collected data, and the other will be trained on the moments -- so just
different feature sets

The  results of which feature set is better is what I hope to include in my
results section

* need to figure out how to do energy detection 

You're feedback on this early implementation outline is greatly appreciated

------------------------------------------------------------------

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
