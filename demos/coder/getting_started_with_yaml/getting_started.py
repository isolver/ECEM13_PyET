# -*- coding: utf-8 -*-
"""
This source file can be found in demos\coder\getting_started.py

Demonstrates the ioHub Common EyeTracking Interface core functionality only:
    A) Initialize ioHub with an Eye Tracker device.
    B) Perform the Eye Tracker Setup logic ( resulting in a Calibrated ET system if all goes well)
    C) Start Recording Eye Data
    D) Print Last Received Eye Event every 0.25 sec.
    E) Stop Recording Eye Data when the SPACE key is pressed.
    F) Close the Eye Tracker Device.
    G) End the Demo
    
For a more complete example of how to code a more realistic experiment structure
using CODER, please see the gc_window example in this directory.
"""

from psychopy.iohub import EventConstants,ioHubConnection,load,Loader
from psychopy.data import getDateStr
import os

# Specify the iohub device config file to use for the
# demo. Here we are selecting the device config that includes the SMI eye tracker.
#
config_file_path=os.path.abspath('./SMI_iview_std.yaml')
print config_file_path
print

# Load the specified iohub configuration file
# converting it to a python dict.
#
io_config=load(file(config_file_path,'r'), Loader=Loader)

# Add / Update the session code to be unique. Here we use the psychopy
# getDateStr() function for session code generation
#
session_info=io_config.get('data_store').get('session_info')
session_info.update(code="S_{0}".format(getDateStr()))
print session_info
print
print io_config
# Create an ioHubConnection instance, which starts the ioHubProcess, and
# informs it of the requested devices and their configurations.
#        
io=ioHubConnection(io_config)

keyboard=io.devices.keyboard
eyetracker=io.devices.tracker
   
# Start by running the eye tracker default setup procedure.
# The details of the setup procedure (calibration, validation, etc)
# are unique to each implementation of the Common Eye Tracker Interface.
# All have the common end goal of calibrating the eye tracking system
# prior to data collection.
#
# Please see the eye tracker interface implementation details for the 
# hardware being used at:
# http://www.isolver-solutions.com/iohubdocs/iohub/api_and_manual/device_details/eyetracker.html#eye-tracking-hardware-implementations
#
eyetracker.runSetupProcedure()
            
# Start Recording Eye Data
#
eyetracker.setRecordingState(True)            

# Clear any events already in the iohub on-line event buffers
#        
io.clearEvents('all')

# While the space key is not pressed
#
while not [event for event in keyboard.getEvents(event_type_id=EventConstants.KEYBOARD_PRESS) if event.key == ' ']:
    # wait 1/4 second
    #
    io.wait(0.25)
    # Get any new events from the Eye Tracker
    #    
    et_events=eyetracker.getEvents()
    if et_events:    
        # If any events were received, print the last one.
        #        
        latest_event=et_events[-1]
        print latest_event
    # Lets also get the latest gaze position
    #
    gpos=eyetracker.getLastGazePosition()
    # And print it
    #
    print '** CURRENT GAZE POSITION: ',gpos

# Space key was pressed, so stop recording from the eye tracker 
# and disconnect it from the iohub.           
#
eyetracker.setRecordingState(False)                    
eyetracker.setConnectionState(False)

# quit the ioHub process
#
io.quit()
