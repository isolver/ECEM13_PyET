.. _savingData:

Saving Data and Finishing Touches.
--------------------------------------

Now we have our experiment up and running we are only missing one thing. We haven't actually saved anything yet!

Creating a file name
~~~~~~~~~~~~~~~~~~~~~~~~~~
In general when running an experiment it is a good idea to give each file and unique identifier whether it is with a participant name, date string or some other variable. In this case we will use the date, we can get a date string using ``psychopy.data.data.getDateStr()``. Use this in combination with an appropriate file descriptor to make a string variable that you can use as your file name.

Saving data
~~~~~~~~~~~~
There are several different formats that PsychoPy can save your data in. In general `wide text` and .psydat are sufficient. So now save your data in those formats. 

.. note::
	You should always save in the .psydat format even if you don't intend to use it. These type of file contains all the information about the experiment you have run including the script so can be used for different kinds of data recovery if you have a problem down the line.
	
Instructions
~~~~~~~~~~~~~
Your participants need to know what to do so at the very beginning of your experiment add a few lines of text explaining what they should do that will remain on the screen until the partipant hits a key to indicate they are ready to start the experiment.

Tidying code
~~~~~~~~~~~~~
Within your script there are several variables which you may wish to change or tweak as you are testing your script. It is a good idea to define these at the start of the script so that you don't have to wade through lines of code in order to make a small change. These types of variables would include things lile the number of repetitions of the conditions and the display time of the stimuli. 

The :ref:`solution <savingDataSolution>`.
