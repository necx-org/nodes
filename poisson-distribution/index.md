---
layout: node
title: Poisson Distribution
uuid: poisson-distibution
prerequisites:
  - statistical-distributions
  - probability
learning_objectives:
  - Derive the poisson distribution
  - Compute the statistical moments
  - Interpret the meaning of the moments with respect to radioactive decay
references:
  - https://stattrek.com/probability-distributions/poisson.aspx
abet_outcomes: n/a
assessments: 
  - derive-poisson-distribution 
...
# Overview
A radioactive isotope decays with a unique, characteristic time. This is conceptualzied by a stochastic process. That is, the exact time any particular atom decays cannon be known. Therefore, a probablilty distribution is used to describe the behavior of radioactive decay.

## Poisson distribution
The statistical distribution applied to describe decay is the Poisson distribution. If the average number of decays in a period of time is defined as 

$$\mu \equiv \lambda \Delta t$$

where $\lambda$ is defined as the decay constant, specific to the radioactive isotope. 

Then the probablity of an exact number of $n$ decays that will occur in $\Delta t$ is

$$P(n) = e^{-\mu} \cdot \frac{\mu^{n}}{n!}$$
