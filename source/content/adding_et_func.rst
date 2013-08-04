.. _eyetrackingPsychoPy:

1:00 - 1:40pm: Incorporating Eye tracking into PsychoPy Experiments
==========================================================================

To add eyetracking into your study you'll need to set up the config file (this is hardware-dependent), run a calibration routine, and then insert some simple code into your script or Builder experiment.

*******************************
Config files
*******************************

These are yaml files. Aren't they super-simple?!

*******************************
Calibrating your eyetracker
*******************************

Something here about the interface to the calib routines

*******************************
Using from Coder
*******************************

Some MINIMAL code to get running (like the coder demo but less)

*******************************
Using from Builder
*******************************

There isn't currently an Eyetracker Component in Builder (I'm sure there will be very soon!) but you can effectively create one yourself using a code component. Remember, these have 5 sections for `Beginning the Experiment`, `Beginning the Routine` (e.g. trial), `Each Frame` of the Routine, `End of the Routine` and `End of the Experiment`.

The way we've set up the demos is that they check first whether you've asked for an eye tracker to be used - in `Experiment Settings` we added an entry to the experiment info dialog box called 'Eye tracker'. In the code below, if that is set to be a string that represents a valid yaml config file then we'll have an eyetracker installed and if not we'll revert to using the mouse as before (handy while creating the experiment inyor office!).


Stroop: 
-----------

We'll look at these steps for a new version of the Stroop task where we simply check whether fixation was maintained during the trial and flag trials where it was broken (at any point).

Begin the Experiment
~~~~~~~~~~~~~~~~~~~~~~~~~

Here we need to import and launch the ioHub server and set up some default values for the rest of the experiment (like how large a window we think is reasonable for fixation to be maintained)::

    maintain_fix_pix_boundary=66.0
    eyetracker = False #will change if we get one!
    if expInfo['Eye Tracker']:
        from psychopy.iohub import launchHubServer,EventConstants
        io=launchHubServer()
        iokeyboard=io.devices.keyboard
        mouse=io.devices.mouse
        if io.getDevice('eyetracker'):
            eyetracker=io.getDevice('eyetracker')
        display_gaze=False #decide whether to show the current gaze location
        x,y=0,0 #will be changed later

Notes:
    - We only import ioHub and set it up if it will be needed!
    - We should create initial values here for things that will be updated during the script (like the current x,y so that other parts of the script won't throw an error if they use them before the first time the true values are determined)
    - the
    
Begin the Routine
~~~~~~~~~~~~~~~~~~~~~~~~~

Simple code that runs if the eyetracker exists (remember, that started as False but was then assigned an eyetracker object if one was successfully created)::

    if eyetracker:
        heldFixation = True #unless otherwise
        io.clearEvents('all')
Notes:
    - at the beginning of the trial we create a variable `heldFixation` and set it to be True. We'll check on each frame if it stays true but this is our default.
    - clearing events means we don't worry what happened before the trial started

Each Frame
~~~~~~~~~~~~~~~~

Now we need to check whether gaze has strayed outside the valid fixation window. But we'll also check whether the user pressed 'g' and if so we'll toggle the `display_gaze` variable.

    if eyetracker:
    
        # get /eye tracker gaze/ position 
        x,y=eyetracker.getPosition()
        d=np.sqrt(x**2+y**2)
        if d>maintain_fix_pix_boundary:
            heldFixation = False #this had a default of True, remember?
            
        # check for 'g' key press to toggle gaze cursor visibility
        iokeys=iokeyboard.getEvents(EventConstants.KEYBOARD_PRESS)
        for iok in iokeys:
            if iok.key==u'g':
                display_gaze=not display_gaze

End of Routine
~~~~~~~~~~~~~~~~~~~~

This is some simple code at the end of the trial that uses the standard data outputs of PsychoPy - a column will appear in the excel/csv file showing whether fixation was held on each trial::

    if eyetracker:
        #add eye-track data to data file
        trials.addData("heldFixation", heldFixation)
        
End Experiment
~~~~~~~~~~~~~~~~~~~~

ioHub runs in a separate process. It's good to shut that down just in case it fails to do so itself!::

    if expInfo['Eye Tracker']:
        io.quit()

Gaze cursor
~~~~~~~~~~~~~~~~

How do we make use of that `display_gaze` variable to show where the gaze is currently located? Simple! We add a `Grating Component` (for example) that has:
    - a small size
    - an opacity of `$display_gaze`. That means it uses the display_gaze variable (which is True=1, False=0). Make sure you `set every frame`
    - a location of `$[x,y]`. Make sure you `set every frame`