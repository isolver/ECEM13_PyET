.. _psychopyOverview:

9:50 - 11:20am Introducing PsychoPy
=========================================

General issues:

    * PsychoPy handles a variety of colour spaces and stimulus units but these are a common source of confusion and PsychoPy doesn't check if you've done something sensible!
    * PsychoPy expects to control on each frame (each refresh of the screen) what gets drawn. So, especially when writing code, you need to think about controlling things at that level. 
    * PsychoPy expects a decent graphics card (seriously, avoid intel integrated graphics) and aims to synchronise to the screen. If it can't then stimulus timing cannot be controlled.
    * Even when it's a good graphics card you should know the limits of what your computer can manage and be careful, especially when loading images from disk.
    
Coder experiments
---------------------

PsychoPy has very many stimulus types:
    
    * *ImageStim* for bitmaps (pretty much any format). These can be used either as the image or as an alpha mask
    * *GratingStim* is similar to ImageStim but it will use the image as a cyclic texture and you can specify the spatial frequency of that texture
    * *RadialStim* for radial patterns (e.g. retinotopy patches)
    * *TextStim*, including choice of fonts and Unicode characters (but no real 'formatting')
    * *DotStim* for random dot kinematograms with a variety of signal/noise methods
    * *ElementArray* allows dynamic (hardware-optimised) presentation of similar-textured elements. e.g. create an array of gabors or a point-light walker
    * *Shapes* (basic or custom vertices, filled or unfilled)
    * *RatingScale* OK this isn't a stimulus exactly but it's pretty handy
    * *Sounds* (either generated or stored in wav files)

Many inputs options:

    * mouse, keyboard, joystick
    * eyetrackers
    * serial/parallel ports
    * ...anything that can communicate with your computer!
    * microphone, including speech recognition by google!!

Many data output formats:

    * 'long-wide' trial-by-trial data in a csv file
    * 'summarised' data (one row per condition) in csv or Excel
    * Python binary files for scripting analyses
    * log files to check timing and for when you forget to store the right stuff!
    
Now, the best place to work out what's possible is to look through some of the demo code

Builder Experiments
-----------------------

There's a 15min youtube video `building the Stroop <http://www.youtube.com/watch?v=VV6qhuQgsiI>` task from scratch, that will take you through all these steps again if you forget something.

The key concepts you'll need for the Builder is the idea that you have `Components` that are put together in `Routines` and these `Routines` are combined in a `Flow` diagram.

Let's just take a look in the Builder view to see how those work together...

Now the next issue is how to create repetition of the trials in such a way that the condition changes on each repeat. To do that we need to:
    
    * create a loop in the `Flow`
    * assign a conditions file to that loop containing variables that can be accessed by the `Components`. Column headings define the name of the variables and each condition is represented by one row.
    * retrieve the current value of the variable using the `$` symbol in our `Component`
    * remember to set the value to 'update every repeat' !!
    
