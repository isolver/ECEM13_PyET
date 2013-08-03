******************************************
The ioHub Common Eye Tracker Interface
****************************************** 

The API details for the ioHub EyeTracker device can be found `here <http://www.isolver-solutions.com/iohubdocs/iohub/api_and_manual/device_details/eyetracker.html#the-iohub-common-eye-tracker-interface>`_

The Common Eye Tracking Interface provides the same user level Python API for all supported eye tracking hardware, meaning:

* The same experiment script can be run with any supported eye tracker hardware.
* The eye event types supported by an eye tracker implementation are saved using the same format regardless of eye tracker hardware.

Currently Supported Eye Tracking Systems
=========================================

* **LC Technologies** EyeGaze and EyeFollower models.
* **SensoMotoric Instruments** iViewX models.
* **SR Research** EyeLink models.
* **Tobii Technologies** Tobii models.

Visit the ioHub documentation for `Eye Tracking Hardware Implementations <http://www.isolver-solutions.com/iohubdocs/iohub/api_and_manual/device_details/eyetracker.html#eye-tracking-hardware-implementations>`_ for details on each implementation.

Areas of Functionality
======================

1. **Initializing the Eye Tracker / Setting the Device State.**
2. **Performing Calibration / System Setup.**
3. **Starting and Stopping of Data Recording.**
4. Sending Messages or Codes to an Eye Tracker.
5. **Accessing Eye Tracker Data During Recording.**
6. **Accessing the Eye Tracker native time base.**
7. **Synchronizing the ioHub time base with the Eye Tracker time base.**

**Note:** Area's of Functionality in **bold** are considered core areas, and must be implemented for every eye tracker interface.

See the `Common Eye Tracker Interface API specification <http://www.isolver-solutions.com/iohubdocs/iohub/api_and_manual/device_details/eyetracker.html#the-iohub-common-eye-tracker-interface>`_ for API details.
