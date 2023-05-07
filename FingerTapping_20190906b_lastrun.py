#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Tue Dec 10 09:39:22 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'FingerTapping2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/vincent/Data/Documents/Utah/Kladblok/20181018_FingerTappingTask/20190528_Duff_Version/Test/FingerTapping_20190906b_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "i01"
i01Clock = core.Clock()
i01_t = visual.TextStim(win=win, name='i01_t',
    text='In this test we will be measuring how fast you can press with \n\nyour LEFT index finger, your RIGHT index finger, \n\nBOTH index fingers simultaneously, and\n\nBOTH index fingers alternating.\n\n\n<< press any GREEN KEY to continue >>',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "i02"
i02Clock = core.Clock()
i02_t = visual.TextStim(win=win, name='i02_t',
    text='Next up are four videos\n\ndemonstrating LEFT index finger pressing,\n\nRIGHT index finger pressing,\n\nDUAL index finger pressing, \n\nand ALTERNATING left and right finger pressing.\n\n\n<< press any GREEN KEY to continue >>',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "i03"
i03Clock = core.Clock()
i03_tL = visual.TextStim(win=win, name='i03_tL',
    text='LEFT INDEX FINGER PRESSING:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
i03_vL = visual.MovieStim3(
    win=win, name='i03_vL',
    noAudio = True,
    filename='./Videos/LeftTapping.mpg',
    ori=0, pos=(0, 0), opacity=1,
    size=(960, 540),
    depth=-1.0,
    )
i03_tR = visual.TextStim(win=win, name='i03_tR',
    text='RIGHT INDEX FINGER PRESSING:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
i03_vR = visual.MovieStim3(
    win=win, name='i03_vR',
    noAudio = True,
    filename='./Videos/RightTapping.mpg',
    ori=0, pos=(0, 0), opacity=1,
    size=(960, 540),
    depth=-3.0,
    )
i03_tD = visual.TextStim(win=win, name='i03_tD',
    text='DUAL INDEX FINGER PRESSING:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
i03_vD = visual.MovieStim3(
    win=win, name='i03_vD',
    noAudio = True,
    filename='./Videos/DualTapping.mpg',
    ori=0, pos=(0, 0), opacity=1,
    size=(960, 540),
    depth=-5.0,
    )
i03_tA = visual.TextStim(win=win, name='i03_tA',
    text='ALTERNATING (LEFT - RIGHT) FINGER PRESSING:',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
i03_vA = visual.MovieStim3(
    win=win, name='i03_vA',
    noAudio = False,
    filename='./Videos/Alternating.mpg',
    ori=0, pos=(0, 0), opacity=1,
    size=(960, 540),
    depth=-7.0,
    )
i03_t = visual.TextStim(win=win, name='i03_t',
    text='<< press any GREEN KEY to continue >>\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "InstrL"
InstrLClock = core.Clock()
iLt = visual.TextStim(win=win, name='iLt',
    text='When the screen shows: "Get ready!"\n\nPlace your LEFT index finger on the LEFT GREEN KEY\n\n\nWhen the screen shows: "Start pressing!"\n\npress the LEFT GREEN KEY AS FAST AS POSSIBLE \n\nwith your LEFT INDEX FINGER.\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
iLc = visual.TextStim(win=win, name='iLc',
    text='\n\n\n\n\n\n\n \n\n\n\n\n<< press the LEFT GREEN KEY to continue >>',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=40, ori=0, 
    color='Chartreuse', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Ready"
ReadyClock = core.Clock()
rT1 = visual.TextStim(win=win, name='rT1',
    text='Get ready!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rT2 = visual.TextStim(win=win, name='rT2',
    text='Start pressing!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Left"
LeftClock = core.Clock()
Lt = visual.TextStim(win=win, name='Lt',
    text='Press \n\nAS FAST POSSIBLE \n\nwith your \n\nLEFT INDEX FINGER\n',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Done"
DoneClock = core.Clock()
Complete = visual.TextStim(win=win, name='Complete',
    text='Done!',
    font='Arial',
    pos=(0, 0), height=0.20, wrapWidth=40, ori=0, 
    color='Chartreuse', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "InstrR"
InstrRClock = core.Clock()
iRt = visual.TextStim(win=win, name='iRt',
    text='When the screen shows: "Get ready!"\n\nPlace your RIGHT index finger on the RIGHT GREEN KEY\n\n\nWhen the screen shows: "Start pressing!"\n\npress the RIGHT GREEN KEY AS FAST AS POSSIBLE \n\nwith your RIGHT INDEX FINGER.\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
iRc = visual.TextStim(win=win, name='iRc',
    text='\n\n\n\n\n\n\n \n\n\n\n\n<< press the RIGHT GREEN KEY to continue >>',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=40, ori=0, 
    color='Chartreuse', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Ready"
ReadyClock = core.Clock()
rT1 = visual.TextStim(win=win, name='rT1',
    text='Get ready!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rT2 = visual.TextStim(win=win, name='rT2',
    text='Start pressing!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Right"
RightClock = core.Clock()
Rt = visual.TextStim(win=win, name='Rt',
    text='Press \n\nAS FAST POSSIBLE \n\nwith your \n\nRIGHT INDEX FINGER',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Done"
DoneClock = core.Clock()
Complete = visual.TextStim(win=win, name='Complete',
    text='Done!',
    font='Arial',
    pos=(0, 0), height=0.20, wrapWidth=40, ori=0, 
    color='Chartreuse', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "InstrB"
InstrBClock = core.Clock()
iBt = visual.TextStim(win=win, name='iBt',
    text='When the screen shows: "Get ready!"\n\nPlace your LEFT finger on the LEFT GREEN KEY.\nPlace your RIGHT finger on the RIGHT GREEN KEY.\n\n\nWhen the screen shows: "Start pressing!"\n\nPress AS FAST AS POSSIBLE\nwith BOTH LEFT AND RIGHT INDEX FINGERS SIMULTANEOUSLY.\n\n\nPress both fingers at the same time (synchronously).\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
iBc = visual.TextStim(win=win, name='iBc',
    text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<< press any GREEN KEY to continue >>',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=40, ori=0, 
    color='Chartreuse', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Ready"
ReadyClock = core.Clock()
rT1 = visual.TextStim(win=win, name='rT1',
    text='Get ready!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rT2 = visual.TextStim(win=win, name='rT2',
    text='Start pressing!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Both"
BothClock = core.Clock()
Bt = visual.TextStim(win=win, name='Bt',
    text='Press AS FAST POSSIBLE \n\nand \n\nSIMULTANEOUSLY \n\nwith \n\nBOTH INDEX FINGERS',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Done"
DoneClock = core.Clock()
Complete = visual.TextStim(win=win, name='Complete',
    text='Done!',
    font='Arial',
    pos=(0, 0), height=0.20, wrapWidth=40, ori=0, 
    color='Chartreuse', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instrA"
instrAClock = core.Clock()
iAt = visual.TextStim(win=win, name='iAt',
    text='When the screen shows: "Get ready!"\n\nPlace your LEFT finger on the LEFT GREEN KEY.\nPlace your RIGHT finger on the RIGHT GREEN KEY.\n\nWhen the screen shows: "Start pressing!" \n\npress AS FAST AS POSSIBLE ALTERNATING \nyour LEFT AND RIGHT INDEX FINGERS.\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=40, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
iAc = visual.TextStim(win=win, name='iAc',
    text='\n\n\n\n\n\n\n\n\n\n\n<< press any GREEN KEY to continue >>',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=40, ori=0, 
    color='Chartreuse', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Ready"
ReadyClock = core.Clock()
rT1 = visual.TextStim(win=win, name='rT1',
    text='Get ready!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rT2 = visual.TextStim(win=win, name='rT2',
    text='Start pressing!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Alternating"
AlternatingClock = core.Clock()
At = visual.TextStim(win=win, name='At',
    text='Press AS FAST POSSIBLE ALTERNATING \n\nyour LEFT and RIGHT index fingers',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Done"
DoneClock = core.Clock()
Complete = visual.TextStim(win=win, name='Complete',
    text='Done!',
    font='Arial',
    pos=(0, 0), height=0.20, wrapWidth=40, ori=0, 
    color='Chartreuse', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "i01"-------
t = 0
i01Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
i01_k = event.BuilderKeyResponse()
# keep track of which components have finished
i01Components = [i01_t, i01_k]
for thisComponent in i01Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "i01"-------
while continueRoutine:
    # get current time
    t = i01Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *i01_t* updates
    if t >= 0.0 and i01_t.status == NOT_STARTED:
        # keep track of start time/frame for later
        i01_t.tStart = t
        i01_t.frameNStart = frameN  # exact frame index
        i01_t.setAutoDraw(True)
    
    # *i01_k* updates
    if t >= 1 and i01_k.status == NOT_STARTED:
        # keep track of start time/frame for later
        i01_k.tStart = t
        i01_k.frameNStart = frameN  # exact frame index
        i01_k.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if i01_k.status == STARTED:
        theseKeys = event.getKeys(keyList=['lshift', 'rshift'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in i01Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "i01"-------
for thisComponent in i01Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "i01" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "i02"-------
t = 0
i02Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
i02_k = event.BuilderKeyResponse()
# keep track of which components have finished
i02Components = [i02_t, i02_k]
for thisComponent in i02Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "i02"-------
while continueRoutine:
    # get current time
    t = i02Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *i02_t* updates
    if t >= 0.0 and i02_t.status == NOT_STARTED:
        # keep track of start time/frame for later
        i02_t.tStart = t
        i02_t.frameNStart = frameN  # exact frame index
        i02_t.setAutoDraw(True)
    
    # *i02_k* updates
    if t >= 1 and i02_k.status == NOT_STARTED:
        # keep track of start time/frame for later
        i02_k.tStart = t
        i02_k.frameNStart = frameN  # exact frame index
        i02_k.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if i02_k.status == STARTED:
        theseKeys = event.getKeys(keyList=['lshift', 'rshift'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in i02Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "i02"-------
for thisComponent in i02Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "i02" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "i03"-------
t = 0
i03Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
i03_k = event.BuilderKeyResponse()
# keep track of which components have finished
i03Components = [i03_tL, i03_vL, i03_tR, i03_vR, i03_tD, i03_vD, i03_tA, i03_vA, i03_t, i03_k]
for thisComponent in i03Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "i03"-------
while continueRoutine:
    # get current time
    t = i03Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *i03_tL* updates
    if t >= 0.0 and i03_tL.status == NOT_STARTED:
        # keep track of start time/frame for later
        i03_tL.tStart = t
        i03_tL.frameNStart = frameN  # exact frame index
        i03_tL.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if i03_tL.status == STARTED and t >= frameRemains:
        i03_tL.setAutoDraw(False)
    
    # *i03_vL* updates
    if t >= 3 and i03_vL.status == NOT_STARTED:
        # keep track of start time/frame for later
        i03_vL.tStart = t
        i03_vL.frameNStart = frameN  # exact frame index
        i03_vL.setAutoDraw(True)
    frameRemains = 3 + 9- win.monitorFramePeriod * 0.75  # most of one frame period left
    if i03_vL.status == STARTED and t >= frameRemains:
        i03_vL.setAutoDraw(False)
    
    # *i03_tR* updates
    if t >= 12 and i03_tR.status == NOT_STARTED:
        # keep track of start time/frame for later
        i03_tR.tStart = t
        i03_tR.frameNStart = frameN  # exact frame index
        i03_tR.setAutoDraw(True)
    frameRemains = 12 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if i03_tR.status == STARTED and t >= frameRemains:
        i03_tR.setAutoDraw(False)
    
    # *i03_vR* updates
    if t >= 15 and i03_vR.status == NOT_STARTED:
        # keep track of start time/frame for later
        i03_vR.tStart = t
        i03_vR.frameNStart = frameN  # exact frame index
        i03_vR.setAutoDraw(True)
    frameRemains = 15 + 9- win.monitorFramePeriod * 0.75  # most of one frame period left
    if i03_vR.status == STARTED and t >= frameRemains:
        i03_vR.setAutoDraw(False)
    
    # *i03_tD* updates
    if t >= 24 and i03_tD.status == NOT_STARTED:
        # keep track of start time/frame for later
        i03_tD.tStart = t
        i03_tD.frameNStart = frameN  # exact frame index
        i03_tD.setAutoDraw(True)
    frameRemains = 24 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if i03_tD.status == STARTED and t >= frameRemains:
        i03_tD.setAutoDraw(False)
    
    # *i03_vD* updates
    if t >= 27 and i03_vD.status == NOT_STARTED:
        # keep track of start time/frame for later
        i03_vD.tStart = t
        i03_vD.frameNStart = frameN  # exact frame index
        i03_vD.setAutoDraw(True)
    frameRemains = 27 + 9- win.monitorFramePeriod * 0.75  # most of one frame period left
    if i03_vD.status == STARTED and t >= frameRemains:
        i03_vD.setAutoDraw(False)
    
    # *i03_tA* updates
    if t >= 36 and i03_tA.status == NOT_STARTED:
        # keep track of start time/frame for later
        i03_tA.tStart = t
        i03_tA.frameNStart = frameN  # exact frame index
        i03_tA.setAutoDraw(True)
    frameRemains = 36 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if i03_tA.status == STARTED and t >= frameRemains:
        i03_tA.setAutoDraw(False)
    
    # *i03_vA* updates
    if t >= 39 and i03_vA.status == NOT_STARTED:
        # keep track of start time/frame for later
        i03_vA.tStart = t
        i03_vA.frameNStart = frameN  # exact frame index
        i03_vA.setAutoDraw(True)
    frameRemains = 39 + 9- win.monitorFramePeriod * 0.75  # most of one frame period left
    if i03_vA.status == STARTED and t >= frameRemains:
        i03_vA.setAutoDraw(False)
    
    # *i03_t* updates
    if t >= 48 and i03_t.status == NOT_STARTED:
        # keep track of start time/frame for later
        i03_t.tStart = t
        i03_t.frameNStart = frameN  # exact frame index
        i03_t.setAutoDraw(True)
    
    # *i03_k* updates
    if t >= 49 and i03_k.status == NOT_STARTED:
        # keep track of start time/frame for later
        i03_k.tStart = t
        i03_k.frameNStart = frameN  # exact frame index
        i03_k.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if i03_k.status == STARTED:
        theseKeys = event.getKeys(keyList=['lshift', 'rshift'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in i03Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "i03"-------
for thisComponent in i03Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "i03" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "InstrL"-------
    t = 0
    InstrLClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    iLk = event.BuilderKeyResponse()
    # keep track of which components have finished
    InstrLComponents = [iLt, iLc, iLk]
    for thisComponent in InstrLComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "InstrL"-------
    while continueRoutine:
        # get current time
        t = InstrLClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iLt* updates
        if t >= 0.0 and iLt.status == NOT_STARTED:
            # keep track of start time/frame for later
            iLt.tStart = t
            iLt.frameNStart = frameN  # exact frame index
            iLt.setAutoDraw(True)
        
        # *iLc* updates
        if t >= 5 and iLc.status == NOT_STARTED:
            # keep track of start time/frame for later
            iLc.tStart = t
            iLc.frameNStart = frameN  # exact frame index
            iLc.setAutoDraw(True)
        
        # *iLk* updates
        if t >= 5 and iLk.status == NOT_STARTED:
            # keep track of start time/frame for later
            iLk.tStart = t
            iLk.frameNStart = frameN  # exact frame index
            iLk.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if iLk.status == STARTED:
            theseKeys = event.getKeys(keyList=['lshift'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstrLComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "InstrL"-------
    for thisComponent in InstrLComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "InstrL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Ready"-------
    t = 0
    ReadyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    tK = event.BuilderKeyResponse()
    # keep track of which components have finished
    ReadyComponents = [rT1, rT2, tK]
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Ready"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ReadyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rT1* updates
        if t >= 0.0 and rT1.status == NOT_STARTED:
            # keep track of start time/frame for later
            rT1.tStart = t
            rT1.frameNStart = frameN  # exact frame index
            rT1.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rT1.status == STARTED and t >= frameRemains:
            rT1.setAutoDraw(False)
        
        # *rT2* updates
        if t >= 3 and rT2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rT2.tStart = t
            rT2.frameNStart = frameN  # exact frame index
            rT2.setAutoDraw(True)
        frameRemains = 3 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rT2.status == STARTED and t >= frameRemains:
            rT2.setAutoDraw(False)
        
        # *tK* updates
        if t >= 3 and tK.status == NOT_STARTED:
            # keep track of start time/frame for later
            tK.tStart = t
            tK.frameNStart = frameN  # exact frame index
            tK.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        frameRemains = 3 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if tK.status == STARTED and t >= frameRemains:
            tK.status = FINISHED
        if tK.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReadyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready"-------
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Left"-------
    t = 0
    LeftClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    Lk = event.BuilderKeyResponse()
    # keep track of which components have finished
    LeftComponents = [Lk, Lt]
    for thisComponent in LeftComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Left"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = LeftClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Lk* updates
        if t >= 0.0 and Lk.status == NOT_STARTED:
            # keep track of start time/frame for later
            Lk.tStart = t
            Lk.frameNStart = frameN  # exact frame index
            Lk.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Lk.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Lk.status == STARTED and t >= frameRemains:
            Lk.status = FINISHED
        if Lk.status == STARTED:
            theseKeys = event.getKeys(keyList=['lshift'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Lk.keys.extend(theseKeys)  # storing all keys
                Lk.rt.append(Lk.clock.getTime())
        
        # *Lt* updates
        if t >= 0.0 and Lt.status == NOT_STARTED:
            # keep track of start time/frame for later
            Lt.tStart = t
            Lt.frameNStart = frameN  # exact frame index
            Lt.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Lt.status == STARTED and t >= frameRemains:
            Lt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LeftComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Left"-------
    for thisComponent in LeftComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Lk.keys in ['', [], None]:  # No response was made
        Lk.keys=None
    trials.addData('Lk.keys',Lk.keys)
    if Lk.keys != None:  # we had a response
        trials.addData('Lk.rt', Lk.rt)
    
    # ------Prepare to start Routine "Done"-------
    t = 0
    DoneClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    DoneComponents = [Complete]
    for thisComponent in DoneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Done"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DoneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Complete* updates
        if t >= 0.0 and Complete.status == NOT_STARTED:
            # keep track of start time/frame for later
            Complete.tStart = t
            Complete.frameNStart = frameN  # exact frame index
            Complete.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Complete.status == STARTED and t >= frameRemains:
            Complete.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DoneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Done"-------
    for thisComponent in DoneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "InstrR"-------
    t = 0
    InstrRClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    iRk = event.BuilderKeyResponse()
    # keep track of which components have finished
    InstrRComponents = [iRt, iRc, iRk]
    for thisComponent in InstrRComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "InstrR"-------
    while continueRoutine:
        # get current time
        t = InstrRClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iRt* updates
        if t >= 0.0 and iRt.status == NOT_STARTED:
            # keep track of start time/frame for later
            iRt.tStart = t
            iRt.frameNStart = frameN  # exact frame index
            iRt.setAutoDraw(True)
        
        # *iRc* updates
        if t >= 5 and iRc.status == NOT_STARTED:
            # keep track of start time/frame for later
            iRc.tStart = t
            iRc.frameNStart = frameN  # exact frame index
            iRc.setAutoDraw(True)
        
        # *iRk* updates
        if t >= 5 and iRk.status == NOT_STARTED:
            # keep track of start time/frame for later
            iRk.tStart = t
            iRk.frameNStart = frameN  # exact frame index
            iRk.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if iRk.status == STARTED:
            theseKeys = event.getKeys(keyList=['rshift'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstrRComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "InstrR"-------
    for thisComponent in InstrRComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "InstrR" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Ready"-------
    t = 0
    ReadyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    tK = event.BuilderKeyResponse()
    # keep track of which components have finished
    ReadyComponents = [rT1, rT2, tK]
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Ready"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ReadyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rT1* updates
        if t >= 0.0 and rT1.status == NOT_STARTED:
            # keep track of start time/frame for later
            rT1.tStart = t
            rT1.frameNStart = frameN  # exact frame index
            rT1.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rT1.status == STARTED and t >= frameRemains:
            rT1.setAutoDraw(False)
        
        # *rT2* updates
        if t >= 3 and rT2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rT2.tStart = t
            rT2.frameNStart = frameN  # exact frame index
            rT2.setAutoDraw(True)
        frameRemains = 3 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rT2.status == STARTED and t >= frameRemains:
            rT2.setAutoDraw(False)
        
        # *tK* updates
        if t >= 3 and tK.status == NOT_STARTED:
            # keep track of start time/frame for later
            tK.tStart = t
            tK.frameNStart = frameN  # exact frame index
            tK.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        frameRemains = 3 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if tK.status == STARTED and t >= frameRemains:
            tK.status = FINISHED
        if tK.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReadyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready"-------
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Right"-------
    t = 0
    RightClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    Rk = event.BuilderKeyResponse()
    # keep track of which components have finished
    RightComponents = [Rk, Rt]
    for thisComponent in RightComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Right"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = RightClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Rk* updates
        if t >= 0.0 and Rk.status == NOT_STARTED:
            # keep track of start time/frame for later
            Rk.tStart = t
            Rk.frameNStart = frameN  # exact frame index
            Rk.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Rk.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Rk.status == STARTED and t >= frameRemains:
            Rk.status = FINISHED
        if Rk.status == STARTED:
            theseKeys = event.getKeys(keyList=['rshift'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Rk.keys.extend(theseKeys)  # storing all keys
                Rk.rt.append(Rk.clock.getTime())
        
        # *Rt* updates
        if t >= 0.0 and Rt.status == NOT_STARTED:
            # keep track of start time/frame for later
            Rt.tStart = t
            Rt.frameNStart = frameN  # exact frame index
            Rt.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Rt.status == STARTED and t >= frameRemains:
            Rt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RightComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Right"-------
    for thisComponent in RightComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Rk.keys in ['', [], None]:  # No response was made
        Rk.keys=None
    trials.addData('Rk.keys',Rk.keys)
    if Rk.keys != None:  # we had a response
        trials.addData('Rk.rt', Rk.rt)
    
    # ------Prepare to start Routine "Done"-------
    t = 0
    DoneClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    DoneComponents = [Complete]
    for thisComponent in DoneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Done"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DoneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Complete* updates
        if t >= 0.0 and Complete.status == NOT_STARTED:
            # keep track of start time/frame for later
            Complete.tStart = t
            Complete.frameNStart = frameN  # exact frame index
            Complete.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Complete.status == STARTED and t >= frameRemains:
            Complete.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DoneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Done"-------
    for thisComponent in DoneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "InstrB"-------
    t = 0
    InstrBClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    iBk = event.BuilderKeyResponse()
    # keep track of which components have finished
    InstrBComponents = [iBt, iBc, iBk]
    for thisComponent in InstrBComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "InstrB"-------
    while continueRoutine:
        # get current time
        t = InstrBClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iBt* updates
        if t >= 0.0 and iBt.status == NOT_STARTED:
            # keep track of start time/frame for later
            iBt.tStart = t
            iBt.frameNStart = frameN  # exact frame index
            iBt.setAutoDraw(True)
        
        # *iBc* updates
        if t >= 5 and iBc.status == NOT_STARTED:
            # keep track of start time/frame for later
            iBc.tStart = t
            iBc.frameNStart = frameN  # exact frame index
            iBc.setAutoDraw(True)
        
        # *iBk* updates
        if t >= 5 and iBk.status == NOT_STARTED:
            # keep track of start time/frame for later
            iBk.tStart = t
            iBk.frameNStart = frameN  # exact frame index
            iBk.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if iBk.status == STARTED:
            theseKeys = event.getKeys(keyList=['lshift', 'rshift'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstrBComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "InstrB"-------
    for thisComponent in InstrBComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "InstrB" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Ready"-------
    t = 0
    ReadyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    tK = event.BuilderKeyResponse()
    # keep track of which components have finished
    ReadyComponents = [rT1, rT2, tK]
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Ready"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ReadyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rT1* updates
        if t >= 0.0 and rT1.status == NOT_STARTED:
            # keep track of start time/frame for later
            rT1.tStart = t
            rT1.frameNStart = frameN  # exact frame index
            rT1.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rT1.status == STARTED and t >= frameRemains:
            rT1.setAutoDraw(False)
        
        # *rT2* updates
        if t >= 3 and rT2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rT2.tStart = t
            rT2.frameNStart = frameN  # exact frame index
            rT2.setAutoDraw(True)
        frameRemains = 3 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rT2.status == STARTED and t >= frameRemains:
            rT2.setAutoDraw(False)
        
        # *tK* updates
        if t >= 3 and tK.status == NOT_STARTED:
            # keep track of start time/frame for later
            tK.tStart = t
            tK.frameNStart = frameN  # exact frame index
            tK.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        frameRemains = 3 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if tK.status == STARTED and t >= frameRemains:
            tK.status = FINISHED
        if tK.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReadyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready"-------
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Both"-------
    t = 0
    BothClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    Bk = event.BuilderKeyResponse()
    # keep track of which components have finished
    BothComponents = [Bk, Bt]
    for thisComponent in BothComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Both"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BothClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Bk* updates
        if t >= 0.0 and Bk.status == NOT_STARTED:
            # keep track of start time/frame for later
            Bk.tStart = t
            Bk.frameNStart = frameN  # exact frame index
            Bk.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Bk.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Bk.status == STARTED and t >= frameRemains:
            Bk.status = FINISHED
        if Bk.status == STARTED:
            theseKeys = event.getKeys(keyList=['lshift', 'rshift'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Bk.keys.extend(theseKeys)  # storing all keys
                Bk.rt.append(Bk.clock.getTime())
        
        # *Bt* updates
        if t >= 0.0 and Bt.status == NOT_STARTED:
            # keep track of start time/frame for later
            Bt.tStart = t
            Bt.frameNStart = frameN  # exact frame index
            Bt.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Bt.status == STARTED and t >= frameRemains:
            Bt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BothComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Both"-------
    for thisComponent in BothComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Bk.keys in ['', [], None]:  # No response was made
        Bk.keys=None
    trials.addData('Bk.keys',Bk.keys)
    if Bk.keys != None:  # we had a response
        trials.addData('Bk.rt', Bk.rt)
    
    # ------Prepare to start Routine "Done"-------
    t = 0
    DoneClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    DoneComponents = [Complete]
    for thisComponent in DoneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Done"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DoneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Complete* updates
        if t >= 0.0 and Complete.status == NOT_STARTED:
            # keep track of start time/frame for later
            Complete.tStart = t
            Complete.frameNStart = frameN  # exact frame index
            Complete.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Complete.status == STARTED and t >= frameRemains:
            Complete.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DoneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Done"-------
    for thisComponent in DoneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "instrA"-------
    t = 0
    instrAClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    iAk = event.BuilderKeyResponse()
    # keep track of which components have finished
    instrAComponents = [iAt, iAc, iAk]
    for thisComponent in instrAComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instrA"-------
    while continueRoutine:
        # get current time
        t = instrAClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iAt* updates
        if t >= 0.0 and iAt.status == NOT_STARTED:
            # keep track of start time/frame for later
            iAt.tStart = t
            iAt.frameNStart = frameN  # exact frame index
            iAt.setAutoDraw(True)
        
        # *iAc* updates
        if t >= 5 and iAc.status == NOT_STARTED:
            # keep track of start time/frame for later
            iAc.tStart = t
            iAc.frameNStart = frameN  # exact frame index
            iAc.setAutoDraw(True)
        
        # *iAk* updates
        if t >= 5 and iAk.status == NOT_STARTED:
            # keep track of start time/frame for later
            iAk.tStart = t
            iAk.frameNStart = frameN  # exact frame index
            iAk.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if iAk.status == STARTED:
            theseKeys = event.getKeys(keyList=['lshift', 'rshift'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrAComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instrA"-------
    for thisComponent in instrAComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instrA" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Ready"-------
    t = 0
    ReadyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    tK = event.BuilderKeyResponse()
    # keep track of which components have finished
    ReadyComponents = [rT1, rT2, tK]
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Ready"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ReadyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rT1* updates
        if t >= 0.0 and rT1.status == NOT_STARTED:
            # keep track of start time/frame for later
            rT1.tStart = t
            rT1.frameNStart = frameN  # exact frame index
            rT1.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rT1.status == STARTED and t >= frameRemains:
            rT1.setAutoDraw(False)
        
        # *rT2* updates
        if t >= 3 and rT2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rT2.tStart = t
            rT2.frameNStart = frameN  # exact frame index
            rT2.setAutoDraw(True)
        frameRemains = 3 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if rT2.status == STARTED and t >= frameRemains:
            rT2.setAutoDraw(False)
        
        # *tK* updates
        if t >= 3 and tK.status == NOT_STARTED:
            # keep track of start time/frame for later
            tK.tStart = t
            tK.frameNStart = frameN  # exact frame index
            tK.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        frameRemains = 3 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if tK.status == STARTED and t >= frameRemains:
            tK.status = FINISHED
        if tK.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ReadyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Ready"-------
    for thisComponent in ReadyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Alternating"-------
    t = 0
    AlternatingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    Ak = event.BuilderKeyResponse()
    # keep track of which components have finished
    AlternatingComponents = [Ak, At]
    for thisComponent in AlternatingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Alternating"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AlternatingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Ak* updates
        if t >= 0.0 and Ak.status == NOT_STARTED:
            # keep track of start time/frame for later
            Ak.tStart = t
            Ak.frameNStart = frameN  # exact frame index
            Ak.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Ak.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Ak.status == STARTED and t >= frameRemains:
            Ak.status = FINISHED
        if Ak.status == STARTED:
            theseKeys = event.getKeys(keyList=['lshift', 'rshift'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Ak.keys.extend(theseKeys)  # storing all keys
                Ak.rt.append(Ak.clock.getTime())
        
        # *At* updates
        if t >= 0.0 and At.status == NOT_STARTED:
            # keep track of start time/frame for later
            At.tStart = t
            At.frameNStart = frameN  # exact frame index
            At.setAutoDraw(True)
        frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
        if At.status == STARTED and t >= frameRemains:
            At.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AlternatingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Alternating"-------
    for thisComponent in AlternatingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Ak.keys in ['', [], None]:  # No response was made
        Ak.keys=None
    trials.addData('Ak.keys',Ak.keys)
    if Ak.keys != None:  # we had a response
        trials.addData('Ak.rt', Ak.rt)
    
    # ------Prepare to start Routine "Done"-------
    t = 0
    DoneClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    DoneComponents = [Complete]
    for thisComponent in DoneComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Done"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DoneClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Complete* updates
        if t >= 0.0 and Complete.status == NOT_STARTED:
            # keep track of start time/frame for later
            Complete.tStart = t
            Complete.frameNStart = frameN  # exact frame index
            Complete.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Complete.status == STARTED and t >= frameRemains:
            Complete.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DoneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Done"-------
    for thisComponent in DoneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
