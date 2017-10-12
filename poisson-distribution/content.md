---
uid: radioactive_decay 
title: radioactive decay 
prerequisites:
  - undergraduate statistics and probability
learning_objectives:
  - Derive the Bateman equation
  - Characterize the effects of decay for radioisotopes with different decay rates
  - Apply the decay equation to identify an unknown radioisotope 
  - Derive the poisson distribution and compute the statistical moments
  - Interpret the meaning of the moments with respect to radioactive decay
references:
  - lamarsh.bib
abet_outcomes: n/a
assessments: 
  - counts.csv
  - bateman_eq_full.yml
  - bateman_eq_short.yml
  - half_life.yml
  - poisson_distribution.yml 
...
# Radioactive Decay
## Learning objective
Derive the Bateman equation  
Characterize the effects of decay for radioisotopes with different decay rates  
Apply the decay equation to identify an unknown radioisotope  
Derive the poisson distribution and compute the statistical moments  
Interpret the meaning of the moments with respect to radioactive decay  

### Overview
Radioactive decay refers generally to the distinegration of an unstable nucleus to a stable state. Radioactive decay is a stochastic process. Because we do not know the exact second that the nucleus will decay, we have to statistically model the decay process. Occurrences (decays) are randomly distributed in time. Therefore, we can use the Poisson process to characterize the mean time that a decay will occur.

The Poisson distribution just describes the probability of a given number of events, in our case, decays, that occur within a fixed time interval: $P(n) = e^{-\mu} \cdot \frac{\mu^{n}}{n!}$, and $\mu = \lambda \Delta t$, where $\lambda$ is defined as the decay constant which is what we really are most concerned about in nuclear science and engineering problems.

(We really do not use the Poisson distribution per se, but we need to define the distribution in order to obtain the decay constant.)

### Decay law
Let's assume n(t) atoms at time (t) have decayed in the very small time interval dt.

$$\lambda n(t)dt$$

On average, the atom decays from t to t+dt as:

$$-dn(t)=\lambda n(t)dt$$

If there are $n_0$ atoms at t = 0, then a solution to this differential equation for n(t) is readily obtained. 

### Half-life
Radioactive decay is typically characterized by half-life because each isotope decays with its specific rate. The half-life can be obtained using the decay law by substituting n(t) = $0.5n_0$ and solving for t. 

A radionuclide is considered negligible after 10 half-lives have elapsed. 

![decay graph](img/decay.png)

The following example for Au-198 shows how the half-life can obtained.

![Au-198](img/au198.png)

If a semi-log plot is used, then the decay constant is just the slope of the line.

![Au-198 log](img/au198_log.png)

A typical introductory laboratory exercise would be to take an unknown radioactive sample, record the counts at certain intervals, like every 30 seconds, and then plot the result. A fairly straightforward regression routine can be used to obtain the decay constant and then the half-life. 
_
### Additional Reading
[OER Radioactive Decay Notes](https://courses.candelalearning.com/x84x9/chapter/radioactive-decay)

