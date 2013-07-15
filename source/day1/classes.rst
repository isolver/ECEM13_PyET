.. _classes:

Classes
----------------------------------

You've possibly realised that everything in Python is an 'object'. Everything has data stored inside it and has methods that allow that data to be accessed or modified. For instance, a string is an object whose data are the values of the letters and whose methods are `upper()`, `lower()`, `split()`... It's very convenient that objects can have methods associated with themselves.

In PsychoPy you'll find objects like windows and stimuli with methods like `draw()`, `setPos()`, `setImage()`.

Classes aren't essential for most programming of experiments, but if you're comfortable with this object-oriented concept of programming, and comfortable with how to create functions already then classes provide you with a way to create your own custom objects, or to modify existing classes of object. (If you aren't yet comfortable with function definitions then leave this section until another day!)

A class is just a collection of functions and variables to store/retrieve/modify related data. Every class has an __init__ function to be run when an 'instance' of that class is created (`'a'` is an instance of a `string`). 

.. note::

    In Python functions that start with _ indicate internal functions/attributes that the user should probably ignore. Methods start/end with __ indicate functions that typically have special meanings to the language. For instance `__init__` is a function that is run when an object is created, `__str__` is a function that is run if an object is being converted to a string representation etc.

Let's define a simple class to represent a moving dot (we'll stick to one axis of motion for simplicity). To know where a dot is at any point in time we would need to know its start position and rate of motion. We'll give our class two methods, one to initialise it and another to report the position for a point in time. I usually give class names a capital letter so I remember what contents of my modules are classes and what are simple functions::

    class Dot:
        def __init__(self, startPos, speed):
            self.startPos = startPos
            self.speed = speed
        def getPos(self, t):
            """Get the location of the dot at a given time"""
            pos = self.startPos + t*self.speed
            return pos
    
    dot1 = Dot(2.0, 1.5) #this is really just a call to the Dot.__init__() function
    print dot1.getPos(3.0) #after 3 secs this dot should be at pos=6.5
    print dot1.speed #the value of self.speed can be accessed like this
    dot2 = Dot(2.0, -1.5) #each instance of the Dot is independent
    print dot2.getPos(3.0) 
    print dir(dot2) #what attributes does a Dot instance have?

Look carefully at that code. For every function within the class there's an extra input argument, which almost every programmer in the world will call `self`. So a class method with 3 arguments should be called with 2 (`self` is going to be given automatically). `self` allows you to set/retrieve variables that are associated with your object.

It might be useful to have the dot keep track of time. Then we could find its current pos without having to tell it a time. Or we could use a built-in clock unless the user requests a specific time::

    import time #the time module built in to Python
    
    class Dot:
        def __init__(self, startPos, speed):
            self.startPos = startPos
            self.speed = speed
            self.t0 = time.time() #the current time
        def getPos(self, t=None):
            """Get the location of the dot at the current time (or 
            any time, if given)"""
            if t == None:#if we were given a value for t use that, otherwise...
                t = time.time()-self.t0 #the time since t0
            pos = self.startPos + t*self.speed
            return pos
    
    dot1 = Dot(2.0, 1.5)
    time.sleep(1.5) #pause the script for 1.5 secs
    print dot1.getPos() #with no args get the current pos
    print dot1.getPos(5.0) #pos at some given point in future
    
Sub-classing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One big advantage of classes is that you can take an existing class and modify just one part of it. This code creates a subclass of string that has all the methods of normal strings but adds the additional method of returning itself as a `sentence()`. All other methods (including `__init__`) are untouched.::

    class NewStr(str):
        def sentence(self):
            #capitalise the first character
            self = self.replace(self[0], self[0].upper())
            #add a full stop
            if not self.endswith('.'):
                self = self+'.'
            return self

    x = NewStr('hello everyone')
    print x.sentence()
    print dir(x) #compare this with dir of a normal string
    
You can also replace existing methods in exactly the same way.