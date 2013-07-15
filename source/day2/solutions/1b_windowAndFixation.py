#Creating stimuli (P4N - March 2013)

from psychopy import visual, event, core

#Create a window
myWin = visual.Window(size = (800,600), monitor = 'testMonitor', units = 'deg',
        fullscr=False, allowGUI=True, bitsMode=None)

#Create fixation
fixation = visual.GratingStim(myWin, tex=None, units = 'deg', size = 0.2, mask = 'circle', color = 'black')

#draw the fixation and cue for 300ms
fixation.draw()
myWin.flip()
core.wait(0.3)
