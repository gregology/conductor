import curses
import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

screen = curses.initscr()

curses.noecho()
curses.cbreak()

screen.keypad(True)

train_stopped = """
                                            
                          
                           
                        
                  
            [~]
            | | (~)  (~)  (~)    /~~~~~~~~~~~~
         /~~~~~~~~~~~~~~~~~~~~~~~  [~_~_] |    * * * /~~~~~~~~~~~|
       [|  %___________________           | |~~~~~~~~            |
         \[___] ___   ___   ___\  No. 4   | |   Hercie Express   |
      /// [___+/-+-\-/-+-\-/-+ \\_________|=|____________________|=
    //// @-=-@ \___/ \___/ \___/  @-==-@      @-==-@      @-==-@
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

train_go = """
                      (+++++++++++)
                  (++++)
               (+++)
             (+++)
            (++)
            [~]
            | | (~)  (~)  (~)    /~~~~~~~~~~~~
         /~~~~~~~~~~~~~~~~~~~~~~~  [~_~_] |    * * * /~~~~~~~~~~~|
       [|  %___________________           | |~~~~~~~~            |
         \[___] ___   ___   ___\  No. 4   | |   Hercie Express   |
      /// [___+/-+-\-/-+-\-/-+ \\_________|=|____________________|=
    //// @-=-@ \___/ \___/ \___/  @-==-@      @-==-@      @-==-@
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

train_reverse = """
(++++++++)
     (++++)
       (+++)
         (+++)
           (++)
            [~]
            | | (~)  (~)  (~)    /~~~~~~~~~~~~
         /~~~~~~~~~~~~~~~~~~~~~~~  [~_~_] |    * * * /~~~~~~~~~~~|
       [|  %___________________           | |~~~~~~~~            |
         \[___] ___   ___   ___\  No. 4   | |   Hercie Express   |
      /// [___+/-+-\-/-+-\-/-+ \\_________|=|____________________|=
    //// @-=-@ \___/ \___/ \___/  @-==-@      @-==-@      @-==-@
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

screen.addstr(0, 0, train_stopped)

def go():
  kit.motor1.throttle = 0.7
  time.sleep(0.3)
  kit.motor1.throttle = 0.8
  time.sleep(0.3)
  kit.motor1.throttle = 0.9
  time.sleep(0.3)
  kit.motor1.throttle = 1.0

def stop():
  kit.motor1.throttle = 0.9
  time.sleep(0.8)
  kit.motor1.throttle = 0.8
  time.sleep(0.8)
  kit.motor1.throttle = 0.7
  time.sleep(0.8)
  kit.motor1.throttle = 0.6
  time.sleep(0.6)
  kit.motor1.throttle = 0.55
  time.sleep(0.4)
  kit.motor1.throttle = 0

def reverse():
  kit.motor1.throttle = 0
  time.sleep(0.2)
  kit.motor1.throttle = -0.7
  time.sleep(0.3)
  kit.motor1.throttle = -0.8

try:
  while True:
    char = screen.getch()
    if char == ord('q'):
      break
    elif char == curses.KEY_UP:
      screen.addstr(0, 0, train_go)
      go()
    elif char == curses.KEY_DOWN:
      screen.addstr(0, 0, train_stopped)
      stop()
    elif char == ord('r'):
      screen.addstr(0, 0, train_reverse)
      reverse()
    elif char == ord('`'):
      screen.addstr(0, 0, train_stopped)
      kit.motor1.throttle = 0
    elif char == ord('1'):
      screen.addstr(0, 0, train_go)
      kit.motor1.throttle = 0.55
    elif char == ord('2'):
      screen.addstr(0, 0, train_go)
      kit.motor1.throttle = 0.6
    elif char == ord('3'):
      screen.addstr(0, 0, train_go)
      kit.motor1.throttle = 0.65
    elif char == ord('4'):
      screen.addstr(0, 0, train_go)
      kit.motor1.throttle = 0.7
    elif char == ord('5'):
      screen.addstr(0, 0, train_go)
      kit.motor1.throttle = 0.75
    elif char == ord('6'):
      screen.addstr(0, 0, train_go)
      kit.motor1.throttle = 0.8
    elif char == ord('7'):
      screen.addstr(0, 0, train_go)
      kit.motor1.throttle = 0.85
    elif char == ord('8'):
      screen.addstr(0, 0, train_go)
      kit.motor1.throttle = 0.9
    elif char == ord('9'):
      screen.addstr(0, 0, train_go)
      kit.motor1.throttle = 0.95
    elif char == ord('0'):
      screen.addstr(0, 0, train_go)
      kit.motor1.throttle = 1
finally:
  curses.nocbreak()
  screen.keypad(0)
  curses.echo()
  curses.endwin()
  kit.motor1.throttle = 0
