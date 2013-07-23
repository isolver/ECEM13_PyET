.. _psychopyConcepts:

PsychoPy Basics
---------------------

Some of the basic principals behind PsychoPy are explained below. There is much more information about each in the formal online documentation and in the demos menu in the PsychoPy Coder view.

Importing the libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are quite a few `PsychoPy Libraries <http://www.psychopy.org/api/api.html>`_ that are useful for different purposes. Nearly always you'll want visual stimuli, core functions (like clocks) and events (to monitor the keyboard and mouse). I recommend importing them like this to keep the 'namespace' (the set of named variables) relatively clean.::

    from psychopy import core, visual, event
    win = visual.Window([400,400], monitor='testMonitor')

Note that there are many other potential arguments that we could use to control the way the `Window`_ is created. 

Presenting visual stimuli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PsychoPy uses OpenGL and double-buffered drawing to update the screen. That means it is drawing to a 'back buffer' and when you've finished laying out the screen the way you like it you tell the `Window <http://www.psychopy.org/api/visual/window.html>`_ to ``flip()``. PsychoPy wil then wait until the frame flip actually occurs before continuing code execution so that on the very next command you know the visual stimuli have all actually appeared on screen. Having created your stimui you can change them in various ways before.

.. code-block:: python

    from psychopy import core, visual, event
    win = visual.Window([400,400])

    #initialise some stimuli
    gabor = visual.GratingStim(myWin, tex="sin", mask="gauss",  texRes=256, size=[1.0,1.0], sf=[4,0], ori = 0, name='gabor1')
    trialClock = core.Clock()

    #repeat drawing for each frame
    while trialClock.getTime()<0.25:
        gabor.setPhase(0.01,'+')
        gabor.draw()
        myWin.flip() #will occur every 1/60th second

See the demos and http://www.psychopy.org/api/visual.html for more information about the different types of stimulus that are available.

Time by frames
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The above code presents the stimulus until the time is greater than or equal to 20s. If the time is actually 19.97s at the point this code is reached then another frame will be drawn (lasting, say 1/60th of a second). If you want a stimulus to last for a very precise amount of time you should display it for a fixed number of monitor *frames*. On a 60Hz monitor 15 frames will always be exactly 250ms, provided no frames were 'dropped'.

The other advantage to timing by frames is that it will remind you that you absolutely cannot present a stimulus for anything other than a whole number of screen refreshes.

To use frames for the code above replace the drawing loop with this.

.. code-block:: python

    for frame in range(15): #15 frames at 60Hz = 250ms    
        gabor.setPhase(0.01,'+')
        gabor.draw()
        myWin.flip()

You can test the frame intervals on your computer using the timeByFrames demo

Stimulus coordinates
~~~~~~~~~~~~~~~~~~~~~~~~~

In PsychoPy coordinate systems (0,0) is always the centre of the screen

There are various units available for the coordinates of your stimuli:

    - ‘norm’: the screen goes -1 to +1 in X and Y (so has a width and height of 2)
    - ‘height’: a value of 1.0 is equal to the height of the screen
    - ‘pix’: number of pixels
    - ‘cm’: requires the resolution and width of the display
    - ‘deg’: requires the resolution, width and distance of the display

Units apply to pos, size, spatial frequency and can be different for each stimulus
For more info see http://www.psychopy.org/general/units.html 

Colours
~~~~~~~~~~~

See the official online documentation for `PsychoPy Color Spaces <http://www.psychopy.org/general/colours.html>`_

.. _Window:  http://www.psychopy.org/api/visual/window.html

Trials and data
~~~~~~~~~~~~~~~~~~~~~~~~~

You could control trials yourself using the lists and dicts that you learned about yesterday. But `psychopy.data <http://www.psychopy.org/api/data.html>`_ provides tools to help.

.. code-block:: python

    from psychopy import data
    trialList = data.importConditions('conditions.xlsx') #create a list of dicts
    trials = data.TrialHandler(trialList, nReps=5,  extraInfo=infoDict, name='mainTrials')
    for thisTrial in trials:
       #do stuff
       trials.addData(‘RT’,thisRT)

There are other types of 'Handler' for other experimental designs like psychophysical staircases (``StairHandler``, ``QuestHandler``, ``MultiStairHandler``). Any of these handlers can save a variety of data formats:

    - Python pickle files (psydat). Literally a copy of the Handler that saved the data. Contains all the information, including a copy of the entire experiment code, and can be used to re-generate the other data files. **Always** save a psydat file!
    - Long-wide data file (csv). Trial-by-trial chronological format. Useful for analysis in software packages like `R`
    - Summarized data (excel or csv). One row represents one condition, rather than one trial

You can save your data in multiple formats. e.g. 

.. code-block:: python

    #create useful and unique file name
    subjName = "JWP"
    timeDateStr = data.getDateStr() #current time/date as a string
    filename = "%s_%s" %(subjName, timeDateStr)
    #save data
    trials.saveAsWideText(fileName, delim=',') #long-wide, one row per trial
    trials.saveAsText(fileName, delim=',') #summarised format
    trials.saveAsExcel(fileName, sheetname = "mainTrials") #summarised format, excel output
    trials.saveAsPickle(filename) #the entire thing
        
ExperimentHandler
~~~~~~~~~~~~~~~~~~~~~~

Each of the Handlers above represent one 'loop' in your experiment. But you might have a set of practice trials, followed by a set of probe trials. It's useful to keep those together in a single data file. Also, if the subject quits, or if there's an error, before the end of the experiment the data up to that point will be lost. `ExperimentHandler <http://www.psychopy.org/api/data.html#experimenthandler>`_ solves those problems. It allows you to assign multiple loops that can be saved in a single file (and the text output will still be chronologically organised if they are interleaved). It expects you to specify a filename during its creation and will then automatically save data in the desired formats in the event of a bug (except for a very extreme one) of early termination. This Handler doesn't support 'summarised' formats, but long-wide text and psydat files are probably the most useful anyway!

For this type of handler it might not be clear when a new line is supposed to start (it might not align with a loop in your code) so you have to inform it when the the next 'event' is beginning.  

.. code-block:: python

    from psychopy import data
    
    trialList = data.importConditions('conditions.xlsx') #create a list of dicts
    trials = data.TrialHandler(trialList, nReps=5,  extraInfo=infoDict, name='mainTrials')
    myExp = data.ExperimentHandler(name='Face Pref', version='0.1',
        extraInfo = info,
        dataFileName = filename, savePickle=True, saveWideText=True)
    myExp.addLoop(trials)
    
    #run conditions
    for thisTrial in trials:
    
       #do stuff
    
        #trials data is added into myExp automatically
       trials.addData(‘resp’,response) #is added into myExp automatically
       trials.addData(‘RT’,thisRT) 
        myExp.nextEvent() #signals the end of this trial
    
    # no need to save data at the end - it will be handled automatically. Promise!

If you do decide there are some occasions where you don't want the data saved after all then you can call the ``abort()`` method of the ExperimentHandler.