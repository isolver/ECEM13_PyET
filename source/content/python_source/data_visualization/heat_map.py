# This Python Source File Available in python_source/data_visualization/heat_map.py

from psychopy.iohub.datastore.util import ExperimentDataAccessUtility
from psychopy.iohub import EventConstants

import matplotlib.pyplot as plt
import numpy as np

from common_workshop_functions import processSampleEventGaps


# Load an ioDataStore file containing 120 Hz sample data from a
# remote eye tracker that was recording both eyes. In the plotting example
dataAccessUtil=ExperimentDataAccessUtility('../hdf5_files','remote_data.hdf5', experimentCode=None,sessionCodes=[])

# A.
# Retrieve a subset of the BINOCULAR_EYE_SAMPLE event attributes, for events that occurred
# between each time period defined by the TRIAL_START and TRIAL_END trial variables of each entry
# in the trial_conditions data table.
#
event_type=EventConstants.BINOCULAR_EYE_SAMPLE
retrieve_attributes=('time','left_gaze_x','left_gaze_y','left_pupil_measure1',
               'right_gaze_x','right_gaze_y','right_pupil_measure1','status')
trial_event_data=dataAccessUtil.getEventAttributeValues(event_type,
                retrieve_attributes,
                conditionVariablesFilter=None,
                startConditions={'time':('>=','@TRIAL_START@')},
                endConditions={'time':('<=','@TRIAL_END@')})

# No need to keep the hdf5 file open anymore...
#
dataAccessUtil.close()

# Process and plot the sample data for each trial in the data file.
#
for trial_index,trial_samples in enumerate(trial_event_data):
    # B.
    # Find all samples that have missing eye position data and filter the eye position
    # and pupil size streams so that the eye track plot is more useful. In this case that
    # means setting position fields to NaN and pupil size to 0.
    #

    # left eye manufacturer specific missing data indicator
    left_eye_invalid_data_masks=trial_samples.status//10>=2
    # Right eye manufacturer specific missing data indicator
    right_eye_invalid_data_masks=trial_samples.status%10>=2

    # Get the needed left eye sample arrays
    #
    left_gaze_x=trial_samples.left_gaze_x
    left_gaze_y=trial_samples.left_gaze_y
    left_pupil_size=trial_samples.left_pupil_measure1

    # Process the left eye fields using the processSampleEventGaps function defined
    # in the common_workshop_functions.py file. The last arguement of 'clear'
    # tells the function to set any x or y position missing data samples to NaN
    # and to set the pupil size field to 0. The operations are preformed in-place
    # on the numpy arrays passed to the fucntion.
    # The returned valid_data_periods is a list of each group of temporally adjacent
    # samples that are valid, but providing a list where each element is the (start, stop)
    # index for a given period of valid data.
    #
    left_valid_data_periods=processSampleEventGaps(left_gaze_x,left_gaze_y,
                                                   left_pupil_size,
                                                   left_eye_invalid_data_masks,
                                                   'clear')

    # Get the needed right eye sample field arrays
    #
    right_gaze_x=trial_samples.right_gaze_x
    right_gaze_y=trial_samples.right_gaze_y
    right_pupil_size=trial_samples.right_pupil_measure1

    # Process the right eye fields
    #
    right_valid_data_periods=processSampleEventGaps(right_gaze_x,right_gaze_y,
                                                    right_pupil_size,
                                                    right_eye_invalid_data_masks,
                                                    'clear')

    # get the array of sample times for the current trial
    time=trial_samples.time

    # C.
    # Plot

    # TO BE COMPLETED