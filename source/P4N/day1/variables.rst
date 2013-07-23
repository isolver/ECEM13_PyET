.. _variables:

Variables and common types
----------------------------------

Assigning variables
~~~~~~~~~~~~~~~~~~~~~~~~

You've already seen variables being assigned using =. You can also assign multiple things at once. Type these in and then check to see what each variable looks like afterwards::

	a = b = 2 
	a, b = 2,3 #also, see what happens if the number of vals doesn't match
	myString = "Hello World"
	firstWord, secondWord = myString.split() #also try splitting by 'o'
	tupleOfTwoWords = myString.split()

Types of variable
~~~~~~~~~~~~~~~~~~~~~~~~

In Python almost everything is an `object`. There are a number of built-in objects that are very widely used:
    
    * integers and floats
    * booleans
    * strings (and unicodes)
    * tuples and lists
    * dicts

You can find out what an object is using the ``type()`` function::

    print type('a')
    print type([1,2,3])
    print type(5)
    print type(True)
    
Finding out the type can be essential if things look the same when printed but aren't the same::

    a = 5
    b = '5'
    print a, b
    print a==b
    print type(a), type(b)
    
But there are a huge number of additional objects and you can make your own too.

Integers and floats
~~~~~~~~~~~~~~~~~~~~~~~~

Integers don't store anything after the decimal place. Beware that in Python up until version 3 (you're probably using version 2.6 or 2.7. You could find out by importing sys and finding that version attribute again) when you divided a pair of integers it gave you back an integer:: 

    print 1/3 #surprise!
    print 1.0/3
    print 1/3.0

From version 3 upwards it will give a float if they don't divide equally. You can get the new style by running the rather strange command::

    from __future__ import division
    
This is a good thing to do at the top of most scripts to avoid confusion, or get used to typing values as floats.

Strings
~~~~~~~~~~~~~~~~~~~~~~~~

Python has fantastic string handling options. Try these methods that are attached to strings::

    a = "hello world"
    a.title()
    a.split()
    a.endswith('world')
    len(a)
    
You can also combine strings in nice, simple ways::

    x = 'abc'
    y = 'xyz'
    z = x*2+y
    z
    x+x.upper()

.. _slicing:

Slicing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often you need to fetch a subset of an object, like a string or a list.

.. warning::

    If you're used to Matlab then be warned: in Python the first element of an array or a list is zero, not one. This will catch you out sooner or later!!

    a = 'nottingham'
    a[0]
    a[2:4]
    a[2:]
    a[:]
    a[-1]
    a[2:-2].upper()
    
You can convert between these different types of objects where they make sense::

    int(1.5)
    int('1')
    str(1.5)
    float(1)

but not where they don't::
    
    float('f1')
    int([1,2])
    
.. _formattedStrings:

Formatted strings
~~~~~~~~~~~~~~~~~~~~~~

Sometimes you need to combine numbers and strings. Imagine I wanted to make a filename to save my data. Maybe in my script I had a variable to store my subject name and another to store a stimulus attribute which was 10, 50, 100, 200 on different runs. I might try and save the data filename like this::
    
    subj = 'jwp'
    cond = 50
    filename = subj+cond+".txt"

You get an error because cond is a number and your trying to add it to a pari of strings (subj and ".txt") and Python doesn't know what way you want them combined. You could convert cond into a string and have no error::

    filename = subj+str(cond)+".txt"

but that doesn't provide much control of the formatting of the number. If you wanted a certain number of decimal places it couldn't set that. In the following the `%i`, `%f` and `%s` indicates that Python go and find a variable in the following list and insert it with the specified representation. Any other text just looks like itself(!). If you've ever used formatted string operations in C or Matlab these will make sense pretty quickly, but otherwise they could take some time::

    "%i" %(23)
    "an int:%i" %(5)
    "a float:%f" %(5)
    "before%i_after" %(200)
    "%s.txt" %(subj) #assuming subj was still defined
    filename = "%s%i.txt" %(subj, cond)

Now the real advantage of this format is that you can control the number of decimal places, and padding with zeros. Try these out::

    "%04i" %(9)
    "%4i" %(9)
    "%.2f" %(9)
    "%s%03i.txt" %(subj, cond)
    "That took %f seconds" %(32.5432143)
    "That took %.2f seconds" %(32.5243553)

These formatted strings may seem cumbersome to start with but they're very powerful when you get the hang of them (and they're roughly the same in most languages). There are many more variants on these operations but those are the main ones that you'll need.

For more see:

    http://docs.python.org/2/library/stdtypes.html#string-formatting-operations

Containers
-----------------

Very often you need variables that store more than one value and keep them organised in some way. The two most common are lists and dictionaries.

Lists
~~~~~~~~~~~~~~~~~~~~~~~~

For storing things that have a defined order::

	a = [10,20,30]
	b = ['a',1,1.0]
	b.append('blah')
	a.append(3.0)
	
Slicing works just the same as with strings::

	a[0] #remember, python starts at zero
	a[4] #so this won't work
	a[-1] #this will
	b[-1]
	b[-1][-1]

Mathematical operators::
	
	a+a #this might be a surprise
	a+b
	b*3
	
Other methods::

	print dir([]) #go and explore some of the other methods of lists
	print a.append(b)
	print a.extend(b)
	print a.index(30)

Python also defines a type of variable called a `tuple`, which has slightly different methods, but similar and I find it less useful::

    x = (1,2) #note the different parentheses
    print type(x)
    print dir(x)
    
For those who have come from Matlab backgrounds, these lists might look like Matlab matrices, but they aren't. These aren't designed for mathematical operations. There is a similar object which *is* very much like Matlab matrices, which we'll explore when we look at :ref:`analysingData`.

Dictionaries (dicts)
~~~~~~~~~~~~~~~~~~~~~~~~

At times you want to keep things with something that identifies what each element is. That's where you'll use a dict. These can be created in various ways::

	stim1 = {'word':'red','ori':90,'duration':0.5}
	#or just create it and add the entries afterwards:
	stim2 = {}
	stim2['word'] = 'blue'
	stim2['ori'] = 90
	stim2['duration'] = 0.3
	print stim1['word']

Then you can access the contents in a similar way::

    print stim1['ori']
    print stim2['fail'] #error?

These are referred to as key-value pairs. Explore what some of the different dict methods do::

	dir(stim1)
	stim1.keys()
	stim1.has_key('blue')
	stim1.has_key('word')

Nesting objects within each other
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often containers are nested within each other. You might well have a list of dicts, or a dict containing lists etc.::

    #a list of dicts
    stimuli = [stim1, stim2, stim3]
    stimuli[0]['word'] #this is stim1 because we start at zero!!
    thisStimulus = stimuli[2]
    thisStimulus == stim3

    #a list of lists
    coordinates=[[0,0], [2,3], [8,0]]
    responses = [ [1, 1, 0, 0], #if your line ends in a comma you can go to the next line
        [1,1,1,0],
        [0,1,1,1]]
    print responses
    print responses[2][3] #the 4th entry of 3rd list (STARTS AT ZERO)
    
    #or we could have done this
    responses = []
    cond1 = [1,1,0,0]
    responses.append(cond1) #etc.

You can nest objects as deeply as you like. The limit is your own brain being able to keep track of what you're doing!

Referents not copies
~~~~~~~~~~~~~~~~~~~~~~~~~~

In many programming languages when you assign one variable to another you get a `copy` of the original. That isn't true in Python; in Python, both variables `refer` to the same item. That means that if you *change* the item in-place then it will be changed for both variables::

    print stim1
    stim3=stim1
    stim3['word']='banana'
    print stim1

The same thing is an issue with lists::

    a = [1, 0, 1, 1]
    b=a
    b.append(25)
    print a

Or combinations of lists and dicts ::
    
    stimuli[0]['colour']='giraffe'
    print stim1
    
This concept that you have multiple variables refering to the same actual objects is very useful for conserving memory and to shorten some code. e.g. if you had a dictionary of 'subjects' where each had a dictionary of 'conditions' and each of those had a list of multiple 'responses' (NB this isn't going to work for you right now)::

    resps = allData['jwp']['preAdaptation'] #retrieve the response list for this condition
    resps.append('correct') # added to the original but we don't have to write it all out
    
but occasionally you do want a copy though, because you *don't* want your changes reflected back in the original. For that we need to do a little more work::

    import copy 
    stim4 = copy.copy(stim1) #the copy function in the copy module
    stim4['word']='rat'
    print stim1, stim4
    