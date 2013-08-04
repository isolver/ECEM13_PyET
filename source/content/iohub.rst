.. _ioHub:

11.20 - 12.00 Introducing the ioHub
========================================

****************************
Overview
****************************

The ioHub is designed to solve several issues in experiment involving eyetracking and other high-throughput data collection.
    * Asynchronous from the stimulus presentation thread so that all hardware polling occurs at a high rate (not synchronised to the frame refresh)
    * Not only asynchronous but running on a separate core (assuming you have more than one). That means intensive data collection doesn't result in sloppy timing in stimulus presentation
    * covers a wide range of devices, including a :ref:`commonETinterface` for supported eyetrackers, so when you change eyetracker you don't have to start from scratch with your experiment!
    * can also save high-throughput data to disk using without impacting either stimulus presentation or data collection


* PsychoPy.ioHub is a Python package providing a cross-platform device
  event monitoring and storage framework. 
* ioHub is free to use and is GPL version 3 licensed.
* Support for the following operating Systems:
    * Windows XP SP3, 7, 8
    * Apple OS X 10.6+
    * Linux 2.6+
* Monitoring of events from computer _devices_ such as:
    * Keyboard
    * Mouse
    * Analog to Digital Converter
    * XInput compatible gamepads
    * Remote ioHub Server instances
    * **Eye Trackers, via the ioHub Common Eye Tracking Interface**


PsychoPy.ioHub MultiProcess Design
---------------------------------------

.. image:: ./iohub_diagram.png
    :width: 480px
    :align: center
    :height: 325px
    :alt: ioHub MultiProcess Design
    

Useful PsychoPy.ioHub Links
---------------------------------------

Installation
~~~~~~~~~~~~~~~~~~~

* ioHub is installed as part of PsychoPy

Documentation
~~~~~~~~~~~~~~~~~~~

*Docs are yet to be merged with the core PsychoPy documentation*

* `PsychoPy Docs <http://www.psychopy.org/documentation.html>`_
* `ioHub Docs <http://www.isolver-solutions.com/iohubdocs/index.html>`_

Support
~~~~~~~~~~~~~~~~~~~

`PsychoPy User Group <https://groups.google.com/forum/#!forum/psychopy-users>`_

Want to Contribute?
~~~~~~~~~~~~~~~~~~~~~~

`PsychoPy Developer Group <https://groups.google.com/forum/#!forum/psychopy-dev>`_

High Level ioHub API Review
--------------------------------

Starting the ioHub Server Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two ways to create a PsychoPy experiment which uses the iohub process. Both menthods ultimately give you access to an instance of the 
`ioHubConnection Class <http://www.isolver-solutions.com/iohubdocs/iohub/api_and_manual/iohub_process/getting_connected.html#the-iohubconnection-class>`_ 
for communication and control of the iohub server:

1. Use the `psychopy.iohub.launchHubServer() <http://www.isolver-solutions.com/iohubdocs/iohub/api_and_manual/iohub_process/launchHubServer.html#the-launchhubserver-function>`_ function.
2. Use the `psychopy.iohub.client.ioHubExperimentRuntime <http://www.isolver-solutions.com/iohubdocs/iohub/api_and_manual/iohub_process/ioHubExperimentRuntime.html#the-iohubexperimentruntime-class>`_, implementing the class's run() method for your experiment's starting python code.

Each approach has pros and cons:

- Using launchHubServer is quicker when creating an experiment that uses simple devices like the mouse and keyboard. 
- When using more advanced devices like an eye tracker, using the ioHubExperimentRuntime approach quickly becomes easier to manage, and makes the python code independent of device implementation being used. When using this approach, an understand of the simple file structure expected by the ioHubExperimentRuntime is needed.
 
Using launchHubServer() 
^^^^^^^^^^^^^^^^^^^^^^^^^

See the `launchHubServer() documentation <http://www.isolver-solutions.com/iohubdocs/iohub/api_and_manual/iohub_process/launchHubServer.html#the-launchhubserver-function>`_ for function details.

**Source File:** [workshop_materials_root]python_source/launchHubServer.py

.. literalinclude:: python_source/launchHubServer.py
    :language: python
    
Other examples of using launchHubServer (just change the top line of the python file which calls the launchHubServer function):

* Enabling event saving by defining an experiment code::
    
    # Start the ioHub, creating an ioDataStore file for experiment code 'silly_exp', and automatically
    # creating an automatic session code.
    #
    launchHubServer(experiment_code='silly_exp')
    
* Enabling event saving and specifying the session code::
 
    # Start the ioHub, creating an ioDataStore file for experiment code 'silly_exp', and 
    # creating a session with code name 's_001_m_42'.
    #
    launchHubServer(experiment_code='silly_exp',session_code='s_001_m_42')
    
* Enabling event saving and enabling the XInput Gampad Device using all default parameters::

    # Start the ioHub, creating an ioDataStore file for experiment code 'silly_exp', and 
    # creating a session with code name 's_001_m_42'. Also enable the ioHub XInput Gamepad support.
    #
    launchHubServer(experiment_code='silly_exp',
                    session_code='s_001_m_42',
                    xinput.Gamepad={})


.. _ioDataStore:

****************************************
ioDataStore - saving data
****************************************

For relatively small amounts of data you can fetch information from the ioHub while back to the stimulus presentation thread and use PsychoPy's standard data storage facilities. (You would still benefit from the fact that the events had been timestamped by ioHub on collection so it doesn't matter that you only retrieve the data from ioHub once per screen refresh). At other times you might be saving large streams of eye-movement data and you can use ioHub to save the data directly to disk using the HDF5 standardised data format.

What can be Stored
----------------------------------------------

* All events from all monitored devices during an experiment runtime.
* Experiment meta-data (experiment name, code, description, version,...) 
* Session meta-data (session code, any user defined session level variables)
* Experiment DV and IV information (generally saved on a trial by trial basis, but up to you)

Notable Features
----------------------------------------------
* You control what devices save which event types to the data store.
* Data is saved in the standard `HDF5 file format <http://www.hdfgroup.org>`_
* `Pytables <http://www.pytables.org>`_ is the Python package used to provide HDF5 read / write access.
* Each device event is saved in a table like structure; different event types use different event tables.
* Events are retrieved as numpy ndarrays, and can therefore easily and directly be used by packages such as numpy, scipy, and matplotlib.
* Data Files can be opened and viewed using free HDF5 Viewing tools such as `HDFView` <http://www.hdfgroup.org/hdf-java-html/hdfview/>`_ and `ViTables <http://vitables.org/download/index.html>`_, both of which are open-source, free, and cross-platform.

ioDataStore File Structure
----------------------------------------------

Hierchial File Structure and Meta-Data Tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ioDataStore HDF5 File Viewed using the HDFView Apllication

.. image:: ./ioDataStore_HDF5_File_Structure.png
    :align: center
    :alt: ioDataStore HDF5 File Viewed using the HDFView Apllication

Example Event Table: Monocular Eye Sample Event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example Event Table Viewed using the HDFView Application

.. image:: ./ioDataStore_MonoSample_Event.png
    :align: center
    :alt: Example Event Table Viewed using the HDFView Application   


Reading Saved Data - the ExperimentDataAccessUtility Class
-----------------------------------------------------------------

* Contains ioHub device event reading functionality
* Simple event access API
* Access events using the same type constants and event attributes as are used during on-line event access. 
* Supports on-disk querying of event tables based on event attribute values and meta-data info.; *fast* retieval of only the events which meet the query constraints.
* When combined with use of the ExperimentVariableProvider class, events access can be filtered by:
    * Dependent and Independent Conditions
    * Session and Trial IDs
    * Other Variables Calculated at Runtime, e.g. Trial Start and End Times, Stimulus Onset and Offset Times, etc
    * Any Event Attribute Value
    
Open ExperimentDataAccessUtility and explore ioDataStore file structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Source file:** python_source/datastore_examples/printing_datastore_file_structure.py

.. literalinclude:: python_source/iodatastore_examples/printing_datastore_file_structure.py
    :language: python
    

Accessing Experiment and Session Meta Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Source file:** python_source/datastore_examples/access_exp_metadata.py

.. literalinclude:: python_source/iodatastore_examples/access_exp_metadata.py
    :language: python
    
Read Any Saved Trial Condition Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Source file:** python_source/datastore_examples/read_condition_data.py

.. literalinclude:: python_source/iodatastore_examples/read_condition_data.py
    :language: python
    

List Device Event Types Where the Event Count > 0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Source file:** python_source/datastore_examples/access_events_with_data.py

.. literalinclude:: python_source/iodatastore_examples/access_events_with_data.py
    :language: python
    

Retrieving Specific Event Fields Grouped by Trial using a Trial Condition Query Selection
------------------------------------------------------------------------------------------

**Source file:** python_source/datastore_examples/access_single_event_table.py

.. literalinclude:: python_source/iodatastore_examples/access_single_event_table.py
    :language: python
    
.. _commonETinterface:

******************************************
The ioHub Common Eye Tracker Interface
****************************************** 

The API details for the ioHub EyeTracker device can be found `here <http://www.isolver-solutions.com/iohubdocs/iohub/api_and_manual/device_details/eyetracker.html#the-iohub-common-eye-tracker-interface>`_

The Common Eye Tracking Interface provides the same user level Python API for all supported eye tracking hardware, meaning:

* The same experiment script can be run with any supported eye tracker hardware.
* The eye event types supported by an eye tracker implementation are saved using the same format regardless of eye tracker hardware.

Currently Supported Eye Tracking Systems
------------------------------------------------------

* **LC Technologies** EyeGaze and EyeFollower models.
* **SensoMotoric Instruments** iViewX models.
* **SR Research** EyeLink models.
* **Tobii Technologies** Tobii models.

Visit the ioHub documentation for `Eye Tracking Hardware Implementations <http://www.isolver-solutions.com/iohubdocs/iohub/api_and_manual/device_details/eyetracker.html#eye-tracking-hardware-implementations>`_ for details on each implementation.

Areas of Functionality
---------------------------

1. **Initializing the Eye Tracker / Setting the Device State.**
2. **Performing Calibration / System Setup.**
3. **Starting and Stopping of Data Recording.**
4. Sending Messages or Codes to an Eye Tracker.
5. **Accessing Eye Tracker Data During Recording.**
6. **Accessing the Eye Tracker native time base.**
7. **Synchronizing the ioHub time base with the Eye Tracker time base.**

**Note:** Area's of Functionality in **bold** are considered core areas, and must be implemented for every eye tracker interface.

See the `Common Eye Tracker Interface API specification <http://www.isolver-solutions.com/iohubdocs/iohub/api_and_manual/device_details/eyetracker.html#the-iohub-common-eye-tracker-interface>`_ for API details.
