.. _gettingStarted:

Getting started
-----------------------------

There are many different interfaces/editors for using Python. For simplicity, we're going to stick with the interface that PsychoPy provides for you, but if you have favourite editor feel free to use that instead. 

Views
~~~~~~~~~~~~

Open PsychoPy and go to the Coder view (you can close Builder for now). The Coder has a script editing panel at the top, an output panel beneath where outputs from your script will appear, and a shell panel next to the output panel

Shell
~~~~~~~~~

This is a great place just to try out a quick command and see what happens. You can check a little Python syntax and see the results of commands. 

Let's type some commands into the shell panel and see what happens::

    >>> a = 3
    >>> b = a+2
    >>> b
    5
    >>> b == 5
    True

Note that in the shell if the command `returns` a value and you didn't provide anything to receive/store that value then it gets printed to the screen instead (this is not the case for scripts run from the editor). 

Python functions are organised into `modules` and `packages` which we need to import to use::

    >>> import os

You can find out what's in a module using the function ``dir()``::

    >>> dir(os)

In this shell window you can also find out what it contains by starting to type a command. Type these lines gradually, taking note of what happens when you type the '.' and the '('::

    >>> os.getcwd()
    '/Applications/PsychoPy2.app/Contents/Resources'
    >>> os.chdir('..')

To repeat a previous command hit ``Alt-P`` on your keyboard. Repeat your ``os.getcwd()`` function to see where your current working directory is now.

Some of the items you see as a part of ``os`` are functions, whereas others are attributes. For instance, ``getcwd`` is a function. Consider the different outputs you get in the following two lines::
	
    >>> os.getcwd
    >>> os.getcwd()
    
The first returns the function itself (and prints it), whereas the second *runs* the function because of the parentheses, and prints what the function returns.

Editing Scripts
~~~~~~~~~~~~~~~~~~~~~

Although the shell is a handy place to check a quick command, it's often desirable to be able to repeat a set of commands from scratch. Type this into the editor window and save the script somewhere (e.g. firstScript.py)::

    a = "hello"
    print a
    b = ' world'
    a+b

.. note::

    Strings in Python can be defined using either ``'`` or ``"``. 

Switch the bottom panel of the Coder view to show the `Output` from the script. Hit the `Run` button (or press `Ctrl-R`). You might have expected to see ``hello world`` but it didn't appear. That's because in running scripts nothing is printed to the output unless you explicitly request it. Change the last line to ``print a+b``.

Indentation
~~~~~~~~~~~~~~~~~~

One of the unusual things in Python is that indentation (whitespace) is actually important. Try to use a genuine programmer's text editor and set it to insert spaces in place of tabs (it's hard to spot errors when you have a mixture of tabs and spaces). Many editors, will try to help you get indentation right.

Type the following into the editor after your other text::

    for thisLetter in a:
        print thisLetter
        print thisLetter.upper()
        print 'done'
    
.. note::

    ``upper()`` is a ``method`` that all strings have. Let's find out what else they have by using that ``dir()`` function from earlier. Add ``print dir(a)`` to the last line
    
Now, that probably didn't do what you expected. In Python the code that is included as part of the for-loop is indicated by the level of indentation, so ``print('done')`` was repeated for each repeat. If you added ``print dir(a)`` at the same level that would also have been repeated. Select the last few lines of code and press `Ctrl-[` to get this::

    for thisLetter in a:
        print thisLetter
    print thisLetter.upper()
    print 'done'
    print dir(a)
    
Now the code will print each of the letters in their lower case. Then the loop ends. ``thisLetter`` still exists but it isn't changing any more. It gets printed just once in upper case, followed by the other commands.

``print`` can print multiple objects at once (if you insert commas), and you can suppress the line endings with a final comma. Try this::

    for thisLetter in a:
        print thisLetter, thisLetter.upper(), 
    print 'end of the loop'
    print 'done'

Comments
~~~~~~~~~~~~~

In Python comments are indicated by the ``#`` symbol. 

.. note::

    Annoyingly a mac keyboard doesn't show you where the ``#`` is, but you can get it using ``Alt-3`` if you're running under OS X. If you're using a British Mac keyboard under Windows you need ``Ctrl+Alt+3``. Sigh!

You can start/end a multi-line comment with three double-quotes::
    
    """This is a potentially long piece of text that
    will be ignored. If it occurs at the start of a 
    function it becomes the help for that function
    """
    
    #I'm going to assign a variable
    a = 5 #it's a pretty boring variable!
    
In the PsychoPy Coder window you can comment out lines with ``Ctrl-'`` and undo that with ``Shift-Ctrl-'`` If you forget it's listed in the ``Edit`` menu

Exercises
~~~~~~~~~~~~~~

#. Create a new variable called ``myPhrase`` and give it the value ``"A whole bunch of words"``. Using the dir() command, work out a way to split that into a set of separate words.

#. In the Shell panel import the module called ``sys`` and find a command in it that will tell you the version of Python that you're running. Find another to tell you about the platform you're running on.

