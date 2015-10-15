__author__ = 'Ricardo'

class Error(Exception):
     def __init__(self, arg):
        self.msg = arg