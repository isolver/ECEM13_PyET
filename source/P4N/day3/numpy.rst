.. _numpy:

Numpy (numerical python) and scipy
=========================================================

Numpy is a library to help perform mathematicl operations on large `arrays` of data, in a way that is much faster than working with each individual element in a loop. For those of you that have programmed in Matlab before, `numpy` should feel quite familiar.

Numpy for maths
-----------------

Numpy contains a huge number of functions for anything mathematical. e.g. you can calculate the means and std devs of an array of numbers, or take their cosine etc. It's also useful for sorting and filtering data based on numeric criteria. You could have a look at the available functions using::

    import numpy as np
    print dir(np) #find out what sort of things you can do
    
    

`scipy` is another python library that extends the functions of `numpy` to perform more advanced operations, such as model fitting (optimisation) and working with statistical distributions

Numpy for speed
--------------------- 

Under the hood, numpy is performing its calculations in a for...loop but is doing that in C and therefore much faster. Let's do some comparisons. Imagine we have a long set of numbers, and for some reason we want to find the. We'll do it two ways and time each (using a PsychoPy clock)::

    from psychopy import core, misc
    import numpy as np
    
    #define some dots in a ring
    angles = np.arange(360.0)
    radius = 1.0
    
    clock=core.Clock()
    x=[]
    y=[]
    for thisAngle in angles:
        thisX, thisY = misc.pol2cart(thisAngle, radius)
        x.append( thisX )
        y.append( thisY )
    print "The loop took %.3f ms" %(clock.getTime()*1000)
    
    clock.reset()
    xArray = np.arange(360) #similar to range but can do decimals too
    x,y = misc.pol2cart(xArray, radius)
    print "numpy took %.3f ms" %(clock.getTime()*1000)
    
Programmers sometimes refer to this form of code as being 'vectorised' (operating on a vector rather than a single value). Try to vectorised code rather than a for...loop any time that calculations are going to be performed on large numbers of elements, especially if time is limited (e.g. if you need to get the next frame drawn before the screen refreshes!).