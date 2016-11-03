# RadioML

Nov 2: 
(goals)
* Generate Q-PSK samples
* Map sampled signal to power, and find the characteristics of a linear classifier that can predict when a sample detects a user
* Demonstrate how this task becomes harder  as SNR decreases: graph that  shows predictor accuracy over decreasing snr

(accomplished)
* Generated some Q-PSK samples 
* Decided to use svm classifer (has fit/predict functions in library) that will train on training set and specified snr
* Wrote scaffold for classifier

(to immediately do)
* Map accuracy vs a degrading snr
