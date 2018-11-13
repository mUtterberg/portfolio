Title: Give Back Hack
Date: 2018-05-14 07:37
Author: marissautterberg
Category: Inspiration, Project-Based Learning
Tags: Business, Community Advocate, DocketDigest, Give Back Hack, hackathon, PACER, RSS, Social Impact, User Validation
Slug: give-back-hack
Status: published

> [GiveBackHack](https://www.givebackhack.com) is a weekend-long event
> that brings together passionate community members to develop
> sustainable, technology-based solutions to some of our most pressing
> social issues. We are the launchpad for social innovation you need to
> turn an idea into a reality. We bring together community leaders,
> designers, developers, and other concerned citizens to create
> solutions that will help make a lasting impact.

After pitching my idea for a biometric attendance scanner at Data Days
CLE, I decided to pitch more broadly to raise awareness about the drain
of administrative ineffeciencies on classroom environments. I brought a
few arduino boards and fingerprint scanners to GiveBackHack Cleveland
over the weekend, just in case my idea gained enough traction for
development. I ended up spending the event working with a team on a
law-related project, which ended up being exactly what I needed as far
as the timing was concerned.

GiveBackHack rescheduled due to marketing issues, so it landed on the
same weekend as PyCon 2018. This was frustrating because I had been
trying to start a Cleveland chapter of PyLadies and wanted to network at
the event. Working with a large team on which I was not the lead freed
me up to step away to PyCon. Twice! I'll comment on that wonderful
aspect in another post, but my pitch not getting developed at this event
really did end up being for the best.

Our project lead is a lawyer that uses the PACER platform (and RECAP
archives) to access court dockets for cases that she follows, often 40
at a time. She showed us the bizarrely predatory fee system of PACER and
the essentially unusable RSS feeds posted by the courts in a naive
attempt at open access to data that should legally be made publicly
available. Open data is more than just "available online;" there is an
aspect of accessibility that the current system violates.

Enter DocketDigest. Our developers were able to put together a web app
to take in a docket number and initiate a web scraper to periodically
listen for mention of that docket in the RSS feed, then email a
notification to the user when an update posts. This reduces the number
of times a user of the PACER system would need to unnecessarily rerun
costly reports just to see if updates had posted. For those that rely on
PACER for their job, DocketDigest has the potential to be a huge
time/money saver. Additionally, for citizens that want to follow court
proceedings via these documents (victims, community advocates, etc)
notifications with docket update titles may lower the barrier for
access.

My involvement was mostly creative and business-oriented because 1) we
had six professional developers on our team and 2) I was excited for the
flexibility to step away for PyCon activities. I learned so much about
design, database issues for web applications, defining a well-formed
business plan, and working on a tech/startup team. We watched teams
dissolve for various reasons and hashed out interpersonal dynamics at
play, then realized how lucky we were to end up with only driven,
reasonable teammates.

At the end of the event, our team lead pitched our MVP (minimum viable
product) and we ended up tieing for first place! If you or anyone you
know is a PACER user and deals with the frustration of trying to stay
current on the information available in this system, follow
[@DDigests](https://www.twitter.com/ddigests) as development continues.
They are still working out the type of bugs you will have when beginning
and pushing out a product in the span of a weekend, but it is currently
live and available for subscription at
[www.DocketDigest.com](https://www.docketdigest.com)

Happy hacking!
