.. _sol1.7:

Solution 1.7
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    trials={'word':[], 'ink':[]}
    for word in ['red','green','blue']:
        for ink in ['red','green','blue']:
            trials['word'].append(word)
            trials['ink'].append(ink)
    print trials
    