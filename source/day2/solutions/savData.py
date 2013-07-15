#Creating stimuli (P4N - March 2013)

from psychopy import visual, core, data, event
import random, time

#Defining some parameters
repetitions = 1
displayT = 0.3

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
trials = data.TrialHandler(stimList, nReps =repetitions)
trials.data.addDataType('RT') #What you want to save at the end of the experiment
trials.data.addDataType('Response')

#Create a clock to measure RT
trialClock = core.Clock()

instructions = visual.TextStim(myWin, text = 'If you see a green dot press 1, if you see a red dot press 2. \n Press any key when you are ready to continue')
instructions.draw()
myWin.flip()
event.waitKeys()

#A loop to go through the conditions
for thisTrial in trials:
    #Randomise the position of the cue and stimulus
    side = random.choice([5.0, -5.0]) 
    cue.setPos([side, 0.0])
    stim.setPos([side, 0.0])
    
    #set the colour of the stimulus
    stim.setLineColor(thisTrial['stimColor'])
    stim.setFillColor(thisTrial['stimColor'])
    
    #draw the fixation and cue for 300ms
    fixation.draw()
    if thisTrial['cue']==1:
        cue.draw()
    myWin.flip()
    core.wait(displayT)

    #draw just fixation for 300ms
    fixation.draw()
    myWin.flip()
    core.wait(thisTrial['SOA'])

    #draw fixation and stimulus for 300ms
    fixation.draw()
    stim.draw()
    trialClock.reset() #reset the clock so it only measures the interval after the stimulus is presented.
    myWin.flip()
    core.wait(displayT)
    
    fixation.draw() #turn the stimulus off again
    myWin.flip()
    
    thisResp = None
    while thisResp==None: #While there isn't a response wait
        keys = event.waitKeys()
        
        for key in keys: #As waitKeys produces a list we need to look at the item in the list
            if key in ['q', 'escape']:
                core.quit() #It is useful to have a statement like this so you can end the program early
            
            elif key in ['num_1', 'num_3']:
                if key in ['num_1']:
                    thisResp = 1
                if key in ['num_3']:
                    thisResp = 0
            
            else:
                print 'Please press 1 or 3 on the number pad. You pressed %s' %key

    thisRT = trialClock.getTime() #get the reaction time
    
    #collect the data for this trial
    trials.data.add('RT', thisRT)
    trials.data.add('Response', thisResp)

#Saving data
date = time.strftime("%b%d_%H%M", time.localtime()) #Generating the date and time to uniquely identify our file
fName = 'InhibitionOfReturn_%s' %date #Creating the file name

trials.saveAsExcel(fileName=fName, sheetName='rawData', stimOut = ['stimList'], dataOut = ('n', 'all_mean', 'all_std', 'all_raw'))
trials.saveAsPickle(fileName=fName)



