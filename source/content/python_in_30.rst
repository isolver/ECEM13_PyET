.. _30minPython:

Python in 30 minutes
==============================================

Python versus Matlab
~~~~~~~~~~~~~~~~~~~~~~~~

 - both high-level interpreted language
 - Matlab is a *maths* language with *programming* added
 - it's easy to learn but limited
 - Python is a *programming* language with *maths* added
 - Python is more powerful/flexible but more to learn
 - Both have large userbases; python is newer to our field, bigger userbase overall


PsychoPy
~~~~~~~~~~~~~~~~~~~~~~~~

 - a library to help run experiments
 - also an application with editor (Coder) and GUI interface (Builder)
 - hardware-accelerated graphics (OpenGL) flexible dynamic stimuli
 - good (and improving) temporal precision
 - >4000 users per month and active dev and user groups
 - easy to install and update
 - large range of stimuli, including dynamic stimuli
 - variety of units for specifying coordinates and colours
 - screen calibration
 - hardware I/O support
 
Open `PsychoPy` now to see the basic views:
    - `Coder` (with an output panel and a shell panel as well)
    - `Builder` (drag and drop to create experiments without code)
    - both have a demos menu to get you started
    - entire app is written in Python

Close the `Builder` for now - we'll be using `Coder` to start with

Python code
~~~~~~~~~~~~~~~~~~

You can try typing some Python commands in the shell view. This is an easy place to test what a small number of commands will do::

    >>> a = 3
    >>> b = a+2
    >>> print b

You could have put the same commands (don't copy the `>>>` ) into a script, saved it and pressed `run`. As soon as you have more than a few lines this is usually easier.
    
Unlike Matlab which allows the user to fetch any function on its path, Python requires you to import just the functions you need. These are collected into libraries called packages. You can find out what a library contains using `dir()` ::

    import os
    print dir(os)
    
Those libs can nest too::

    import numpy #numerical python functions (matrices etc)
    print numpy.random.rand() #the rand function, from the random sub-module of numpy
    
To call a function you need to give round parentheses (even if it needs no arguments to be given)::

    print os.getcwd() #run the function and print the output
    print os.getcwd   #this will print info about the function itself
    
Python indentation
~~~~~~~~~~~~~~~~~~~~~~

One of the things that confuses new users to Python is that indentation of code blocks (e.g. `if` statements and `for` loops). Whereas most languages use a character to signify end of a loop, Python uses the indentation::

    for n in range(10):
        print n
        print 'not done' #because indented below for loop
    print 'done' #because no longer indented

We all agree that you should indent code blocks like this, but in Python you **must** or it will be an error!

Python starts at 0
~~~~~~~~~~~~~~~~~~~~~~

If you're coming from a Matlab background then you might be surprised that the first entry of a list is 0::

     x = 'hello'
     print x[1] #surprisingly not an 'h'!
     print x[1:] #from e to the end
     print x[:-2] #from start to penultimate (-ve indices indicate back from the end)

Although zero-indexing takes some getting used to it's what nearly all languages do *except* for Matlab.

Object-oriented programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Python every variable is an object - functions (methods) are often associated with the objects for which they make sense::

    x = 'hello world'
    print x.split()
    print x.upper()
    print x.title()

Did we mention that the syntax is much nicer than Matlab's once you're used to it?::

    for word in x.split():
        print word
        
    print x+"!" # to combine strings just add them
    print x*3 #or repeat them by multiplying
    
    s1 = 'She said "hello"' #define a string with single-quote
    s2 = "She didn't!" #or with a double-quote
    
    a, b = 1, 2 #assign 2 things at once
    a, b = b, a #swap them!!
    

We could go on for a long time about this. But there are many online tutorials showing you how to use Python. Now you've seen some basic python syntax maybe take a look at soem of the PsychoPy Coder demos.

