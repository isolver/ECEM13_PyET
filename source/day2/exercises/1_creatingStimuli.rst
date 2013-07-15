.. _creatingStimuli:

1. Creating Stimuli
-----------------------------

We'll start by making sure we create our stimuli before adding the code to control different trials.

1a. Import the libraries you'll need
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Always do this at the top of your script regardless of where you actually use the lib within the script (it's easier to find and keep libs together when they're at the top). You'll certainly need ``from psychopy import visual, event, core`` but you'll find you need more as you go through.

1b. Creating a window & fixation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first thing you will need is to generate a window to draw your stimuli in and a fixation point. To start with it is easier to not use a full screen window as that will allow you to see if errors are occuring in the background, we can change it full screen later.

.. note::
	When you are building up your script ``event.waitKeys()`` can be useful. It will cause your script to pause, waiting for a key to be pressed, so you get a chance to see your stimuli and make sure that it is drawn the way you expected.

Now to create a fixation point - use a grating stimulus with no texture (tex=None) and a circular mask (mask='circle). 

:ref:`See the script so far <1b_windowAndFixation>`

1c. Creating the cue
~~~~~~~~~~~~~~~~~~~~~~~

Now we want to draw the cue+fixation for 300ms followed by just the fixation for 300ms. For the cue, you need to generate a black square outline a few degrees to the right of fixation. 

:ref:`See the script so far <1b_windowAndFixation>`

1d. Creating stimuli
~~~~~~~~~~~~~~~~~~~~~~
At this stage don't worry about making your stimulus change colour. Just get a circle that is either red or green presented to the right of fixation after the cue appears.

By now your program should have a window appear with a fixation drawn in it, a cue which then turns off and after a further pause is replaced with a coloured circle.

1e. Randomising position
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's present the stimulus and cue randomly either to the left or the right of fixation. Use the `random` library and `setPos` to do this. Hint: you'll need to create an x position that is randomly positive (right) or negative (left).

Your Code
~~~~~~~~~~~~~~

As with any piece of code there are several ways to achieve the same thing, but at this point your script should look something like :ref:`the solution <creatingStimuliSolution>`.

