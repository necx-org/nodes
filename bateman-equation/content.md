---
title: BATEMAN EQUATION
uuid: bateman-equation
prerequisites:
  - undergraduate differential equations
  - undergraduate calculus
learning_objectives:
  - Derive the Bateman equation
  - Characterize the effects of decay for radioisotopes with different decay rates
references:
  - lamarsh.bib
abet_outcomes: n/a
assessments: 
  - bateman-eq-full.yml
  - bateman-eq-short.yml
...
# Bateman equation
## Learning objective
Derive the Bateman equation  
Characterize the effects of decay for radioisotopes with different decay rates  

### Decay law
Let's assume n(t) atoms at time (t) have decayed in the very small time interval dt.

$\lambda n(t)dt$,

where $\lambda$ is the decay constant.

The decay constant is a characteristic time for the decay of a radionuclide based on the Poisson distribution. As such, it is unique to each radionuclide. 

On average, the atom decays from t to t+dt as:

$$-dn(t)=\lambda n(t)dt$$

If there are $n_0$ atoms at t = 0, then a solution to this differential equation for n(t) is readily obtained. 

$n(t)=n_0 e^{-\lambda t}$

### Decay chains

In many cases, whether in nature or for radionuclides produced as a result of reactor operation, a radionuclide will decay into another, and then another, etc., until a stable nuclide is produced. This is known as a decay chain. 

For a two member decay chain where A decays to B:

$\frac{dN_2}{dt}=\lambda_1 N_1-\lambda_2 N_2$

The number of atoms of B increase due to the decay of A into B, but the number of atoms of B also decrease due to its own decay.

$N_2(t)=N_1^0 \frac{\lambda_1}{\lambda_2-\lambda_1}(e^{-\lambda_1 t} e^{-\lambda_2 t})+N_2^0 e^{-\lambda_2 t}$,

if there are $N_0$ atoms present of the radionuclide at t = 0. 

For a chain of radionuclides from 1, 2, 3, ... i-1, i, i+1, N:

$\frac{dN_i}{dt}=\lambda_{i-1} N_{i-1}-\lambda_i N_i$

This can be solved for any number of radionuclides in a given decay chain, where the solution is known as the Batemani equation.

### Additional Reading
[OER Radioactive Decay Notes](https://courses.candelalearning.com/x84x9/chapter/radioactive-decay)
