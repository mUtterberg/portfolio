Title: The Missing AWS Link
Date: 2018-03-13 19:09
Author: marissautterberg
Category: Development, Project-Based Learning
Tags: Amazon, Amazon Web Services, AWS, Cloud, Cloud Hosting, Domain.com, Front End, hackathon, Major League Hacks, Route 53, S3, web development, website development
Slug: the-missing-aws-link
Status: published

One of the pieces I wasn't able to connect during my first hackathon was
linking my domain to the hosting I had set up on AWS. Without a site to
demo, the project fell by the wayside as the hackathon ended and my
responsibilities took over. Flash forward about a month to the email I
received from MLH (Major League Hacks) this afternoon with several
articles, including a quick tutorial on deploying via AWS.

As I followed the tutorial, I ran across several previous attempts in S3
buckets. None of these loaded on my domain, so I went ahead and uploaded
a fresh bucket to make sure everything matched the guide. Part of what I
was missing were public permissions for my index.html and the other
missing link was Route 53. I had spent the majority of my time trying to
figure out what I needed from ElasticBeanstalk, though I was doing so
before even having finished the code for my web app. For now, I decided
hosting a static website in AWS would be success enough to keep me
invested. I proceeded with the walkthrough and VOILA! Successful deploy
of [capngown.org](http://capngown.org) phase one. Cloud hosting, for the
win.

\[gallery ids="1234,1235" type="slideshow"\]

One of the things I'd like to revisit this summer is Elastic Beanstalk
so that I can deploy an actual app on this domain, but for now I have it
running an interactive static website from the Full Stack Web
Development course I took this winter.
