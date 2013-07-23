.. _sol1.9:

Solution 1.9
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import sys
    print sys.version
    print sys.platform
    print sys.getdefaultencoding() #NB this is a function not a variable
    print sys.executable
    import os
    print os.getcwd()
    print os.environ

.. note::

    Python built-in modules tend to use the word get___() to indicate that this is a function rather than an attribute. That might be a good thing to do in your own functions?
    
.. code-block:: python

    import numpy as np
    print np.random.random([2,3])
    print np.random.randint(5,11) #NB the high-end of the interval is non-inclusive :-/
    #or
    print round(np.random.random()*5+5)