Title: Not-So-SimpleCV: Fixer-Upper
Date: 2018-10-24 10:45
Author: marissautterberg
Category: Data Science, Project-Based Learning
Tags: Computer Vision, Debugging, Dependencies, Machine Learning, OpenCV, Porting, Python, SimpleCV
Slug: not-so-simplecv-fixer-upper
Status: published

After some time away due to a new job & the NASA Space Apps Challenge
hackathon, I was finally able to sit down for a day of debugging my fork
of SimpleCV. I left off with a version that loads and functions on
frozen-in-time dependencies on my Raspberry Pi, but that setup left me
with no real-time image capture capabilities. The camera I run on my Pi
is a discount Arduino camera, which may explain why SimpleCV was not
able to recognize the device driver. It works from the command line, but
not within the SimpleCV shell.

Luckily, I was use my progress on the Pi to get my big-girl computer to
the point that it can now load SimpleCV in the Python 2.7 virtual
environment I have for working on it! Since I already have a version
that works on historical versions of dependencies, I'm ready to start
moving the internals forward in time. The biggest issue is changing the
processing functions from OpenCV 2.x to 3.x, especially since the
removal of cv2.cv came with significant changes in names and parameters
of image processing functions.

Taking a step to the side, then, I'm working through OpenCV directly.
[This documentation tutorial on changing
color-spaces](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces) was
one such exercise.

\[gallery ids="1630,1631" type="slideshow"\]

So far, it is looking like many of the changes from cv2.cv to cv2 are
more than just different function/method/parameter names, though some
fixes have been as simple as removing 'CV\_' from certain constants.
However, the more familiar I become with these libraries, the better my
attempts at addressing the endless tracebacks will be. I know this is
more than a 1-person workload, but I still feel like updating this
library is a valuable project and an attainable goal.
