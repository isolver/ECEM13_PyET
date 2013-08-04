
.. _traceplot:

***************************************
Plotting Eye Position Traces
***************************************

The basic steps involved in plotting eye position traces collected from an eye tracker
via the ioHub Common Eye Tracker Interface are:

1. Read Data From ioDataStore
2. Identify Missing Sample Data Periods (i.e. from Blinks, Eye Occlusion, and Other Causes of Eye Tracking Loss)
3. Plot the Data (we will use Matplotlib)

The following code example outlines these steps. It is assumed that you are running 
matplotlib using the windowed graph viewer.

.. literalinclude:: python_source/data_visualization/sample_trace_plot.py
    :language: python

Example Plots
-------------------

Left and Right Eye Position Traces using MatPlotLib

.. image:: ./eye_position_traces.png
    :width: 485px
    :align: center
    :height: 360px
    :alt: Left and Right Eye Position Traces using MatPlotLib
    

Same Plot as above, zoomed into a Two Second Interval of Eye Position Data

.. image:: ./eye_position_traces_zoomed.png
    :width: 485px
    :align: center
    :height: 360px
    :alt: Same Plot as above, Zoomed into a Two Second Interval of Eye Position Data
    
   