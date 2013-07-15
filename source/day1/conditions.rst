.. _conditionals:

Conditionals
---------------

We need to be able to control what parts of a script get run based on *conditions*. For example, if this trial requires a probe to be presented then run *this code* but if not run *that code*.

Boolean logic
~~~~~~~~~~~~~~~~~

Python, like most programming languages represents things as being ``True`` or ``False`` and these correspond to 1 or 0. 'Comparison operators' (``<``, ``>``, ``==``, ``<=``, `>=``, ``!=``) will return ``True`` or ``False``. See what these return (some are obvious, some not)::

    a = 4
    4<5
    a>5
    a==4
    4=4 #error?
    4.0==4 #compare a float with an int
    a>=3
    a=>3
    a!=3
    True==1
    False==0.0   
    
.. note::

    In nearly all programming languages ``=`` means 'make this equal to' whereas ``==`` means 'test whether this is equal to'. But even experienced programmers will occasionally use the wrong one.

Conveniently Python does the 'right thing' when comparing strings using the same syntax::

    a = "spam"
    b='blah'
    b > 'aaah'
    b<'aaah'
    b=='a'
    b[2]=='a'
    b.endswith('h')
    'aaa'.endswith(a) #work out why this is wrong!

As well as those standard comparison operators, Python defines the operation ``in`` for testing the contents of any object that Python considers `iterable`::

    'a' in 'blah'
    10 in range(5) #maybe find out what range(5) does?!
    subj = {'name':'jwp','age':21}
    'age' in subj.keys()
    5 in 10

As with any boolean logic system you can perform AND, OR, NOT operations on these things. These are usually typed with lower case (``and``, ``or``, ``not``)::

    a=='spam'
    1==2 or a==4
    1==1 and not a<4
    subj['name'].startswith('j') and subj['age']<18
    not True == False #get your head around this one!
    5 not in [1,2,4]
    
.. note::

    You can also use ``&``, ``|``, ``!`` for ``and``, ``or``, ``not`` but few people do. The text version is just more natural to read. You do sometimes see ``!=`` though.

As soon as Python can determine that the boolean statement is ``False`` the rest of the statement is not evaluated. That's very important for some statements where you first need to check if it's possible to run the next function, or where evaluating one part will take processing time and isn't always necessary::

    subj['weight']==83 and subj.has_key('weight')
    subj.has_key('weight') and subj['weight']==83 #reorder
    keys = ['y']
    keys[0]=='y' #check the first key press
    keys = []
    keys[0]=='y'
    len(keys)>1 and keys[0]

if... statements
~~~~~~~~~~~~~~~~~~~

If statements allow you to say, "if this statement evaluates to be ``True`` then run the next lines of code". To determine what count as the 'next lines' you have to indent the code. These examples are getting longer - you might want to switch to using the script editor panel if you've been using the shell so far::

    if True:
        print 'hello'
        print "toast"
    if  5==4:
        print 'no'

You can optionally define one or more ``elif`` statements and an ``else`` statement::

    if 5==4:
        print 'crazy'
    elif 3*5>10 and 'a'<'b':
        print 'possibly'
    else:
        print 'catch all'

If I've used an if...elif... I find it's often a good idea to include an ``else`` statement even if you don't think it will be called. It can make it easier to find bugs later on if something surprising happens::

    resp = ['left']
    if resp=='left':
        corr=True
    elif resp=='right':
        corr=False
    else:
        print "Response should be 'left' or 'right' not %s" %(resp)
        
.. note::

    The fact that Python will interpret either " or ' as a string makes it very easy if you want a string to contain one of those characters. e.g. "Won't hurt" is fine but 'Won't hurt' will cause an error (because the string effectively ends after the `n`). If you want to be really safe you can start or end a string with triple quotes and then the string can contain either type of quote inside.

Statements can nest too. Make sure you understand whether each of the following lines will be run and why::

    resps = [0,1,1,0]
    if len(resps)>0: #subj responded
        print "mean resp=", sum(resps)/float(len(resps))
        if resp[0]==0:
            print 'first resp correct'
        else:
            print 'first resp incorrect'
        print 'hello'
    print 'done'
