---
layout: node
uuid: why-burnup
title: Why is burnup the best indicator of fuel irradiation time
prerequisites:
  - define-burnup
  - fuel-depletion
  - fuel-structural_changes
  - neutron-fluence
learning_objectives:
  - Explain why burnup is used instead of time as an indication for how long fuel has been irradiated.
references:
  - None
assessments: 
  - why-burnup-a

---


# Why is burnup the best indicator

Most often, we are interested in the way that irradiation has changed the
nuclear fuel in a reactor.  There are changes in the composition, including
the depletion of fissile material, the generation of fission products, and
transmutation of actinides.  There are also changes in the fuel structure
including swelling, porosity and cracks.  Those quantities typically depend
most strongly on the neutron fluence that the fuel has experienced.

# Relationship between neutron fluence and burnup

* Neutron fluence is the time integral of the neutron flux.
* Specific thermal power at any time is directly related to the neutron flux at that time.
* Burnup is the time integral of the specific thermal power.
* Therefore, burnup is an engineering manifestation of the neutron fluence.

# Relationship between burnup and time

![Figure 1](../img/fuel_response_v_time.svg){:height="400px" float="right"}

Figure 1 shows a simple power history for a piece
of nuclear fuel as a function of time.  There are three different power levels
including a period in which there is no power.  During each of the periods of
constant power, the burnup increases linearly, with a slope proportional to
the power.  During the period of zero power, the burnup doesn't change.  The
final plot represents some quantity, f, that depends on the neutron fluence.
It shows the same shape as the burnup plot.  All units are arbitrary.

![Figure 2](../img/fuel_response_v_burnup.svg){:height="400px" }

Figure 2 shows the same power history as a
function of the burnup.  The period with zero power does not appear in these
plots because it is reduced to a single point on the burnup domain.
Obviously, the slope of burnup vs burnup is constant (1).  Similarly, the
quantity, f, that depends on fluence also experiences a constant slope when
plotted vs burnup.


