.. _sol1.5:

Solution 1.5
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    me = {'name':'Jon','age':21,'house':33,'street':'Banana Drive'}
    for key in me:
        print "%s: %s" %(key, me[key])

    #the last line could be
    print key, ":", me[key]