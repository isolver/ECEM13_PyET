.. _sol1.10:

Solution 1.10
~~~~~~~~~~~~~~~~~~~~~~


1.10 a)
=========

.. code-block:: python

    if x<0:
        x=-x

1.10 b)
=========

.. code-block:: python

    def absol(x):  
        if x<0:
            x=-x
        return x

1.10 c)
=========

.. code-block:: python

    def absol(x):  
        if x<0:
            x=-x
        return x
        
    import numpy as np
    nFails=0
    for val in range(100):
        thisX = np.random.random()*2-1
        if abs(thisX)==absol(thisX):
            nFails += 1
    if nFails>0:
        print "%i of the abs calculations failed" %(nFail)
    else:
        print "success! All passed!"
        
        
Test the output of your new function against the built-in ``abs()`` for 100 random numbers between -1 and 1. Count the number of fails and report with a ``print`` statement at the end whether the method works.
