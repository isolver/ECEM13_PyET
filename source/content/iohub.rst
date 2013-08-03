.. _ioHub:

Introducing the ioHub
============================================

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