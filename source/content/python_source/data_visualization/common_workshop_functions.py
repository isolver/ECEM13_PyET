# Python Source File Available in python_source/data_visualization/common_workshop_functions.py

import numpy as np

def processSampleEventGaps(x,y,pupil,missing_points_marray,gap_fill_operation='clear'):
    valid_data_periods=np.ma.extras.notmasked_contiguous(
                                np.ma.array(pupil, mask=missing_points_marray)
                                )                                
    if gap_fill_operation == 'linear':
        # Linear fill in for data processing / filtering continuity
        #
        fill_in_data_arrays=[x,y]           
        for data_array in fill_in_data_arrays:        
            data_array[0:valid_data_periods[0].start]=data_array[valid_data_periods[0].start]
            last_slice_end=valid_data_periods[0].stop
            for data_slice in valid_data_periods[1:]:
                invalid_1=last_slice_end
                invalid_2=data_slice.start
                valcount=(invalid_2-invalid_1)
                # fill
                startval=data_array[invalid_1-1]
                endval=data_array[invalid_2]
                last_slice_end=data_slice.stop
                #display("{}:{}, {}:{}, {}, {}".format(invalid_1,invalid_2,startval,endval,valcount,(endval-startval)/valcount))
                if endval==startval:
                    data_array[invalid_1:invalid_2]=endval
                else:
                    data_array[invalid_1:invalid_2]=np.arange(startval,endval,(endval-startval)/valcount)[0:valcount]
        pupil[missing_points_marray]=0
    elif gap_fill_operation=='clear':
        fill_in_data_arrays=[x,y]           
        for data_array in fill_in_data_arrays:        
            data_array[missing_points_marray]=np.NaN
        pupil[missing_points_marray]=0        
    return valid_data_periods


