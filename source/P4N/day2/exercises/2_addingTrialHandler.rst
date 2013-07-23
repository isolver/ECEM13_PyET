.. _addingTrialHandler:

Adding TrialHandler and Creating Loops
---------------------------------------

There is a TrialHandler demo which you may find helpful for this section

Creating a conditions list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The conditions list (aka trialList) for a TrialHandler is simply a list of dictionaries. As you loop through the trials you will receive one dictionary from the list selected from the original set (to do with as you will).

There are various ways to create that list of dicts:

    - do it using code as you did in the previous exercises
    - use psychopy.data.importConditions('someFile.xlsx') 
    
We'll create an Excel document for this. Psychopy treats the first row as the variable names and each row after that as a different condition. In this case we will only have three variable per condition but you can have many more. Your conditions will be the different intervals between cue and stimulus presentation, the colour of the stimulus and whether the cue is presented. In this case you want your SOA variable to start at 0 and go up to 500ms in 100ms increments twice once for red and once for green and then twice more for cued/uncued, leading to 24 conditions.
* Think about how you want your data presented in the Excel file i.e. for the cue variable do you want it to contain a string e.g. 'cued', 'uncued' or a number 0, 1 or something else? What will be most useful for your script.

* Import this conditions list into Psychopy.

* Create a TrialHandler object called `trials` using `data.TrialHandler` which uses your conditions list.

* Decide what type of data you want to save, in this case reaction time, response and stimulus colour and add these to the trial handler.

.. note::
	Your Excel file needs to be saved in the same folder as your script (or you can specify the path to it as well as the file name).

Creating a for... loop
~~~~~~~~~~~~~~~~~~~~~~~~~~
You now need a loop to cycle through your conditions list. Your loop should iterate through `thisTrial` in `trials`, this is the value you want to change on each iteration. It should also call on the stimulus colour and cue variables. 

.. note:: 
	When you extract your conditions from the TrialHandler they are dictionaries. The variable name is the dictionary key.

The :ref:`Solution <addingTrialHandlerSolution>`.


