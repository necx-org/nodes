---
layout: node
uuid: n-batch-cores
title: Multi-batch core loading - the n-batch core
prerequisites:
  - define-reactivity
  - define-burnup
learning_objectives:
  - Calculate the reactivity swing for single-batch versus multi-batch cores
  - Communicate how gains in discharge burnup are achieved using multi-batch cores
references:
  - tsoulfanidis_fuel_cycle_2013
abet_outcomes: []
assessments: 
 - TBD
---


# Characteristics of the N-batch core

## Assembly burnup after n cycles

The burnup of a batch of assemblies after *n* cycles of an N-batch core is:

$$
BU_N^{\left(n\right)} \left(T \right) = \left[\frac{ n BU_N \left(T \right) }{N} \right] \rvert_{n=1 \dots N}
$$

## Reactivity swing



## Total core reactivity

The total reactivity of the core at time *t* for the N-batch core is:

$$
  \rho_N \left( t \right) = \rho_1 \frac{ \sum_{n=1}^N \left[ 1 - \frac{BU_N^{\left(n \right)} \left(t \right) }{ BU_1 \left(T \right) } \right] }{N} \rho_1
$$

## Final assembly discharge burnup

The final assembly discharge burnup after *N* cycles is:

$$ 
BU_N \left(T \right) = \left[ \frac{2 N}{N + 1} \right] BU_1 \left(T \right) 
$$

The general relationship of the discharge burnup relative to the one-batch core is thus:


| # batches     | $$\frac{ BU_N \left( T \right)}{BU_1 \left(T \right) }$$ |
----------------|:---------------------------------------------------------|
1               | 1   |
2               | 4/3 |
3               | 3/2 |
4               | 8/5 |
5               | 5/3 |
$$\infty$$      | 2   |



## So why don't we use as many batches as possible...?

Using more batches comes with an inherent trade-off: shorter cycle length. Because the minimum outage time is generally fixed (given the sequence of activities required to shut down the core, unload the fuel, and reload the fuel), having too many cycles can lead to lower capacity factors (thus obviating the benefit of greater discharge burnup).
