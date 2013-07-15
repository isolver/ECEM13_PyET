#Creating stimuli (P4N - March 2013)

from psychopy import visual, event, core

#Create a window
myWin = visual.Window(size = (800,600), monitor = 'testMonitor', units = 'deg',
        fullscr=False, allowGUI=True, bitsMode=None)

#Create fixation, cue and stimulus
fixation = visual.GratingStim(myWin, tex=None, units = 'deg', size = 0.2, mask = 'circle', color = 'black')
cue = visual.Rect(myWin, width = 2.0, height = 2.0, units = 'deg', lineColor = 'black', pos = (5.0, 0.0))

#draw the fixation and cue for 300ms
fixation.draw()
cue.draw()
myWin.flip()
core.wait(0.3)

#draw just fixation for 300ms
fixation.draw()
myWin.flip()
core.wait(0.3)
