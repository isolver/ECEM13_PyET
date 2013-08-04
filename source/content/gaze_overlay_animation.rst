
.. _gazeoverlay:

**********************
Animated Gaze Overlay 
**********************

Here we illustrate a cute, but perhaps not so scientifically useful, 
animated gaze position overlay cursor.

The basic steps involved in creating an Animated Gaze Overlay
using eye data from the ioDataStore:

A. Load the eye sample data from the ioDataStore.
B. Clean position and pupil data for samples tagged as having missing eye data.
C. Load the background image used for the trial selected for the gaze overlay playback.
D. Create the matplotlib animated figure, including the gaze overlay graphic.
E. Start the animation.

.. literalinclude:: python_source/data_visualization/gaze_overlay_animation.py
    :language: python
