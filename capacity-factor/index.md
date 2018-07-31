---
layout: node
uuid: capacity-factor
title: Capacity Factor
prerequisites:
  - availability-factor
learning_objectives:
  - Describe capacity factor.
references:
  - refs.bib
abet_outcomes: [a]
assessments:
  - capacity-factor-calulation
  - capacity-vs-availability
...

# Capacity Factor 

The capacity factor is representative of the plant's tendency to acheive its rated power capacity.

\begin{align}
CF &= \frac{\mbox{actual power generated over time T}}{\mbox{rated power potential over time T}}\\\\
   &=\frac{\int_0^T P(t)dt}{P_0T}\\\\
P(t) &= \mbox{ thermal power at time t during period T}
\end{align}
