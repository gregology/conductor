import curses

screen = curses.initscr()

curses.noecho()
curses.cbreak()

screen.keypad(True)

train_art = """
                      (+++++++++++)
                  (++++)
               (+++)
             (+++)
            (++)
            [~]
            | | (~)  (~)  (~)    /~~~~~~~~~~~~
         /~~~~~~~~~~~~~~~~~~~~~~~  [~_~_] |    * * * /~~~~~~~~~~~|
       [|  %___________________           | |~~~~~~~~            |
         \[___] ___   ___   ___\  No. 4   | |   A.T. & S.F.      |
      /// [___+/-+-\-/-+-\-/-+ \\_________|=|____________________|=
    //// @-=-@ \___/ \___/ \___/  @-==-@      @-==-@      @-==-@
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

screen.addstr(0, 0, train_art)

try:
  while True:
    char = screen.getch()
    if char == ord('q'):
      break
    elif char == curses.KEY_UP:
      screen.addstr(14, 0, '       ')
      screen.addstr(14, 0, 'go')
    elif char == curses.KEY_DOWN:
      screen.addstr(14, 0, '       ')
      screen.addstr(14, 0, 'stop')
    elif char == ord('r'):
      screen.addstr(14, 0, '       ')
      screen.addstr(14, 0, 'reverse')
finally:
  curses.nocbreak()
  screen.keypad(0)
  curses.echo()
  curses.endwin()