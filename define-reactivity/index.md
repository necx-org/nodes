---
layout: node
uuid: define-reactivity
title: Reactivity
prerequisites:
  - define-multiplication-factor
learning_objectives:
  - TODO
references:
  - TODO
abet_outcomes: [TODO]
assessments: 
  - calculate-reactivity
---

# Introduction

Reactivity is used to represent the **fractional change** in the neutron population between each generation; i.e., a reactivity greater than zero implies that the neutron population is increasing (power is increasing), whereas a negative reactivity implies that the neutron population is decreasing (decreasing power).

Typically in the context of reactor operations, we refer to reactivity as a means of maintaining equilibrium (steady-state) conditions within the core. That is, we look at the sum of various reactivity components (positive and negative) to determine the conditions required to maintain steady-state operations (such as how much fresh fuel to add, how much chemical shim or burnable poisons to include, and how much negative reactivity is needed in our control rods to safely control the reactor).

## Reactivity in an infinite reactor

For an infinitely large reactor (no leakage), the reactivity is defined in terms of the infinite multiplication factor ($$k_\infty$$) as:

$$
\rho = \frac{k_\infty - 1}{k_\infty}
$$

## Reactivity for a finite reactor

$$
\rho = \frac{k - 1}{k}
$$

Recall from the six-factor formula, the finite multiplication factor is simply the infinite multiplication factor plus the fast ($$P_F$$) and thermal ($$P_T$$) non-leakage terms, i.e.:

$$
k = P_{F} P_{T} k_\infty
$$

# Units of reactivity: Dollars and cents

Recall that the delayed neutron fraction of our reactor $$\beta$$ plays a crucial role to reactor control and kinetics; i.e., so long as our reactor is delayed critical (or, more generally, "prompt subcritical" - i.e., where delayed neutrons push us to to $$k \geq 1$$), the reactor period is proportional to the delayed neutron lifetime (which is substantially longer than the prompt neutron lifetime); this is what makes our reactor controllable.

As such, we define a special unit of reactivity change relative to the delayed neutron fraction in the reaction known as the dollar:

$$
\text{Reactivity in \$} =\frac{\rho}{\beta}
$$

Thus, one dollar ($) of reactivity corresponds to the reactivity insertion required for the reactor to go from delayed critical to prompt critical. 

Similarly, one cent (¢) corresponds to one hundredth (0.01) of a dollar.

For reference, recall that the delayed neutron fraction $$\beta$$ for $${}^{235}$$U is about 0.0065.

## Alternate units of reactive worth

Another alternate unit that frequently is used in characterizing the multiplication factor is pcm, or percent mille, which corresponds to one one-thousandth of one percent (or, 1E-5).

For example, the reactor multiplication factor may change on the order a few hundred pcm between cold zero power and hot zero power conditions (due to the expansion of the moderator). This corresponds to a change in $$k_{eff}$$ of:

$$
\Delta k = 100\ \text{pcm} = 100 \cdot 10^{-5} = 0.001
$$


