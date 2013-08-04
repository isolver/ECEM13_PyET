# This Python Source File Available in python_source/data_visualization/gaze_overlay_animation.py

from psychopy.iohub.datastore.util import ExperimentDataAccessUtility
from psychopy.iohub import EventConstants

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import animation

from common_workshop_functions import processSampleEventGaps

import numpy as np

plt.close()

##### STEP A. #####
# Load an ioDataStore file containing 1000 Hz sample data from a 
# head supported eye tracker that was recording the right eye. 
dataAccessUtil=ExperimentDataAccessUtility('..\hdf5_files',
                                           'head_supported_data.hdf5', 
                                           experimentCode=None,
                                           sessionCodes=[])

# For the demo, we will playback the eye position of one trial only.
#
TRIAL_ID=1

# Specify the sampling rate of the data collected, so the proper playback rate
# can be calculated.
#
et_sampling_rate=1000.0

# In msec, 1000/desired_playback_rate ~= desired frame rate in Hz.
# So we are asking for 50 Hz playback frame rate here.
#
desired_playback_rate=20

# Retrieve a subset of the BINOCULAR_EYE_SAMPLE event attributes, for events that occurred
# between each time period defined by the TRIAL_START and TRIAL_END trial variables of each entry
# in the trial_conditions data table.
#
event_type=EventConstants.MONOCULAR_EYE_SAMPLE
retrieve_attributes=('time','gaze_x','gaze_y','pupil_measure1','status')
trial_event_data=dataAccessUtil.getEventAttributeValues(event_type,
                            retrieve_attributes,
                            conditionVariablesFilter=None, 
                            startConditions={'time':('>=','@TRIAL_START@')},
                            endConditions={'time':('<=','@TRIAL_END@')})

# No need to keep the hdf5 file open anymore...
#
dataAccessUtil.close()

# Get the data for the trial we will playback
#
trial_data=trial_event_data[TRIAL_ID]

##### STEP B. #####
# Same drill as other plot examples so far.
#
# Eye manufacturer specific missing data indicator
#
invalid_data_mask=trial_data.pupil_measure1==0

# Get the needed left eye sample arrays 
#
gaze_x=trial_data.gaze_x
gaze_y=trial_data.gaze_y
pupil_size=trial_data.pupil_measure1
# get the array of sample times for the current trial
#
time=trial_data.time

# Process the eye fields using the processSampleEventGaps function defined
# in the common_workshop_functions.py file. 
#
valid_data_periods=processSampleEventGaps(gaze_x,gaze_y,
                                               pupil_size,
                                               invalid_data_mask,
                                               'clear')

##### STEP C. #####       
# Load the image used in the current trial.                                        
# get the trial condition values used for each trial in example experiment.
#
condition_set=trial_data.condition_set 
# Get the image name used for display during the trial
#
image_name=condition_set.IMAGE_NAME
trial_id=condition_set.trial_id

# load the image as a numpy 3D array
#
trial_image_array=np.flipud(mpimg.imread("./images/"+image_name))

# Get background image size
# divide by two to make the plate 50% scale
#
image_size=(trial_image_array.shape[1]/2,trial_image_array.shape[0]/2)

ihw,ihh=image_size[0]/2,image_size[1]/2

##### STEP D. #####
# Create the Animated Figure
#   
dpi = 100
margin = 0.05 # (5% of the width/height of the figure...)
xpixels, ypixels = image_size
# Make a figure big enough to accomodate an axis of xpixels by ypixels
# as well as the ticklabels, etc...
#
figsize = (1 + margin) * xpixels / dpi, (1 + margin) * ypixels / dpi
fig = plt.figure(figsize=figsize, dpi=dpi)
plt.title("Trial {0}: {1}".format(trial_id,image_name))
# Make the axis the right size...
#
ax = fig.add_axes([margin, margin, 1 - 3*margin, 1 - 3*margin])

# Draw the background image array
#
ax.imshow(trial_image_array,origin='lower',extent=(-ihw, ihw,-ihh, ihh))

# Create a circle graphic to use as the gaze overlay cursor.
#
circle = plt.Circle((1000, 1000), radius=9, facecolor='r',edgecolor='y', 
                    linewidth=2, alpha=0.7)
# Create a text box to display the current trial time.
#
time_text = ax.text(0.02, 0.95, '', color='black', fontsize=12, 
                    bbox={'facecolor':'red', 'alpha':0.5, 'pad':10},
                    transform=ax.transAxes)

# Calculate the eye trackers sampling rate in msec.
#
ifi=1000.0/et_sampling_rate
# Calculate how many samples occur within the requested playback rate.
#
sample_frame_interval=desired_playback_rate//ifi+1
# Since this will never be what was requested, calculate the actual playback 
# rate so an int number of eye tracker samples occur within each animate frame.
#
actual_playback_rate=int(sample_frame_interval*ifi)
# Calculate how many frames the animate conitains based on the number of 
# eye tracking samples available and the sample frame interval.
#
sample_frame_count=int(len(time)//sample_frame_interval)

# Create the matplotlib Animation object
#
def init():
    """
    This gets called each time the animation first starts.
    You must return any of the plot graphics that change
    Each frame of the animateion.
    """
    ax.add_patch(circle)
    time_text.set_text('time = %.1f sec' % time[0])
    return circle,time_text

def animate(i):
    """
    This gets called each frame of the animation.
    This is where the animated graphics can be updated for the next frame.
    You must return any of the plot graphics that change
    Each frame of the animateion.
    """
    s=int(i*sample_frame_interval)
    circle.center = (gaze_x[s]/2., gaze_y[s]/2.)
    time_text.set_text('time = %.1f sec' % time[s])
    return circle,time_text

# Start the animation, but only play it for 1 frame
# (This gets around a current bug in the matplotlib anaimation code when
# you want to use blit=True during the real playback; which you do as it is
# 10x faster than when blit=False)
#
anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=1, 
                               interval=actual_playback_rate,
                               blit=False)

# Start the animation for real this time. Based on the args provided,
# the animation will play from start to finish and then loop to the
# start and play over again. This repeats until you close the matplotlib window.
#
anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=sample_frame_count, 
                               interval=actual_playback_rate,
                               blit=True)

plt.show()
                             
# It is also possible to save the animation as a video file,
# Check out http://nickcharlton.net/posts/drawing-animating-shapes-matplotlib.html
                               