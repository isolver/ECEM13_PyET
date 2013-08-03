
.. _ioDataStore:

****************************************
ioDataStore - saving data
****************************************

For relatively small amounts of data you can fetch information from the ioHub while back to the stimulus presentation thread and use PsychoPy's standard data storage facilities. (You would still benefit from the fact that the events had been timestamped by ioHub on collection so it doesn't matter that you only retrieve the data from ioHub once per screen refresh). At other times you might be saving large streams of eye-movement data and you can use ioHub to save the data directly to disk using the HDF5 standardised data format.

What can be Stored
===================

* All events from all monitored devices during an experiment runtime.
* Experiment meta-data (experiment name, code, description, version,...) 
* Session meta-data (session code, any user defined session level variables)
* Experiment DV and IV information (generally saved on a trial by trial basis, but up to you)

Notable Features
=================
* You control what devices save which event types to the data store.
* Data is saved in the standard `HDF5 file format <http://www.hdfgroup.org>`_
* `Pytables <http://www.pytables.org>`_ is the Python package used to provide HDF5 read / write access.
* Each device event is saved in a table like structure; different event types use different event tables.
* Events are retrieved as numpy ndarrays, and can therefore easily and directly be used by packages such as numpy, scipy, and matplotlib.
* Data Files can be opened and viewed using free HDF5 Viewing tools such as `HDFView` <http://www.hdfgroup.org/hdf-java-html/hdfview/>`_ and `ViTables <http://vitables.org/download/index.html>`_, both of which are open-source, free, and cross-platform.

ioDataStore File Structure
==========================

Hierchial File Structure and Meta-Data Tables
----------------------------------------------

ioDataStore HDF5 File Viewed using the HDFView Apllication

.. image:: ./ioDataStore_HDF5_File_Structure.png
    :align: center
    :alt: ioDataStore HDF5 File Viewed using the HDFView Apllication

Example Event Table: Monocular Eye Sample Event
-------------------------------------------------

Example Event Table Viewed using the HDFView Application

.. image:: ./ioDataStore_MonoSample_Event.png
    :align: center
    :alt: Example Event Table Viewed using the HDFView Application   


Reading Saved Data - the ExperimentDataAccessUtility Class
===========================================================

* Contains ioHub device event reading functionality
* Simple event access API
* Access events using the same type constants and event attributes as are used during on-line event access. 
* Supports on-disk querying of event tables based on event attribute values and meta-data info.; *fast* retieval of only the events which meet the query constraints.
* When combined with use of the ExperimentVariableProvider class, events access can be filtered by:
    * Dependent and Independent Conditions
    * Session and Trial IDs
    * Other Variables Calculated at Runtime, e.g. Trial Start and End Times, Stimulus Onset and Offset Times, etc
    * Any Event Attribute Value
    
Creating an instance of ExperimentDataAccessUtility and printing an ioDataStore file structure
-----------------------------------------------------------------------------------------------

.. literalinclude:: python_source/iodatastore_examples/printing_datastore_file_structure.py
    :language: python
    

Accessing Experiment and Session Meta Data
------------------------------------------

.. literalinclude:: python_source/iodatastore_examples/access_exp_metadata.py
    :language: python
    
Read Any Saved Trial Condition Variables
---------------------------------------------

.. literalinclude:: python_source/iodatastore_examples/read_condition_data.py
    :language: python
    

List Device Event Types Where the Event Count > 0
--------------------------------------------------

.. literalinclude:: python_source/iodatastore_examples/access_events_with_data.py
    :language: python
    

Retrieving Events based on Query Selection and Grouped by Each Trial Condition Row
-----------------------------------------------------------------------------------

.. literalinclude:: python_source/iodatastore_examples/access_single_event_table.py
    :language: python
    
