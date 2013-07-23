#Creating stimuli (P4N - March 2013)

from psychopy import visual, core, data
import random

#Create a window
myWin = visual.Window(size = (800,600), monitor = 'testMonitor', units = 'deg',
        fullscr=False, allowGUI=True, bitsMode=None)

#Create fixation, cue and stimulus
fixation = visual.GratingStim(myWin, tex=None, units = 'deg', size = 0.2, mask = 'circle', color = 'black')
cue = visual.Rect(myWin, width = 2.0, height = 2.0, units = 'deg', lineColor = 'black', pos = (5.0, 0.0))
stim = visual.Circle(myWin, radius = 0.5, units = 'deg', lineColor = 'red', fillColor = 'red', pos = (5.0, 0.0))

#Import conditions list
stimList = data.importConditions('conditions.xlsx')

#Create a TrialHandler object which uses stimList
trials = data.TrialHandler(stimList, nReps = 5)
trials.data.addDataType('RT') #What you want to save at the end of the experiment
trials.data.addDataType('Response')
trials.data.addDataType('stimColor')

#A loop to go through the conditions
for thisTrial in trials:
    #Randomise the position of the cue and stimulus
    side = random.choice([5.0, -5.0]) 
    cue.setPos([side, 0.0])
    stim.setPos([side, 0.0])
    
    #draw the fixation and cue for 300ms
    fixation.draw()
    if thisTrial['cue']==1:
        cue.draw()
    myWin.flip()
    core.wait(0.3)

    #draw just fixation for 300ms
    fixation.draw()
    myWin.flip()
    core.wait(thisTrial['SOA'])

    #draw fixation and stimulus for 300ms
    fixation.draw()
    stim.draw()
    myWin.flip()
    core.wait(0.3)

