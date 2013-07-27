# -*- coding: utf-8 -*-
"""
Misc. Python functions for use during the ECEM Py4ET 2013 workshop.

Free to use in any way by any one.
"""

import psychopy.iohub
from psychopy.iohub.datastore.util import displayDataFileSelectionDialog, ExperimentDataAccessUtility
from psychopy.iohub import EventConstants

import os
import sys

import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import scipy.signal
import scipy.stats
import numpy as np

orginal_plt_width=None
orginal_plt_height=None

def _temp():
    pass
    
def loadSampleData(event_type=EventConstants.BINOCULAR_EYE_SAMPLE):
    # Open an ioDataStore HDF5 file.
    #
    data_file_path= displayDataFileSelectionDialog(psychopy.iohub.module_directory(_temp))  
    if data_file_path is None:
        sys.exit(0)
    dpath,dfile=os.path.split(data_file_path)           

    # Create an instance of the ExperimentDataAccessUtility class
    # for the selected DataStore file. This allows us to access data
    # in the file based on Device Event names and attributes.
    #
    dataAccessUtil=ExperimentDataAccessUtility(dpath,dfile, experimentCode=None,sessionCodes=[])
    
    # Retrieve a subset of the BINOCULAR_EYE_SAMPLE event attributes, for events that occurred
    # between each time period defined by the TRIAL_START and TRIAL_END trial variables of each entry
    # in the trial_conditions data table.
    #
    if event_type==EventConstants.BINOCULAR_EYE_SAMPLE:
        retrieve_attributes=['time','left_gaze_x','left_gaze_y','right_gaze_x','left_pupil_measure1',
                                 'right_gaze_y','right_pupil_measure1','status']
    else:
        retrieve_attributes=['time','gaze_x','gaze_y','pupil_measure1','status']
                             
    session_trial_sample_data=dataAccessUtil.getEventAttributeValues(event_type,
                                retrieve_attributes,
                                conditionVariablesFilter=None, 
                                startConditions={'time':('>=','@TRIAL_START@')},
                                endConditions={'time':('<=','@TRIAL_END@')})
    
    
    dataAccessUtil.close()
    return session_trial_sample_data
    
def plotResults(trial_id,time,data_set_1,data_set_2,fig_title='',fig2_title='',ylabel='Position (pixels)',ds1_label_pref=' Horizontal Position',ds2_label_pref=' Vertical Position'):
    plt.clf()
    
    left_x,left_y,left_pupil,right_x,right_y,right_pupil=data_set_1
    if data_set_2 is not None:
        left_x_sg,left_y_sg,right_x_sg,right_y_sg=data_set_2
    
    fig = plt.figure()
    ax2 = fig.add_subplot(212)
    ax1 = fig.add_subplot(211,sharex=ax2)
    if left_x is not None:
        ax1.plot(time,left_x,label=ds1_label_pref)
    if left_y is not None:
        ax1.plot(time,left_y,label=ds1_label_pref)
    if data_set_2 is not None:
        if left_x_sg is not None:
            ax1.plot(time,left_x_sg,label=ds2_label_pref)
        if left_y_sg is not None:
            ax1.plot(time,left_y_sg,label=ds2_label_pref)
    
    if right_x is not None:    
        ax2.plot(time,right_x,label=ds1_label_pref)
    if right_y is not None:
        ax2.plot(time,right_y,label=ds1_label_pref)
    if data_set_2 is not None:
        if right_x_sg is not None:    
            ax2.plot(time,right_x_sg,label=ds2_label_pref)
        if right_y_sg is not None:    
            ax2.plot(time,right_y_sg,label=ds2_label_pref)
    ax2.set_xlabel('Time')

    ax1.set_ylabel(ylabel)
    ax2.set_ylabel(ylabel)

    ax1.set_title(fig_title)
    ax2.set_title(fig2_title)
    tmin=time.min()//1
    tmax=time.max()//1+1
    #trange=tmax-tmin
    plt.xticks(np.arange(tmin,tmax,0.5),rotation='vertical')

    trans1 = mtransforms.blended_transform_factory(ax1.transData, ax1.transAxes)
    trans2 = mtransforms.blended_transform_factory(ax2.transData, ax2.transAxes)
    ax1.fill_between(time, 0, 1, where=left_pupil==0, facecolor='DarkRed', alpha=0.5, transform=trans1)
    ax2.fill_between(time, 0, 1, where=right_pupil==0, facecolor='DarkRed', alpha=0.5, transform=trans2)

    plt.legend()
    plt.show()
    
def handleTemporalGaps(tsamples):
    notmasked_contiguous=np.ma.extras.notmasked_contiguous
    marray=np.ma.array
    status=tsamples.status
    left_pupil_measure1=tsamples.left_pupil_measure1
    right_pupil_measure1=tsamples.right_pupil_measure1
    left_gaze_x=tsamples.left_gaze_x
    left_gaze_y=tsamples.left_gaze_y
    right_gaze_x=tsamples.right_gaze_x
    right_gaze_y=tsamples.right_gaze_y

    missing_left_indexes=status//10>=2
    missing_right_indexes=status%10>=2
    left_pupil_measure1[missing_left_indexes]=0
    right_pupil_measure1[missing_right_indexes]=0
    left_valid_data_periods=notmasked_contiguous(marray(left_pupil_measure1, mask=missing_left_indexes))
    right_valid_data_periods=notmasked_contiguous(marray(right_pupil_measure1, mask=missing_right_indexes))

    #Left eye fill in for filtering continuity
    left_gaze_x[0:left_valid_data_periods[0].start]=left_gaze_x[left_valid_data_periods[0].start]
    left_gaze_y[0:left_valid_data_periods[0].start]=left_gaze_y[left_valid_data_periods[0].start]
    last_slice_end=left_valid_data_periods[0].stop
    for data_slice in left_valid_data_periods[1:]:
        invalid_1=last_slice_end
        invalid_2=data_slice.start
        valcount=(invalid_2-invalid_1)
        # left_x
        startval=left_gaze_x[invalid_1-1]
        endval=left_gaze_x[invalid_2]
        left_gaze_x[invalid_1:invalid_2]=np.arange(startval,endval,(endval-startval)/valcount)[0:valcount]
        # left_y
        startval=left_gaze_y[invalid_1-1]
        endval=left_gaze_y[invalid_2]
        left_gaze_y[invalid_1:invalid_2]=np.arange(startval,endval,(endval-startval)/valcount)[0:valcount]
        last_slice_end= data_slice.stop
        
    #Right eye fill in for filtering continuity
    right_gaze_x[0:right_valid_data_periods[0].start]=right_gaze_x[right_valid_data_periods[0].start]
    right_gaze_y[0:right_valid_data_periods[0].start]=right_gaze_y[right_valid_data_periods[0].start]
    last_slice_end=right_valid_data_periods[0].stop
    for data_slice in right_valid_data_periods[1:]:
        invalid_1=last_slice_end
        invalid_2=data_slice.start
        valcount=(invalid_2-invalid_1)
        # left_x
        startval=right_gaze_x[invalid_1-1]
        endval=right_gaze_x[invalid_2]
        right_gaze_x[invalid_1:invalid_2]=np.arange(startval,endval,(endval-startval)/valcount)[0:valcount]
        # left_y
        startval=right_gaze_y[invalid_1-1]
        endval=right_gaze_y[invalid_2]
        right_gaze_y[invalid_1:invalid_2]=np.arange(startval,endval,(endval-startval)/valcount)[0:valcount]
        last_slice_end= data_slice.stop
    
    return missing_left_indexes,missing_right_indexes
    
class VisualAngleCalc(object):
    def __init__(self,display_size_mm,display_res_pix,eye_distance_mm=None):
        self._display_width=display_size_mm[0]
        self._display_height=display_size_mm[1]
        self._display_x_resolution=display_res_pix[0]
        self._display_y_resolution=display_res_pix[1]
        self._eye_distance_mm=eye_distance_mm
        
    def pix2deg(self,display_pos_x,display_pos_y=None,display_dim_x=None,display_dim_y=None,eye_distance_mm=None):
        """
        Stimulus positions (display_pos_x,display_pos_y) are defined in x and y pixel units, with the origin (0,0)
        being at the **center** of the display, as to match the PsychoPy pix unit coord type.
    
        Stimulus dimentions (display_dim_x,display_dim_y) are defined in pixels, representing the width, height of
        the stim area, with stim_xy being the origin. stim_dim_xy is optional.
    
        For example, a stim with a width,height of 100,100 pixels, centered on display pixel
        localation 200,200 (where 0,0 is the display center), would have:
            display_pos_xy=150,150
            display_dim_xy=100,100
        """
        if self._eye_distance_mm is None and eye_distance_mm is None:
            raise ValueError("The eye_distance_mm arguement must not be None as no default eye distance was provided for VisualAngleCalc.")
        eye_dist_mm=self._eye_distance_mm
        if eye_distance_mm is not None:
            eye_dist_mm=eye_distance_mm
            
        sx,sy=display_pos_x,display_pos_y
        
        thetaH1=np.degrees(np.arctan(sx/(eye_dist_mm*self._display_x_resolution/self._display_width)))
        
        if sy is not None:
            thetaV1=np.degrees(np.arctan(sy/(eye_dist_mm*self._display_y_resolution/self._display_height)))

        if display_dim_x:
            sw,sh=display_dim_x,display_dim_y
            thetaH2=np.degrees(np.arctan(((sw+sx)/(eye_dist_mm*self._display_x_resolution/self._display_width))))
            horz_degree_dist=thetaH2-thetaH1
            if display_dim_y:
                thetaV2=np.degrees(np.arctan(((sh+sy)/(eye_dist_mm*self._display_y_resolution/self._display_height))))
                vert_degree_dist=thetaV2-thetaV1
        
        if sy is not None:
            if display_dim_y:
                return (thetaH1,thetaV1),(horz_degree_dist,vert_degree_dist)
            else:
                return thetaH1,thetaV1
        else:
            if display_dim_x:
                return thetaH1,horz_degree_dist
            else:
                return thetaH1
                
def calculateVelocity(time,data_x,data_y=None,units='deg'):
    """
    Returns data in visual degrees.
    """
    if units=='pix':
        vac=VisualAngleCalc(display_size_mm=(500.0,300.0),display_res_pix=(1280.0,1024.0),eye_distance_mm=550.0)
        if data_y is None:
            data_x=vac.pix2deg(data_x)
        else:
            data_x=vac.pix2deg(data_x)
            data_y=vac.pix2deg(data_y)
            data=np.sqrt(data_x*data_x+data_y*data_y)
    else:
        if data_y is None:
            data=data_x
        else:
            data=np.sqrt(data_x*data_x+data_y*data_y)
        
    velocity_between = (data[1:]-data[:-1])/(time[1:]-time[:-1])
    velocity = (velocity_between[1:]+velocity_between[:-1])/2.0
    return velocity
    
def calculateAccelleration(time,data_x,data_y=None,units='deg'):
    """
    Returns data in visual degrees.
    """
    velocity=calculateVelocity(time,data_x,data_y,units)
    accel = calculateVelocity(time[1:-1],velocity)
    return accel