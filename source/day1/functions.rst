.. _functions:

Functions
----------------------------------

You've learned all the key elements to programming. Variable, conditionals and loops allow you to do pretty much anything your computer can do. But your code will quickly become hard to read if you simply write everything line after line and copy-and-paste pieces of code you want to re-use.

Functions allow you to a) reuse your code and b) make it easier to read by hiding away the 
guts of your code. For instance, if we have a pair of points in space, pt1 and pt2, with (X,Y) coordinates. We could find the distance between those using Pythagoras' theorem::

    pt1 = [8.0, 5.3]
    pt2 = [2.1, 9.2]
    sep1 = ((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**0.5
    
Now, the problem is that a) each time you see that in your code you'll have to spend a moment working out why it's there, and b) each time you write it you might make a mistake. Let's re-use the code for two more variables later in our script.::

    pt3 = [3.0, 8.1]
    pt4 = [2.5, 4.2]
    sep2 = ((pt3[0]-pt4[0])**2+(pt1[1]-pt4[1])**2)**0.5
    
Did you notice that when I changed the pt1,pt2 values to pt3,pt4 I missed one? Hard bugs to spot, right? OK, the solution is to write functions to do these simple jobs and hide away the hard-to-read pieces of code so that the rest is clear. In this case we want a function that takes two values and finds their separation. Type this function in (if you do this in the shell then press an extra `<return>` when you're done to dedent the definition of the function)::

    def separation(a, b):
        """Get the distance between two points"""
        sep = ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
        return sep
        
Having defined that function you can use it repeatedly::

    sep1 = separation(pt1, pt2)
    sep2 = separation(pt3, pt4)
    
Did you notice how help was provided for the function when you started the brackets? It was based on the `"""textHere"""` in your `separation` function. In Python these are called docstrings.

.. note::

    Almost any time you're planning to do something multiple times in a script you should think about replacing it with a function.

Function inputs
~~~~~~~~~~~~~~~~~~

On the whole you should assume that your function only knows about the things that it was given in the first line (you can also have `global` variables that can be seen from anywhere, but these are generally to be avoided). In the function above we required two variables and these were given the names `a` and `b` as we received them (it doesn't matter what names they had in the script).

Python allows you to specify the inputs to a function by order, or by name, or by a combination. e.g. we could have called the function like this::

    sep1 = separation(a=pt1, b=pt2)

You can also provide default values for inputs so that these don't have to be specified each time. For instance::

    def separation(a, b=[0,0]):
        """Get the distance between two points, or from the origin for a single point"""
        sep = ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
        return sep

    sep3 = separation(pt4) #b is set to [0,0]

Because we can use names for the arguments, we don't have to specify all those that precede the one we care about. e.g.::

    def separation(a, b=[0,0], verbose=False):
        """Get the distance between two points, or from the origin for a single point"""
        if verbose:
            print 'vertical sep=', a[1]-b[1]
            print 'horizontal sep=', a[0]-b[0]
        sep = ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
        return sep

    sep4 = separation(a=pt3, verbose=True) #use first and last args, middle is default
    sep5 = separation(pt4, pt2, verbose=True) #can combine ordered args and names
    sep6 = separation(a=pt4, pt2) #error? after a named arg, all others must be named
    
Function outputs
~~~~~~~~~~~~~~~~~~~

Some functions don't need to return anything (they just perform an operation like present a stimulus). The function above returns a single value. You can return multiple values too. Or you can choose whether to return one or more values in the function (this might not be wise though!)::

    def separation(a, b=[0,0], verbose=False):
        """Get the distance between two points, or from the origin for a single point"""
        vert = a[1]-b[1]
        horiz = a[0]-b[0]
        sep = (vert**2 + horiz**2)**0.5
        if verbose:
            print 'vertical sep=', vert
            print 'horizontal sep=', horiz
            return sep, horiz, vert
        else:
            return sep
    
    sep5, horiz5, vert5 = separation(pt4, pt2, verbose=True)
    #or store them as a tuple of 3 values:
    sepInfo5 = separation(pt4, pt2, verbose=True)
    print sepInfo5

.. note::
    
    If you don't specify any return values in your function but you then try to assign a variable to the output, then that variable will just become equal to None (i.e. it doesn't automatically raise an error).


Operations in-place
~~~~~~~~~~~~~~~~~~~~~

Remember that Python passes pointers to objects rather than copies of them, unless you manually make a copy. So again, if you do anything that changes the variable 'in-place' then it will be changed in the code that called your function.::

    def change(input):
        input[0] = 'a'
    
    myList = [1,2,3]    
    new = change(myList)
    print new #surprise? (see note above)
    print myList #should have changed
    
Modules
------------

You can put functions that you use repeatedly into a file so that you don't end up rewriting them at the top of your script. Save your `separation` function into a file called tools.py. Now, in the same directory, create a new file (e.g. 'importingExercise.py')::

    import tools
    print tools.separation([1,2],[6,4])

You could also do::
    
    from tools import separation
    print separation([1,2],[6,4]) #now we don't need tools.______
    from tools import * #Not recommended - see below
    
.. note::

    It's tempting to import everything from a module into the main `namespace` so that you don't have to keep typing module._____ . In fact it isn't a good idea because if you have many things defined in your modules you can find that you've overwritten one of your functions with a variable (or vice versa). Again it creates bugs that can be really hard to find.

And you can even rename things as you import them. `numpy` is a common library for numerical operations (as we've seen) and most people import that like this so that it only takes 2 characters to call the functions::

    import numpy as np
    print np.ones([2,3])

So that syntax of a dot is used in various ways in Python::

    import numpy, os
    os.getcwd() #the getcwd function in os module
    numpy.random.rand() #the rand function in the random submodule of numpy
    ("hello").upper() #the upper method of a string object

You can also have multiple modules within a folder. Then you may also need to add a file called __init__.py which can, optionally, run some code every time you import things from this folder. e.g. I might have a folder in my home directory like::

    HOME/
        python/
            jwpTools/
                __init__.py
                geometry.py
                filters.py
                sounds.py

If I add jwpTools to my path (see below) then I can do this in any Python script I run::

    from jwpTools import sounds, filters
    import jwpTools.geometry as geom

Adding a location to your path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a 'normal' python installation you could add HOME/python to your path by finding the site-packages directory of your installation and adding a text file there called `anythingYouLike.pth` and containing any paths that you want on separate lines (e.g. HOME/python in our case). If you use the PsychoPy Standalone installation then specify your folder in the preferences>general>paths (e.g. ["HOME/python"] ) and then you need to make the one extra step of importing the psychopy lib before importing your own libs::

    import psychopy #importing this causes the addition of paths in prefs
    import jwpTools.sounds
