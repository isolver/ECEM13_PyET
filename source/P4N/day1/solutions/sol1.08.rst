.. _sol1.8:

Solution 1.8
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    greet = 'Hello'
    name = 'Jon'
    height = 1.80
    hour = 9
    minute = 5

    print "%s %s" %(greet, name)
    print "%s %s" %(greet.upper(), name)
    print "The time is %i.%02iam" %(hour, minute)
    print "The time is %02i:%02i" %(hour, minute)
    print "%s is %.1fm tall" %(name, height)