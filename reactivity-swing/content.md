# Introduction

As nuclear fuel is burned in a reactor, the reactive worth of the fuel steadily decreases. The net change in reactivity of the fuel over a cycle is referred to as the *reactivity swing*, often specified as $\Delta \rho$.

## Reactivity swing in a single-batch core

Consider the case of a core where all of the fuel is replaced at the end of the cycle. The reactive worth of the fuel as a function of time is:

\[ \rho \left( t \right) = \rho_1 \left\[\frac{1 - BU_1^{\left(1\right)} \left(t \right)}{BU_1^{\left(1\right)} \left(T\right)} \right] \] 

where $\rho \left(t\right)$ is the reactivity of the batch at time *t*, $\rho_1$ is the reactivity loaded into the core at the begining of the cycle, *T* is the total cycle length, $BU_1^{\left(1\right)} \left(T\right)$ is the final discharge burnup for a one-batch core (i.e., the end-of-cycle burnup), and $BU_1^{\left(1\right)} \left(t \right)$ is the fuel burnup at time *t* for batch 1. 

In general, this assumes the decrease in reactivity is linear with burnup, which is generally valid after a few days of irradiation in the core.

## Reactivity swing in a two-batch core

Now consider the case where half of the fuel is replaced with fresh fuel at the end each cycle. Therefore, the fuel is burned for two cycles before being discharged from the core. The reactivity swing as a function of time is thus:

\[ \rho \left( t \right) = \rho_1 \left( \frac{\left\[1 - \frac{BU_2^{\left(1\right)} \left(t \right)}{BU_1 \left(T\right)} \right] + \left\[1- \frac{BU_2^{\left(2\right)} \left(t \right)}{BU_1 \left(T\right)} \right]}{2} \right) \] 

Here, $BU_2^{1}\left(t\right)$ refers to the burnup of the first batch of the two-batch core at time *t* and $BU_2^{2}\left(t\right)$ refers to the burnup of the second (once-burned) batch at time *t*. 

# Implications of the multi-batch core

## Discharge burnup of a two-batch core

Let's look at the end-of-cycle burnup for the two-batch core, i.e. where $\rho = 0$. If we assume equal burnups between the first and second cycles - i.e., $BU_2^{\left(1\right)}\left(T\right) = \frac{BU_2^{\left(2\right)}}{2}$, we have:

\[ 0 = \rho_1 \left( \frac{\frac{ \left\[ 1 - \frac{BU_2\left(T\right)/2}{BU_1 \left(T \right)} \right\] + \left\[ 1 - \frac{BU_2\left(T\right)}{BU_1\left(T \right) \right\]}{2} \right) \]

Solving for $BU_2\left(T \right) in terms of $BU_1\left(T\right)$, we have:

\[ BU_2\left(T\right) = \left{ \frac{4}{3} \right} BU_1 \left(T \right) \]

In other words, the two-batch core represents a **33% gain** in terms of achievable discharge burnup over the single-batch core.

## Reactivity swing for the two-batch core

The new reactivity swing between the end of cycle and the new core (i.e., the amount of new reactivity that needs to be added to the core) is:

\[ \rho_2 \left(t \right) = \rho_1 \left( \frac{\frac{ \left\[ 1 - \frac{BU_2\left(0 \right)/2}{BU_1 \left(T \right)} \right\] + \left\[ 1 - \frac{BU_2\left(0 \right)}{BU_1\left(T \right) \right\]}{2} \right) = \frac{ 1 + \frac{2}{3} }{2} = \frac{2}{3} \rho_1 \]

In other words, the reactivity swing is now **a third lower** for the two-batch core than for the one-batch core. In other words, we only need to supply two-thirds of the new reactive worth to the core at the end of the cycle, **all for the same initial fuel enrichment**.

## Where does the extra burnup come from?

Multi-batch core loading allows us to squeeze out more burnup from the same amount of fuel - so is this a free lunch? What's the "trade-off" we take for this? In other words, where is the extra burnup coming from?

-To achieve a lower reactivity swing, multi-batch cores use a **shorter cycle length** (i.e., more frequent refueling outages)
-Multi-batch cores also require less burnable poisons compared to a single-batch core to keep the core at-critical; in other words, higher burnup is achieved because we don't "waste" neutrons on burnable absorbers.
-Because we're using our neutrons more efficiently, we're burning more of the fissile material in the fuel, achieving higher fuel utilization.

So is this a "free lunch?" No; we pay for it in terms of both shorter cycle length as well as better use of our neutrons in the core.

# Characteristics of the N-batch core

## Assembly burnup after n cycles

The burnup of a batch of assemblies after *n* cycles of an N-batch core is:

\[ BU_N^{\left(n\right)} \left(T \right) = \frac{ n BU_N \left(T \right) }{N} \rvert_{n=1 \dots N} \]

## Total core reactivity

The total reactivity of the core at time *t* for the N-batch core is:

\[ \rho_N \left( t \right) = \rho_1 \frac{ \sum_{n=1}^N \left[ 1 - \frac{BU_N^{\left(n \right) \left(t \right) }{ BU_1 \left(T \right) } \right] }{N} \]

## Final assembly discharge burnup

The final assembly discharge burnup after *N* cycles is:

\[ BU_N \left(T \right) = \frac{2 N}{N + 1} BU_1 \left(T \right) \]

The general relationship of the discharge burnup relative to the one-batch core is thus:

| # batches | $\frac{BU_N\left( T \right)}{BU_1 \left{T \right} } |
------------|:---------------------------------------------------:|
1 | 1
2 | 4/3 |
3 | 3/2 |
4 | 8/5 |
5 | 5/3 |
$\infty$ | 2 |

## So why don't we use as many batches as possible...?

Using more batches comes with an inherent trade-off: shorter cycle length. Because the minimum outage time is generally fixed (given the sequence of activities required to shut down the core, unload the fuel, and reload the fuel), having too many cycles can lead to lower capacity factors (thus obviating the benefit of greater discharge burnup).
