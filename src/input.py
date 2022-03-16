import atexit
import sys
import termios
from select import select


class KBHit:
    '''Refer: "https://stackoverflow.com/a/22085679/17422403"
    This is a different input.py from stackoverflow. Permission for the same has been taken from Vikrant Sir.
    '''

    def __init__(self):
        self.__fd = sys.stdin.fileno()
        self.__new_term = termios.tcgetattr(self.__fd)
        self.__old_term = termios.tcgetattr(self.__fd)

        self.__new_term[3] = (self.__new_term[3] & ~
                              termios.ICANON & ~termios.ECHO)
        termios.tcsetattr(self.__fd, termios.TCSAFLUSH, self.__new_term)

        atexit.register(self.set_normal_term)

    def set_normal_term(self):

        termios.tcsetattr(self.__fd, termios.TCSAFLUSH, self.__old_term)

    @staticmethod
    def getch():

        return sys.stdin.read(1)

    @staticmethod
    def kbhit():
        return select([sys.stdin], [], [], 0)[0] != []

    @staticmethod
    def clear():

        termios.tcflush(sys.stdin, termios.TCIFLUSH)
