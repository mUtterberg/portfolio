Title: FunctionalCV on Python 2.7
Date: 2018-09-25 12:53
Author: marissautterberg
Category: Data Science, Project-Based Learning
Tags: Computer Vision, IoT, Machine Learning, Raspberry Pi, SimpleCV
Slug: functionalcv-on-python-2-7
Status: published

Though I'm still working on getting a Python 3 branch of SimpleCV
together, my Python 2.7 master branch has steadily improved to a
(mostly) functional state. I've only been able to get it up & running on
my Raspberry Pi, where the PiCam driver does not seem to be recognized
by SimpleCV, but all capabilities related to existing image captures
seem to be available.

\[gallery ids="1595,1596" type="slideshow"\]

Heads up: you don't seem to be able to escape in the middle of a
tutorial, even with control + D as suggested, but you can quit between
tutorials. I was able to experiment with the functionality in tutorials
1, 2, 4, 5, and 6 - which is what leads me to believe camera capture is
the only functionality I still need to troubleshoot on that branch.

Feel free to check out [my fork of the SimpleCV library on
GitHub](https://www.github.com/mutterberg/simplecv) for yourself and let
me know what issues it runs into on your Python 2.7 environment!
