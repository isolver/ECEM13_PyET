.. _ex1.6:

Exercise 1.6 - a list of dicts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

a)
========

We want to run the Stroop task. To do this we need a set trials (I would use a list of dictionaries) that have keys:

    - 'word' (one of 'red','green','blue')
    - 'ink' (one of 'red', 'green','blue')

We want every ink colour to be paired with every word. This can be done with 4 lines of code (but 5 is reasonable).

b)
========

In a loop print step through the entries of your trials and print out something like this::

    red red
    red green
    red blue
    ...
    blue blue

c)
=========

Print out just the ink colour of just the 4th trial in your list. If it didn't match the 4th row of your output from (b) then you've done something wrong!

d)
=========

Repeat Part (b) but add the index of each trial to your printout::

    0 red red
    1 red green
    ...
    7 blue green
    8 blue blue

Go to :ref:`sol1.6`