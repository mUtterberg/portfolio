Title: Artificial Neural Networks
Date: 2018-03-04 10:53
Author: fuegalicious
Slug: artificial-neural-networks
Status: published

The concept of Deep Learning was so intriguing and new to me that I
found it difficult to tear myself away from the lectures on the weekend
that I reached this topic. I ended up taking more detailed notes on ANN
and CNN than on any of the previous models, partly as a function of
their complexity/novelty and partly out of a desire to understand the
concepts thoroughly enough to explain what I was learning to my talented
Network Engineer boyfriend.

Deep Learning is an area of Machine Learning in which programs are
designed to mimic the way in which humans process new information and
learn. Specifically, these Deep Learning is modeled after human neural
networks, complete with several layers of connected neurons working in
concert with other "hidden layer" neurons to process the information
received through synapses.

\[caption id="attachment\_1120" align="alignnone" width="625"\]![Source:
Dixon, Matthew Francis, Klabjan, Diego and Bang, Jin Hoon,
Classification-Based Financial Markets Prediction Using Deep Neural
Networks (July 18, 2016). The Journal of Algorithmic
Finance.](https://utterbergdatadev.files.wordpress.com/2018/03/dixon-screen-shot-2016-09-17-at-12-23-09-pm.png){.alignnone
.size-full .wp-image-1120 width="625" height="507"} Source: Dixon,
Matthew Francis, Klabjan, Diego and Bang, Jin Hoon, Classification-Based
Financial Markets Prediction Using Deep Neural Networks (July 18, 2016).
The Journal of Algorithmic Finance.\[/caption\]

For a more technical, in-depth description of synaptic input in the
context of Deep Learning, I will refer back to *[Efficient
BackProp](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf)*[by Yann
LeCun et al.
(1998)](http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf). This
document contains roughly 41 pages of analysis that is pertinent to
practicioners of Data Science. The network of neurons return outputs
that can be continuous, binary, or categorical - in which case, there
could be several outputs for each observation. In addition to this,
these signals are often passed to further hidden layers for processing
before the user sees a complete output.

The focus of a neural network is in the weights of each input for given
synapses. These weights are used to train the model and are how the
model is able to learn, or refine itself with successive iterations. The
activation function (chosen by the programmer) is what takes the initial
weighted sums and decides what signal to output for the next layer. In
the course I took ([Deep Learning A-Z by Kirill Eremenko and Hadelin de
Ponteves](https://www.superdatascience.com/courses/deep-learning-a-z/)),
we examined four common activation functions: Threshold, Sigmoid,
Rectifier, and Hyperbolic Tangent functions. The further reading offered
on this topic was *[Deep Sparse Rectifier Neural
Networks](http://proceedings.mlr.press/v15/glorot11a/glorot11a.pdf)*[by
Xavier Glorot et al.
(2011)](http://proceedings.mlr.press/v15/glorot11a/glorot11a.pdf).

Neural networks can be simplified to an input layer and an output layer,
which would essentially be analagous to or replaceable by any of the
regression models reviewed earlier. However, what sets NNs apart from
those models is the activity in one or more hidden layers between the
inputs and the output. Each neuron in the hidden layer treats the
weights as it was trained, so the distinct neurons in the hidden layer
receive the same inputs but often pass along different signals that
contribute to the next layer or to the output. In addition to this, each
neuron has distinct conditions that must be met (as determined in the
training phase of the model) for the neuron to even activate and pass on
a signal!

Maybe it's the educator in me, but I am obsessed with the analogies to
human learning. For example, since neural networks learn by observation
rather than being coded with explicitly defined rules, it is important
for data scientists to be conscious of possible biases in the data used
to train neural networks. One researcher shared an anecdote related to
the training of his computer vision model designed to identify and
automatically filter out gratuitous nudity. As he was training the model
to differentiate between clothed, artful nudity, and gratuitous nudity,
his model continued to flag images that were not nude. His research team
noticed that these false flags were often swimsuit photos or similarly
bare midriffs. Since his training data included no examples of segmented
nudity, his model believed that navels were indecent! This is similar to
confirmation bias or persistent misconceptions in human learning.
Thankfully, human and computer neural networks can be retrained with
strategically improved training data. And, for humans, a willingness to
relearn.

In addition to this, the way in which we train neural networks looks
very similar to the observe-hypothesize-assess-adjust cycle that humans
use when learning and forming worldviews. In making mistakes, we learn
from them when given meaningful feedback (similar to the Cost function C
in NNs) and apply ourselves to consider new possible hypotheses (similar
to Gradient Descent) - in this way, we form and reform understanding of
the information we receive through sight, sound, smell, taste, and feel.

https://youtu.be/JC82Il2cjqA

> [You Can Learn Anything (video from Khan
> Academy)](https://youtu.be/JC82Il2cjqA)

In Python:
==========

We employed Theano, TensorFlow, and Keras to power the ANN for our
scenario.

In R:
=====

As is often the case, R has more succint libraries more readily
available for data science tasks. What took 10 videos in Python only
took 4 videos to walk through in R. I still prefer Python in general
because the language is applicable in a broader range of contexts, but R
is clearly a highly efficient tool that I will continue to use in
certain data science contexts.

Additional Reading:
===================

Additional readings for...

Cost functions:

*[A list of cost functions used in neural networks, alongside
applications](https://stats.stackexchange.com/questions/154879/a-list-of-cost-functions-used-in-neural-networks-alongside-applications)*[from
CrossValidated
(2015)](https://stats.stackexchange.com/questions/154879/a-list-of-cost-functions-used-in-neural-networks-alongside-applications)

Gradient descent:

*[A Neural Network in 13 lines of Python (Part 2 - Gradient
Descent)](https://iamtrask.github.io/2015/07/27/python-network-part2/)*[by
Andrew Trask
(2015)](https://iamtrask.github.io/2015/07/27/python-network-part2/)

Backpropagation (mathematics-rich explanations):

[*Neural Networks and Deep Learning, chapter 2* by Michael Nielsen
(2015)](http://neuralnetworksanddeeplearning.com/chap2.html)

 
