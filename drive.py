import curses
import time
from adafruit_motorkit import MotorKit

class Conductor:

  def __init__(self): 
    self.kit = MotorKit()
    self.speed = 0

  def increase_speed(self):
    if -0.5 < self.speed < 0.5:
      self.speed = 0.5
    elif self.speed < 1:
      self.speed += 0.1
    self.kit.motor1.throttle = self.speed

  def decrease_speed(self):
    if -0.5 < self.speed < 0.5:
      self.speed = -0.5
    if self.speed > -1:
      self.speed -= 0.1
    self.kit.motor1.throttle = self.speed

  def stop(self):
    self.speed = 0
    self.kit.motor1.throttle = self.speed

  def draw(self):
    train = """
                [~]
              | | (~)  (~)  (~)    /~~~~~~~~~~~~
          /~~~~~~~~~~~~~~~~~~~~~~~  [~_~_] |    * * * /~~~~~~~~~~~|
        [|  %___________________           | |~~~~~~~~            |
          \[___] ___   ___   ___\  No. 4   | |   Hercie Express   |
        /// [___+/-+-\-/-+-\-/-+ \\_________|=|____________________|=
      //// @-=-@ \___/ \___/ \___/  @-==-@      @-==-@      @-==-@
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    if self.speed == 1:
      smoke = """
                          (+++++++++++)
                      (++++)
                  (+++)
                (+++)
                (++)
    """
    elif self.speed > 0.9:
        smoke = """
                      (+++++++++++)
                    (++++)
                  (+++)
                (+++)
                (++)
    """
    elif self.speed > 0.8:
        smoke = """
                  (+++++++++++)
                  (++++)
                (+++)
                (+++)
                (++)
    """
    elif self.speed > 0.7:
        smoke = """
                  (++++++)
                  (+++)
                (++)
                (++)
                (++)
    """
    elif self.speed > 0.6:
        smoke = """
                (++++)
                (+++)
                (++)
                (++)
                (++)
    """
    elif self.speed > 0.5:
        smoke = """
              (++++)
                (++)
                (++)
                (++)
                (++)
    """
    elif self.speed > 0.4:
        smoke = """





    """
    elif self.speed > -0.5:
        smoke = """
              (++++)
                (++)
                (++)
                (++)
                (++)
    """
    elif self.speed > -0.6:
        smoke = """
              (++++)
              (+++)
                (++)
                (++)
                (++)
    """
    elif self.speed > -0.7:
        smoke = """
        (++++++)
            (+++)
              (++)
                (++)
                (++)
    """
    else:
        smoke = """
    (++++++++++)
          (++++)
            (+++)
              (+++)
                (++)
    """
    
    return smoke + train



screen = curses.initscr()

curses.noecho()
curses.cbreak()

screen.keypad(True)

train = Conductor()

screen.addstr(0, 0, train.draw())

try:
  while True:
    char = screen.getch()
    if char == ord('q'):
      break
    elif char == curses.KEY_UP:
      train.increase_speed()
      screen.addstr(0, 0, train.draw())
    elif char == curses.KEY_DOWN:
      train.decrease_speed()
      screen.addstr(0, 0, train.draw())
    elif char == ord(' '):
      train.stop()
      screen.addstr(0, 0, train.draw())
finally:
  curses.nocbreak()
  screen.keypad(0)
  curses.echo()
  curses.endwin()
  train.stop()
