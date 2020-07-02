# RadioML

EE-UY 372

Fall 2016


As a conceptual model, a Cognitive Radio can 'sense' the spectrum to opportunistically communicate on frequencies. Using Q-PSK+AWGN signals generated with the gnu-radio software with varying SNRs, we formulate the signals' second and fourth moments (or signal variance and kurtosis) and use them as feature sets for our classifier.

Using an SVM Machine we test linear and Radial Basis Function kernels to determine the success of using our higher order moment feature sets to classify whether a Primary User is present.

Mentor: Fraida Fund
