from psychopy import misc, gui
import numpy as np
import matplotlib
matplotlib.use('WXAgg')
import pylab

"""this script will analyse a data file (or more than one) that you select

take a look at the print statements to see how to investigate what the
data objects are
"""

files = gui.fileOpenDlg()

congInds = range(12,24)
inCongIds = range(0,12)
SOAs = [0,0.1,0.2,0.3,0.4,0.5]

for filename in files:
    datFile = misc.fromFile(filename)
    datFile.abort()
    trials = datFile.loops[0]
    
    print 'dir(trials):', dir(trials) #reveals an attribute called data
    print 'what is trials.data:', type(trials.data) #NB a DataHandler? Hmmm
    print 'what can it do?:', dir(trials.data) #it looks like dict
    print 'trials.data keys:', trials.data.keys()
    RTs = trials.data['RT']
    print 'what is RTs:', type(RTs) # a numpy array
    print 'RTs.shape:', RTs.shape#
    
    congRTs = RTs[congInds, :]#fetch congruent trials
    #separate red and green
    congRed = congRTs[0:6,:]
    congGreen = congRTs[6:,:]
    #recobine red and green congruent trials
    allCongRTs = np.concatenate( (congRed, congGreen), 1)
    
    incongRTs = RTs[inCongIds,:]
    incongRed = incongRTs[0:6,:]
    incongGreen = incongRTs[6:,:]
    allInCongRTs = np.concatenate( (incongRed, incongGreen), 1)
    print 'allInCongRTs.shape:', allInCongRTs.shape
    
    inconMeans = np.mean(allInCongRTs, 1)
    inCongStdErr = np.std(allInCongRTs, 1)/np.sqrt(allInCongRTs.shape[1])
    congMeans = np.mean(allCongRTs, 1)
    congStdErr = np.std(allCongRTs, 1)/np.sqrt(allCongRTs.shape[1])
    
    pylab.errorbar(SOAs, inconMeans, color='r', yerr=inCongStdErr)
    pylab.errorbar(SOAs, congMeans, color='b', yerr=congStdErr)
    pylab.show()
    