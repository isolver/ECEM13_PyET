# -*- coding: utf-8 -*-
"""
This source file can be found in demos\coder\getting_started.py

Demonstrates the ioHub Common EyeTracking Interface core functionality only:
    A) Initial ioHub with an Eye Tracker device.
    B) Perform the Eye Tracker Setup logic ( resulting in a Calibrated ET system if all goes well)
    C) Start Recording Eye Data
    D) Print Last Received Eye Event every 0.25 sec.
    E) Stop Recording Eye Data when the SPACE key is pressed.
    F) Close the Eye Tracker Device.
    G) End the Demo
    
For a more complete example of how to code a more realistic experiment structure
using CODER, please see the gc_window example in this directory.

Inital Version: August 1st, 2013, Sol Simpson
"""

from psychopy.iohub import EventConstants,launchHubServer

# First we need to provide non default device settings. Common devices that
# need configuration are the Display and Eye Tracker devices.
# Here we define the settings in python dictionary format. They can also be read from
# a .yaml configuration file, but here we are keeping the file count to one.
#
devices={u'Display': 
            {
            u'name': u'display', 
            u'device_number': 0, 
            u'default_eye_distance': {
                u'surface_center': 500,
                u'unit_type': u'mm', 
                }, 
            u'physical_dimensions': {
                u'width': 590, 
                u'height': 340,
                u'unit_type': u'mm', 
                }, 
            u'reporting_unit_type': u'pix',
            u'psychopy_monitor_name': u'default', 
            },
            
        u'eyetracker.hw.sr_research.eyelink.EyeTracker':
            {
            u'name': u'tracker', 
            u'network_settings': u'100.1.1.1', 
            u'save_events': True, 
            u'stream_events': True, 
            u'monitor_event_types': [u'MonocularEyeSampleEvent', u'BinocularEyeSampleEvent', u'FixationStartEvent', u'FixationEndEvent', u'SaccadeStartEvent', u'SaccadeEndEvent', u'BlinkStartEvent', u'BlinkEndEvent'],
            u'enable_interface_without_connection': True, 
            u'simulation_mode': False, 
            u'calibration': 
                {
                u'type': u'NINE_POINTS', 
                u'auto_pace': True, 
                u'pacing_speed': 1.5, 
                u'screen_background_color': [128, 128, 128, 255], 
                u'target_type': u'CIRCLE_TARGET',
                u'target_attributes': 
                    {
                    u'inner_diameter': 6, 
                    u'outer_color': [255, 255, 255], 
                    u'inner_color': [0, 0, 0], 
                    u'outer_diameter': 33
                    }, 
                }, 
            u'device_timer': 
                {
                u'interval': 0.001
                }, 
            u'runtime_settings': 
                {
                u'sampling_rate': 1000, 
                u'vog_settings': 
                    {
                    u'pupil_measure_types': u'PUPIL_AREA', 
                    u'pupil_center_algorithm': u'CENTROID_FIT', 
                    u'tracking_mode': u'PUPIL_CR_TRACKING'
                    }, 
                u'sample_filtering': 
                    {
                    u'FILTER_ONLINE': u'FILTER_OFF'
                    }, 
                u'track_eyes': u'RIGHT_EYE'
                }, 
            u'model_name': u'EYELINK 1000 TOWER'
            },
            
#        u'eyetracker.hw.smi.iviewx.EyeTracker': 
#            {
#            u'name': u'tracker', 
#            u'stream_events': True, 
#            u'save_events': True, 
#            u'monitor_event_types': [u'BinocularEyeSampleEvent', u'FixationStartEvent', u'FixationEndEvent'],
#            u'calibration': 
#                {
#                u'show_validation_accuracy_window': True, 
#                u'auto_pace': True, 
#                u'type': u'FIVE_POINTS', 
#                u'screen_background_color': 20, 
#                u'pacing_speed': u'FAST', 
#                u'target_attributes': 
#                    {
#                    u'target_inner_color': u'RED', 
#                    u'target_size': 30, 
#                    u'target_color': 239
#                    }, 
#                u'target_type': u'CIRCLE_TARGET'
#                }, 
#            u'network_settings': 
#                {
#                u'send_ip_address': u'127.0.0.1', 
#                u'receive_ip_address': u'127.0.0.1', 
#                u'send_port': 4444, 
#                u'receive_port': 5555
#                }, 
#            u'device_timer': 
#                {
#                u'interval': 0.002
#                }, 
#            u'runtime_settings': 
#                {
#                u'sampling_rate': 60, 
#                u'vog_settings': 
#                    {
#                    u'pupil_measure_types': u'PUPIL_DIAMETER'
#                    }, 
#                u'sample_filtering': 
#                    {
#                    u'FILTER_ALL': u'FILTER_OFF'
#                    }, 
#                u'track_eyes': u'BINOCULAR_AVERAGED'
#                }, 
#            u'model_name': u'REDm',
#            u'event_buffer_length': 1024, 
#            }
    }
# Now start the ioHub process, passing in the device dictionary defined above.
#
io=launchHubServer(**devices)

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
    gpos=eyetracker.getPosition()
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
