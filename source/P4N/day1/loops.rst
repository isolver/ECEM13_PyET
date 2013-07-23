.. _loops:

Loops 
--------------

Repeating things is what computers are good at and humans find boring! Repetition is controlled with loops, which come in two varieties. :ref:`forLoops` are when you want something to repeat a known number of times, whereas :ref:`whileLoops` will run for an unspecified duration until some condition is met.

.. _forLoops:

for... loops
~~~~~~~~~~~~~~~

If you've come from matlab programming you probably expect a for...loop to operate over some numbers, which you'll use to index some other object (a string or an array). In Python anything that knows how to 'iterate' can be used as the basis for a loop and will return its next value each pass through the loop.

For instance, strings and lists both know how to 'iterate'::

    for thisLetter in 'hello':
        print thisLetter
        print 'printed'
    print 'loop done'
    
    for thisWord in ("Hello World, I greet you").split():
        print thisWord
    
    for thisInt in [1,2,3]:
        print thisInt, thisInt*3
    
Let's use a loop to create a list of dictionaries::

    myList=[]
    for thisInt in range(5):
        thisEntry = {}
        thisEntry['val']=thisInt
        thisEntry['X3']=thisInt*3
        myList.append(thisEntry)
    print 'myList is now', myList
    
    print 'printing one entry per line:'
    for thisEntry in myList:
        print thisEntry
        
**Jon's style tip:** I quite often use 'this' as a way to remind myself that a variable was being used in a loop. It can lead to confusing bugs if you refer to a variable after a loop has ended that was designed for use in the loop. After the loop ends the variable still exists, but has the last value it was left with in the loop::

    word = 'blah' #maybe this was defined earlier in the script
    
    wordSet =[]
    for word in ('Hello people').split():
            wordSet.append( {'word':word, 'upper':word.upper()} )
            
    print word #I was still intending to print 'blah'
        
If the value that is returned during the iteration can be 'unpacked' further then it can be assigned to multiple values in the loop. For example::
    
    a_b = [2,8]
    a, b = a_b #'unpack' the variable a_b to a pair of variables
    a, b, c, = a_b #error?
    a, b = [1,2,3] #error?
    
If you use a dictionary in a loop it will return each of the keys::

    man = {'name':'Jon', 'style':'geek', 'age':21}
    for thisKey in man:
        print "This man's %s is %s" %(thisKey, man[thisKey])

Dictionaries also have an `items` method, which returns a list of key/value pairs. We could iterate over the list of pairs, which means we could do this::

    for thisKey, thisVal in man.items():
        print "This man's %s is %s" %(thisKey, thisVal)

Nesting loops
~~~~~~~~~~~~~~~~

You can nest one loop inside another (as deeply as you like). The inner loop will perform a full cycle on each pass through the outer loop::

    for thisNum in range(5):
        for thisChar in 'abc':
            print thisNum, thisChar

Switch the order of the two loops and try it again.

Remember indentation is key in deciding which of the loops a code line belongs to::

    for thisNum in range(5):
        print '------------starting run %i' %(thisNum)
        for thisChar in 'abc':
            print thisNum, thisChar
            print 'x'
        print '------------finished run %i' %(thisNum)

Enumerate
~~~~~~~~~~~~~

Often you'll want to know not only the current value in a list, but also its location. For instance, if we run some trials like this (NB. I'd definitely recommend doing this in the code editor rather than the Shell panel)::

    from numpy import random #we need a new lib for this demo
    oris = [0,45,90,180]
    resps = []
    trials=[]
    RTs = []
    for thisRep in range(5):#repeat 5 times
        random.shuffle(oris) #NB this shuffles the list 'in-place'
        for thisOri in oris:

            #imagine we presented a stimulus

            #and simulate getting a response
            resp = round(random.rand()) #we'll create a random 'response'
            resps.append(resp) #the response from this trial
            RT = random.rand() #some number between 0-1
            RTs.append(RT)
            trials.append(thisOri) #also store what this trial was
    
    #... later we want to print out what happened
    for thisResp in resps:
        print thisResp

For the last part we could avoid looping through the `values` of ``resps`` and instead loop through a set of `indices` to fetch the values::

    for ii in range(len(resps)):
        thisResp = resps[ii]
        thisTrial = trials[ii]
        thisRT = RTs[ii]
        print ii, thisResp, thisTrial
        
The need to know the current value AND its index in the list is so common that Python has a special function for it built-in called ``enumerate``::

    for ii, thisResp in enumerate(resps):
        thisTrial = trials[ii]
        thisRT = RTs[ii]
        print ii, thisResp, trials[ii]

.. _whileLoops:

while... loops
~~~~~~~~~~~~~~~~~

If you want your loop to end based on some condition, rather than based on a certain number or iterations, then you could use a while...loop. For instance, an experiment might be based something on time rather than on repeats::

    import time #time module is built into Python
    t0=time.time() #time in secs
    nReps = 0
    while (time.time()-t0) < 0.5: #continue this loop for 0.5s
        nReps = nReps+1 # (or you could use the shorthand n+=1. Try that in the shell)
    print 'we did %i loops in 0.5s' %(nReps)

Or you might want to end the loop only when a valid response has occurred.::

    from numpy import random
    validKeys = 'az'
    availableKeys = 'azqwertyuiop'
    resp=None #None is a special value in Python for, well, none!
    while resp==None:
        ii = random.randint(0,len(availableKeys))
        keyPress = availableKeys[ii]
        if keyPress in validKeys:
            resp=keyPress
            print 'At last'
        else:
            print "'%s' was not a valid key" %(keyPress)
    print "subject responded with '%s'" %(resp)

	
Other than that, while...loops are really similar to for...loops (personally I use them less).

`break` and `continue`
~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you need to end a loop, or this repeat of a loop, prematurely. ``break`` allows you to end a loop completely and move to the next code after it. ``continue`` means 'continue to the next iteration of the loop without finishing this one'. They both only operate on the innermost level if your loops are nested.

Let's combine some of the earlier code. We'll run trials as in the :ref:`enumerate` demo and collect keypresses a bit like the :ref:`whileLoops` section. But instead of waiting for a valid response, we'll just ignore trials where subjects responded got the wrong keys. And if they hit 'q' we'll abort the experiment::

    from numpy import random #we need a new lib for this demo
    validKeys = 'az'
    availableKeys = 'azqwertyuiop'
    oris = [0,45,90,180]
    resps = []
    trials=[]
    RTs = []
    for thisRep in range(5):#repeat 5 times
        random.shuffle(oris) #NB this shuffles the list 'in-place'
        for thisOri in oris:

            #imagine we presented a stimulus

            #now simulate getting a response
            ii = random.randint(0,len(availableKeys))
            keyPress = availableKeys[ii]
            RT = random.rand() #some number between 0-1
            #perform analysis
            if keyPress == 'q':
                print 'experiment aborted'
                break
            elif keyPress not in validKeys:
                print 'invalid response'
                continue # to next trial (don't analyse further)
            #we got a useful trial so store info
            resps.append(keyPress) #the response from this trial
            RTs.append(RT)
            trials.append(thisOri) #also store what this trial was
    

	