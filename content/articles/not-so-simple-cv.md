Title: Not-So-SimpleCV
Date: 2018-09-19 14:09
Author: marissautterberg
Category: Data Science, Project-Based Learning
Tags: Computer Vision, Machine Learning, Open Source, Python, SimpleCV
Slug: not-so-simple-cv
Status: published

It wasn't until after I'd submitted the talk proposal to 3 conferences
that I realized how big of a chunk I'd bitten off by writing in a
computer vision aspect. "Participants will gain insight on impactful
mindsets and actionable strategies for more effective professional
development - as well as a few starter Computer Vision scripts!"
Yeah...assuming they're running Python 2.7 on a raspberry pi and are
comfortable debugging their own fork of the seemingly abandoned SimpleCV
repo. Smooth move, Marissa. Clearly a stellar talk. Knock 'em dead.

However, as the focus of my talk is on leveraging research-based
strategies from the field of cognitive science to improve your own
learning, this was obviously an excellent opportunity to give my talk
takeaways a focused run-through. So before I get to the outcome of my
work on the SimpleCV library, let's establish those cognitive theory
talking points.

My talk is structured around a study from several research
groups[**(†)**](http://utterbergdatadev.com/2018/09/19/not-so-simple-cv#footnote) that
identified characteristics differentiating how novices and experts
approach new situations in a given domain. The shortest description the
study's authors gave for their concept was *the six principles of
expertise*, which makes me cringe to say. As a mathematician, I tend to
have a *really* hard time making imperative statements. What if we
missed a criterion? Or worse, what if we find a *counterexample*???
(Overthink much, Marissa?) Regardless, the 6 characteristics they
described were as follow:

> 1.  Experts notice features and meaningful patterns of information
>     that are not noticed by novices.
> 2.  Experts have acquired a great deal of content knowledge that is
>     organized in ways that reflect a deep understanding of their
>     subject matter.
> 3.  Experts’ knowledge cannot be reduced to sets of isolated facts or
>     propositions but, instead, reflects contexts of applicability:
>     that is, the knowledge is “contextualized” on a set of
>     circumstances.
> 4.  Experts are able to flexibly retrieve important aspects of their
>     knowledge with little attentional effort.
> 5.  Though experts know their disciplines thoroughly, this does not
>     guarantee that they are able to teach others.
> 6.  Experts have varying levels of flexibility in their approach to
>     new situations.

In the talk, I unpack each characteristic with comparisons that
developers across domains can relate to. However, I would like to have
more concrete contrasts as a way to get some tangible ML concepts and
realities across. With that in mind, I considered my experience digging
into SimpleCV in the context of expertise.

 

 

\[gallery ids="1573,1571" type="slideshow"\]

Running through a quick inventory of my expertise at this stage, I can't
avoid the reality of principle 4: fluency. Expert pythonistas tend to
recall appropriate libraries and commands much more quickly that I would
say that I currently do. Until I can approach a problem with a list of
possible libraries or solutions off-hand, fluency is my counter-example.
Ok, so I fall into the novice category at this point. What now?

This is where we consider scaffolding, also known as scaling. In the
field of education, scaffolding is targeted scaling that we specifically
intend to remove as proficiency increases. We may scale the scope of our
goal or the time-frame for success, the size of our team or the
resources we intend to use. For me, it seemed appropriate to start by
segmenting my scope. Rather than trying to put together a tutorial that
relies on SimpleCV being functional in a wide range of environments, I
first needed to get SimpleCV to run. Full stop.

Troubleshooting goal \#1: Make it work
--------------------------------------

Operating at the novice level **does not disqualify you**. Metacognitive
self-assessment is not an excuse to box yourself into a fixed category.
Genuine and critical self-reflection should be interpreted in the
context of 'artisans' vs 'virtuosos' (principle 6): everyone will be a
novice in some domain at many points in a lifetime. That's kind of the
point of being a life-long learner - we don't know it all! So being at
the novice stage of learning does not mean you should wait to start a
project until you are at the expert level. Pursuing projects for which
you're in over your head can progress you toward expert-like learning
because you are contextualizing as you learn (principle 3). We rarely
read through all documentation before beginning a project. Not that it's
a terrible idea, it's just more likely to stick (or to make sense,
period) if we have a concrete context for what we're learning.

So my context for learning is clearly SimpleCV in this project, but the
content of my learning is turning out to be much more than anticipated.
Did I get it to work?

\[caption id="attachment\_1576" align="alignnone"
width="3264"\]![](https://utterbergdatadev.files.wordpress.com/2018/09/img_5713.jpg){.wp-image-1576
.size-full width="3264" height="2448"} Success! Functional SimpleCV on
my Raspberry Pi.\[/caption\]

Heck yeah! Kind of. Calling `simplecv` in Python 2.7 no longer gives
errors now that I've installed my updated fork of it on my Raspberry Pi,
but there are still some bugs in trying to do image capture with it. For
now, I'm going to say that this technically meet my goal \#1. But I
don't feel much closer to expertise.

Now what?

Troubleshooting goal \#2: Make it right
---------------------------------------

I could reassess and take stock of my *growth* toward expertise, which
has not been insignificant. However, I think I'll break that out into a
separate post. For now, I'm playing around with my goals \#2 (working
through the actual functionality of the library, fixing bugs as they
appear) and \#3 (making progress toward Python 3 compatibility on my
fork of SimpleCV). It feels like that third bite is much bigger than
I'll be able to achieve, but that's assuming a team of size 1. In
preparing for my talk itself, a certain amount of work will be on my
own, but collaboration is part of the beauty of the open-source software
community. In fact, discussing others' progress toward Python 3 support
and working with their forks makes that goal \#3 feel more possible.

Since one of the takeaways of my talk is the power of growth mindset,
I'll close with a brief video on the topic.

https://www.youtube.com/watch?v=M1CHPnZfFmU

Though my talk is changing as we speak, and will continue to do so even
after I present it a few times, one takeaway that I will believe will
continue to serve me well is this: no one is born knowing everything, so
everything we want to learn is accessible - though it may take a few
extra steps (and some creative risk) to get there.

 

#### Footnote:

[†](#footnote) The study, published in April 1999 with the work of *The
Committee on Developments in the Science of Learning *and
of the *National Research Council (NRC)*, was expanded upon in August
2000 with the work of an additional *NRC* committee, *The Committee on
Learning Research and Educational Practice*.
