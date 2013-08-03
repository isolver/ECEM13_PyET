Useful Web Resources
========================================

This page contains links to web resources that are valuable sources of information
on Python, useful Python Tools, Python in Neuroscience or Psychology, and 
Eye Tracking with Python. It is not complete so love google!

Python
~~~~~~~

NB **stick to Python 2.7.x for now.** Python 3 is a substantial rewrite and many packages don't yet support it.

    * `Python 2.7.5 Documentation <http://docs.python.org/2/index.html>`_
    * `Python's built-in modules <http://docs.python.org/2/library/>`_

Learning Python
    * `The official Python tutorial <http://docs.python.org/2/tutorial/index.html>`_
    * http://www.Codecademy.com/
    * `Dive into Python <http://www.diveintopython.net/>`_

??????

Python Tools
~~~~~~~~~~~~~

    * `Numpy <http://www.numpy.org>`_ is for fast numeric computations on arrays
    * `SciPy <http://www.scipy.org>`_ extends Numpy with mathematical routines (like optimization, filtering etc.)
    * `Matplotlib <http://www.matplotlib.org>`_ is the main plotting library for Python, using similar syntax to Matlab
    * `IPython <http://www.ipython.org>`_ provides a nice interactive shell for using Python and also a 'notebook' interface for storing notes and documentation along with your analysis code.

Python and Psychology or Neuroscience
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`PsychoPy <www.psychopy.org>`_ :

    * `PsychoPy Docs <http://www.psychopy.org/documentation.html>`_
    * `ioHub Docs <http://www.isolver-solutions.com/iohubdocs/index.html>`_
    * `PsychoPy downloads (includes ioHub) <http://sourceforge.net/projects/psychpy/files/PsychoPy/>`_
    * `PsychoPy User Group <https://groups.google.com/forum/#!forum/psychopy-users>`_

Also:

    * `NiPy <http://nipy.org/>`_ for neuroimaging
    * The Frontiers journal special issue on `Python in Neuroscience tools <http://www.frontiersin.org/Neuroinformatics/researchtopics/python_in_neuroscience/8>`_ (many about modelling packages)
    
There's also `Open Sesame` (graphical interface for experiments with some eye-tracking support) and `PyEPL` (scripted, no eye-tracking) but neither is as flexible as PsychoPy!

Python and Eye Tracking
~~~~~~~~~~~~~~~~~~~~~~~~ 

Most eyetracker manufacturers provide Python interfaces if yours isn't supported by ioHub (yet) but you won't get the performance benefits of running on a separate CPU core, and if you buy a new eyetracker you'll have to change your code.