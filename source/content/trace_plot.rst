
.. _traceplot:

***************************************
Plotting Eye Position Traces
***************************************

The basic steps involved in plotting eye position traces collected from an eye tracker
via the ioHub Common Eye Tracker Interface are:

1. Read Data From ioDataStore
2. Identify Missing Sample Data Periods (i.e. from Blinks, Eye Occlusion, and Other Causes of Eye Tracking Loss)
3. Plot the Data (we will use Matplotlib)

The following code example outines these steps. It is assumed that you are running 
matplotlib using the windowed graph viewer.

.. literalinclude:: python_source/data_visualization/sample_trace_plot.py
    :language: python
