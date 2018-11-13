Title: Django-twilio to the Rescue
Date: 2018-08-18 13:45
Author: marissautterberg
Category: Development, Project-Based Learning
Tags: CLEPyLadies, Django, Django-Twilio, GitHub, Giveaway, Meetup, Open Source, PyLadies, Twilio
Slug: django-twilio-to-the-rescue
Status: published

[Amanda Casari](https://www.oreilly.com/pub/au/7543) recently gave a
remote presentation (via Zoom) at [Cleveland
PyLadies](https://www.meetup.com/CLE-PyLadies/) on the topic of Feature
Engineering for count and text data. Since she graciously offered a copy
of her book to give away at the meetup, I wanted to put together a fancy
little [Twilio](https://www.twilio.com/) app to allow livestream viewers
to enter.

I don't know if I've come to expect an unreasonable level of
documentation or what, but I was disappointed that the Twilio
documentation only really gave useful information for hooking to Flask
apps. While I'm not new to Flask, I'm much more fluent in the Django
framework. As I was on a time crunch, I decided I was spending too much
time looking up Flask particulars, so I ultimately stuck with Django for
this particular project.

Handling the names that participants would be texting was my first goal,
which was the minimum viable functionality. But, in typical Utterberg
fashion, I decided to complicate things by having my app also generate a
confirmation text response. I find it frustrating when you can't be 100%
confident that you entered the right digits, so a confirmation text
seemed like it'd be worth the effort. The database structure was simple,
as all I needed the app to do on intake was store the phone number and
text body (participant name, per giveaway instructions) in a single
model. Getting the webhook to play nicely on a data type level turned
out to be the main nightmare. I must have wrestled with manual solutions
for almost an hour!

\[caption id="attachment\_1543" align="alignnone" width="472"
height="127" alt="Before django-twilio"\]![Before
django-twilio](https://utterbergdatadev.files.wordpress.com/2018/08/screen-shot-2018-09-10-at-1-14-16-pm.png){.alignnone
.size-full .wp-image-1543 width="472" height="127"} Before
django-twilio: Django did not play well with Twilio out of the
box.\[/caption\]

However, as [this helpful article from Paul
Hallett](https://www.twilio.com/blog/2014/04/building-a-simple-sms-message-application-with-twilio-and-django-2.html)
points out, the django-twilio package works in Django debug mode and
formats the HttpResponse object in the way that Twilio expects! I had
basic functionality with about 3 hours to spare.

Of course, opening the door to auto-generating texts led to me adding a
congratulation text to the winner and "aw shucks, not this time" texts
to all other entrants upon the official contest drawing. Luckily, a
simple "for" loop in my random selection view took care of that pretty
easily. Each participant received a text with a link to the GitHub repo
for the book - and everyone except the winner also got a link to
purchase the book itself.

![](https://utterbergdatadev.files.wordpress.com/2018/08/img_5591.jpg){.wp-image-1514
.aligncenter .size-full width="890" height="1780"}

Code for this project is available
at https://github.com/mUtterberg/book\_giveaway - though please do
remember that I ran this locally via Ngrok due to time constraints. If I
run a giveaway on this script again, I'll be setting up legitimate
hosting for it first.
