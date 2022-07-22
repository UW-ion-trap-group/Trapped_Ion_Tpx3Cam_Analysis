Traning for quantum jumps project. 
Method Used: Integration Time
> About the method: 
>> Split the length of the experiment into "chunks" of time (the "integration time") of say, 40 ms. Count the number of photons that hit the camera in each interval.
>> For an appropriate integration time, the graph should be *roughly* two Poisson curves — one while the ion is dark and the other while the ion is bright. The intersection of the two curves is used to determine a "threshold" (k) for number of photons. If within an integration time, the number of photons collected is larger than the threshold, then the ion must be in the bright state. 

> Multi-ion and crosstalk 
>> Due to crosstalk, the threshold is not exactly at the intersection. To determine an adequate threshold, we try to perform error analysis. 

> Error: The change in transition rate as k is shifted by +-1. 
> Since the slope at intersection is at its lowest, the change in transition rate is the lowest at "true" k. Thus, by minimizing the change in transition rate, we can determine optimal/true k. 

Steps ( NOT specific to integration time method). 
1) Collect and preprocess data. 
2) Perform "Preliminary Processing" (folder file with the same name)
3) Look at data for melting etc. Resolve any inconsistencies. "Pandas"
4) Data is ready to be analyzed. 
