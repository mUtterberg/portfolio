Title: Not-So-SimpleCV: Tracebacks and Bitmaps
Date: 2018-10-26 09:02
Author: marissautterberg
Category: Data Science, Project-Based Learning
Tags: Computer Vision, OpenCV, Python, SimpleCV
Slug: not-so-simplecv-tracebacks-and-bitmaps
Status: published

My progress with the SimpleCV update was somewhat mixed yesterday. I was
able to go from a low of tracebacks on any image operation to a high of
loading two photo formats (though not stored with quite the right
attributes) before encountering dependency tracebacks on
***img.show()***. Hooray! But I also began to suspect that OpenCV might
have become simple enough to use with a few key documentation
improvements.

SimpleCV was written at a time that OpenCV, which has been around since
2001, used a C-dependent structure ([IplImage - a format taken from the
Intel Image Processing
Library](https://docs.opencv.org/2.4/modules/core/doc/old_basic_structures.html?highlight=cv_8u#iplimage))
to store image data and metadata. It was pretty foreign to Pythonic
styles because of things like manual memory management. SimpleCV manages
image processing by standardizing IplImages into
[bitmap](http://paulbourke.net/dataformats/bitmaps/) or matrix formats,
though there do seem to have been some attempts to include numpy array
functionality later on, as that format was first being
implemented. These days, OpenCV operates primarily on Matrices; the
Python wrapper draws heavily on Numpy arrays in particular.

![SimpleCVstatus.png](https://utterbergdatadev.files.wordpress.com/2018/10/simplecvstatus.png){.alignnone
.size-full .wp-image-1638 width="873" height="464"}

The file that I spent most of my day in was ImageClass.py, the core
component of SimpleCV's data model. In working through the tracebacks, I
created a Bitmap class to hold information as closely as I could find
information to help me construct it. I began questioning the need for
the use of Bitmaps right around when I got to tracebacks in which OpenCV
was expecting Numpy arrays.

My process so far has included a lot of hacking and workarounds to see
if I can appease cv2 with as few changes as possible. However, I'm
getting closer to a point that I will just start restructuring the
entire Image class to reflect the structure now used by OpenCV. The
authors may have abandoned the project for good reason, now that OpenCV
is more directly usable by Python developers. However, I am enjoying the
update process and will continue working through the broken bits. If
nothing else, they've got a decent shell interface that I'd like to be
able to use for teaching OpenCV.
