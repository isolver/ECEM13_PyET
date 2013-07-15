.. _collectingResponses:

Adding the Task and Collecting Responses
----------------------------------------

Changing the stimuli
~~~~~~~~~~~~~~~~~~~~
Your participant will be asked to press one of two keys depending on whether the stimulus presented is red or green. Currently our stimulus is always red so the first thing we need to do is  vary the colour between red and green based on our Excel file.

Collecting a response
~~~~~~~~~~~~~~~~~~~~~~~
In some experiments participants only have a limited time to respond and if they do not respond the experiment will continue running and that trial will be lost. In this experiment we are going to give our participants as long as they want to respond. In our loop we need to do several things that are linked together at this stage but we'll go through the one at a time.

Recording reaction time
~~~~~~~~~~~~~~~~~~~~~
In order to record reaction time we need a clock which starts when the stimulus is presented, records when the participant responds and is reset for each loop (after the RT has been saved).

Recording the response
~~~~~~~~~~~~~~~~~~~~~
What we need here is for the loop to pause until the participant makes a response. The easiest way to do this is with a while.. loop - while there is no response wait. Then once a response has been made save it. We want our participant to press 1 on the number pad if the stimulus is green and 3 if it's red. You want to make sure that your experiment will only accept these keys and won't move onto the next trial if a different key is pressed. Rather than recording the responses as 'red' and 'green' we will record a response of 1 if the participant presses 1 and 0 if the participant presses 3, this can make the data easier to analyse later.

.. note::
	At this point it's useful to add a statement that quits the experiment early if you press 'q' or 'escape'.
	
.. warning::
	`event.waitKeys()` produces a list, if you want to evaluate the contents of that list using the `in` command you will need to find a way to access that list e.g. using a for.. loop.

Collecting the data
~~~~~~~~~~~~~~~~
Add the two types of data (RT, response) to your TrialHandler object.

The :ref:`Solution <collectingResponsesSolution>`.

