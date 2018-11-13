Title: Reinforcement Learning
Date: 2018-03-02 11:41
Author: fuegalicious
Slug: reinforcement-learning
Status: published

Reinforcement Learning, also referred to as Online Learning, is an
adaptive way to select between versions of a product or advertisement to
optimize a desired user response.

The Multi-Armed Bandit Problem
==============================

The multi-armed bandit problem has been explored by statisticians for
decades. In the time of its origin, one-armed bandit was common term for
a Slot Machine. It makes sense, then, that the premise of this problem
involves a slot machine with many arms of varying payout
rates/probabilities. The challenge for analysts is to systematically and
sensibly sample and make observations on the outcomes from different
arms on the machine to maximize the probable payout without wasting
finite investment resources.

For the modern era, this problem is often approached from an advertising
perspective. This tutorial laid out the following scenario: an online
marketing company needs to choose between 10 versions of an
advertisement for their product. This is a multi-armed bandit problem
because there is no objective/available data on click-through rates
until the ads are piloted, however it would not be wise for them to
invest equally on all ads as clickthrough trends begin to emerge.
Therefore, we use an adaptive Reinforcement Learning approach to narrow
the field down to the top candidate(s), and to do so as quickly as
possible.

Upper Confidence Bound (UCB)
============================

#### In Python:

\[gallery ids="1085,1086" type="slideshow"\]

#### In R:

\[gallery ids="1087,1088" type="slideshow"\]

Our analysis of the multi-armed bandit problem in R began with a Random
Sampling for a baseline. As expected, there was little variation in the
clickthrough results for this method. By contrast, the Upper Confidence
Bound algorithm showed a clear top contender that was almost exclusively
called in the final hundreds of iterations (out of 10,000). The total
reward for the UCB algorithm was approximately 2200 - about 1000 more
total clickthroughs than in the Random Sampling algorithm.

Thompson Sampling
=================

\[gallery ids="1095,1096" type="slideshow"\]

Thompson Sampling showed an even greater improvement than the UCB model.
It more than doubled the reward given by the random sampling model -
from 1200 in Random Sampling to about 2600 from Thompson Sampling. While
searching for additional insights on this method, I found *[A Tutorial
on Thompson
Sampling](https://web.stanford.edu/~bvr/pubs/TS_Tutorial.pdf)*[by Daniel
Russo et al.
(2018)](https://web.stanford.edu/~bvr/pubs/TS_Tutorial.pdf), which I
would like to revisit for a more technical explanation of the algorithm
once my graduate and independent coursework calms down a bit.

 
