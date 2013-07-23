.. _sol1.6:

Solution 1.6
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    #part a)
    trials=[]
    for word in ['red','green','blue']:
        for ink in ['red','green','blue']:
            thisTrial = {'word':word, 'ink':ink}
            trials.append( thisTrial )

    #part b)
    for thisTrial in trials:
        print thisTrial['word'], thisTrial['ink']
    
    #part c)
    print trials[3]['ink'] #4th entry has index 3 BECAUSE WE START AT zero

    #part d)
    for ii, thisTrial in enumerate(trials):
        print ii, thisTrial['word'], thisTrial['ink']