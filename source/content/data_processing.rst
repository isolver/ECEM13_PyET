.. _dataProcessing:

Processing Recorded Eye Data
=============================

This section of the workshop will cover some common areas of eye data 
processing, including: 

1. Pixel to Visual Angle Conversion
2. Filtering Out High Frequency Noise
3. Velocity and Accelleration Calculation
4. Parsing Eye Sample Data into Eye Events


1. Pixel to Visual Angle Conversion
------------------------------------

When using PsychoPy and the ioHub the experiment creator can specify that position
information should be represented in one of several coordinate spaces, including 
pixels and visual degrees. When visual degrees are specified, stimuli are
drawn using visual degree coordinates and sizes, and position data returned by
devices capable of doing so (like the mouse or an Eye Tracker), will also
report position in visual degrees.

In some cases you may wish to use pixels for the coordinate space in your experiment,
but convert the eye position data to visual degrees after the data has been collected.
Examples of this include wanting to use a different pixel to visual degree
calculation, unknown eye to calibration plane distance during recording, or in
the case of experiments do not require the head to be fixed, situations where
the eye to display distance varies over time, and is reported as such by either a
hear tracking device, or some of the remote eye tracking systems available.

In situations like the able, using the example code provide here will allow the conversion
of pixel data to angle data; either using a fixed eye to calibration plain distance,
or a varying distance based on data in an array that is the same length as the 
pixel position data being processed.

.. literalinclude:: python_source/data_processing/pixels2angle.py
    :language: python

Example Plot
^^^^^^^^^^^^^^

Eye Position Traces in Pixel and Visual Degree Coordinates

.. image:: ./pix2deg.png
    :width: 600px
    :align: center
    :height: 400px
    :alt: Eye Position Traces in Pixel and Visual Degree Coordinates.

