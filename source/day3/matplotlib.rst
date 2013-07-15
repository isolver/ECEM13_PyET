.. _matplotlib:

Matplotlib (Matlab-like plotting library)
=========================================================

For complete documentation see:

    - functions summary: http://matplotlib.org/api/pyplot_summary.html
    - documentation index: http://matplotlib.org/users/index.html
    - example gallery: http://matplotlib.org/gallery.html

This is a plotting library designed capable of makign publication-quality plots (in fact I think every data figure I've published since around 2003 was created using matplotlib. For those who've programmed in Matlab the basics will be extremely familiar, by design. The more advanced aspects of plot manipulation, though, should show the strengths of the Python language again.

Importing the package
--------------------------

As with other libraries there are multiple ways to import the functions from matplotlib. Most of the really useful functions are under pyplot and would often be imported like this to keep the namespace clear and but to reduce the amount you need to type on each plotting command::

    import matplotlib.pyplot as plt
    
All the following examples assume you used that import method. Another option is ``import pylab as plt`` but that will fetch much more code, most of which you won't need.

Also, I would recommend you do all of this in the editor window, rather than the shell, because the shell can struggle providing all the help and smart completion of this very large library!

A simple plot
________________

You can create a simple plot like this::

    plt.plot([1,2,3],[10,11,12])
    plt.show()

Note that matplotlib doesn't show a figure unless you tell it to. The step of actually updating something on the screen is the slowest part of generating a plot so it doesn't try to do this for each command you call (or you would see the plot gradually appearing and changing and would take longer). If you are running from a shell you can call ``plt.ion()`` to turn on 'interactive mode' which will update the plot window on every command.

There are many formatting options for your line. For simple ones you can use the similar formatting methods as in Matlab (for the full set see the `pyplot.plot documentation <http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot>`_ ). Let's add some circles as well as a line and make it green. And alter the axes to make the ends of the lines more visible::

    plt.plot([1,2,3],[10,11,12], 'o-g')
    plt.xlim([0,4])
    plt.ylim([9,13])
    plt.show()
    
Often we'd have more numbers to plot than that. Let's generate a sine wave using numpy:


    