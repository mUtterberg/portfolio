Title: joy = StackOverflow.append(TensorFlow, h2o)
Date: 2018-03-05 20:21
Author: marissautterberg
Category: Data Science, Development, Project-Based Learning
Tags: Anaconda, Debugging, Deep Learning, h2o, h2o.init(), Java, JDK, Keras, ModuleNotFoundError, Python, R, Stack Overflow, TensorFlow
Slug: joy-stackoverflow-appendtensorflow-h2o
Status: published

We know that Stack Overflow is one of the most useful troubleshooting
forums for developers. However, I am grateful and outright elated every
time it helps me solve a persistent frustration. Most recently:
TensorFlow (for Python) and h2o (for R) refused to load from my
scripting IDEs.

![tensorflow\_error.png](https://utterbergdatadev.files.wordpress.com/2018/03/tensorflow_error.png){.alignnone
.size-full .wp-image-1168 width="1125" height="605"}

At first, I thought it was TensorFlow itself that was not compatible
with whatever system I was running. My firewall, maybe. The search term
"ModuleNotFoundError TensorFlow" only led me to [various GitHub
discussions](https://www.google.com/search?q=modulenotfounderror+no+module+named+%27tensorflow%27&oq=modulenotfound+error&aqs=chrome.5.69i57j0l5.8615j0j1&sourceid=chrome&ie=UTF-8)
that ended up taking me down an Anaconda version/environment rabbit hole
thinking I'd failed outright in installing TensorFlow itself. After
trying a few different install modes per forum suggestions, I tabled any
thought of Deep Learning with Python. Luckily, the h2o library in R gave
more meaningful error messages than the "No module named tensorflow"
returned by Spyder.

![h2o\_error.png](https://utterbergdatadev.files.wordpress.com/2018/03/h2o_error.png){.alignnone
.size-full .wp-image-1169 width="562" height="746"}

My hope was that R would have the answers when Python gave me grief, and
vice versa. This had been the case several times before, but not this
go-around. Error in h2o.init(nthreads = -1) ... Two package errors in
one session? Gimme a brark. Morning Grind time was running short and it
was nearing Morning Commute O'Clock. I tried the first JDK I could find,
which was the most up-to-date, and rushed a quick install in time to get
one last error before heading off to work. The suspense, it stung.

As a classroom teacher, any downtime I find during the work day is
consumed by grading. Plus, with the stress of managing teenagers for 7-8
hours a day, I often need to go for a long walk or hit the gym right
after work. It wasn't until after dinner that I finally calmed down
enough to open my computer and have another go. Someone on Stack
Overflow had mentioned that [h2o was not supported by Java 9, only JDKs
7 or
8](https://stackoverflow.com/questions/46392394/error-with-h2o-in-r-cant-connect-to-local-host).
Hope springs eternal! I tried that lead and...no luck. Yet. Further down
the thread, someone else had mentioned that they'd needed to fully
remove JDK 9 for h2o to kick in. One Stack Overflow post later, it
turned out that [uninstalling JDK 9 was as simple as deleting version 9
from the JavaVirtualMachines folder in my
library](https://stackoverflow.com/questions/47897097/how-to-uninstall-java-9-on-macos-sierra).

![JDK\_issue\_SOLVED.png](https://utterbergdatadev.files.wordpress.com/2018/03/jdk_issue_solved.png){.alignnone
.size-full .wp-image-1170 width="1428" height="733"}

AAAAAAAAND WE'RE BACK! Not only did this solve my issue with h2o in R,
but now TensorFlow loads and I can run my Python models that depend on
Keras!
