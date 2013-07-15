from psychopy import visual, core, event, data, gui
import numpy as np

dateStr = data.getDateStr()
info = {}
info['subj'] = ''
infoDlg = gui.DlgFromDict(info)
if infoDlg.OK: #this will be True (user hit OK) or False (cancelled)
    print info
else: 
    print 'User Cancelled'
    core.quit()

#create a window
win = visual.Window([800,600], units='deg', monitor='testMonitor')
#initialise some stimuli
fixation = visual.GratingStim(win, mask='circle', tex=None, size=0.1, color='white')
fixation.setAutoDraw(True)
target = visual.GratingStim(win, mask='circle', tex=None, 
                pos = [4,0], size=0.5, color='red')
cue = visual.Rect(win, width=2, height=2, pos = [4,0])
trialClock = core.Clock()

def checkKeys(keys, stimColor):
    """check whether the keypress was 'correct' """
    if 'q' in keys:
        core.quit()
    elif 'left' in keys and stimColor=='red':
        corr = 1
    elif 'left' in keys and stimColor=='green':
        corr = 0
    elif 'right' in keys and stimColor=='green':
        corr = 1
    elif 'right' in keys and stimColor=='red':
        corr = 0
    else:
        corr=None
    return corr

#set up conditions
conditions = data.importConditions('conditions.xlsx')
trials = data.TrialHandler(conditions, nReps=1, method='random', extraInfo=info, name='trials')
#create experiment handler
filename = '%s_%s' %(info['subj'], dateStr)
exp = data.ExperimentHandler(name='IOR',
                version='0.1',
                extraInfo=info,
                savePickle=True,
                saveWideText=True,
                dataFileName=filename)
exp.addLoop(trials)

for thisTrial in trials:
    SOA = thisTrial['SOA']
    cueSide = thisTrial['cue']
    side = round(np.random.rand())*2-1
    stimColor = thisTrial['stimColor']
    corr = None
    
    #present fixation
    for frameN in range(30):
        #fixation.draw()
        win.flip()

    #present cue
    cue.setPos([cueSide*side*4, 0])
    for frameN in range(18):
        cue.draw()
        win.flip()

    #onset asynchrony
    for frameN in range(int(SOA*60)):
        win.flip()

    #present stimuli
    trialClock.reset()
    event.clearEvents()
    target.setPos([side*4, 0])
    target.setColor(thisTrial['stimColor'])
    for frameN in range(int(0.3*60)):
        if corr == None:
            keys = event.getKeys(keyList=['left','right','q'])
            corr = checkKeys(keys, stimColor)
            rt = trialClock.getTime()
        target.draw()
        win.flip()

    #present fixation and wait for further response if needed
    win.flip()#fixation is being drawn automatically
    #check for keys
    if corr == None:
        keys = event.waitKeys(keyList=['left','right','q'])
        corr = checkKeys(keys, stimColor)
        rt = trialClock.getTime()
        
    trials.addData('rt',rt)
    trials.addData('corr',corr)
    exp.nextEntry()
