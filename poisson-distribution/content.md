---
title: POISSON DISTRIBUTION
uuid: poisson-distibution
prerequisites:
  - undergraduate statistics and probability
learning_objectives:
  - Derive the poisson distribution
  - Compute the statistical moments
  - Interpret the meaning of the moments with respect to radioactive decay
references:
  - lamarsh.bib
abet_outcomes: n/a
assessments: 
  - poisson-distribution.yml 
...
# Poisson distribution 
## Learning objective
Derive the poisson distribution and compute the statistical moments  
Interpret the meaning of the moments with respect to radioactive decay  

### Radioactive decay 
Radioactive decay refers generally to the distinegration of an unstable nucleus to a stable state. Radioactive decay is a stochastic process. Because we do not know the exact instant in time that the nucleus will decay, we have to statistically model the decay process. Occurrences (decays) are randomly distributed in time. Therefore, we can use the Poisson process to characterize the mean time that a decay will occur.

The Poisson distribution just describes the probability of a given number of events, in our case, decays, that occur within a fixed time interval: $P(n) = e^{-\mu} \cdot \frac{\mu^{n}}{n!}$, and $\mu = \lambda \Delta t$, where $\lambda$ is defined as the decay constant, which is covered in a related node.

### Additional Reading
[OER Radioactive Decay Notes](https://courses.candelalearning.com/x84x9/chapter/radioactive-decay)
