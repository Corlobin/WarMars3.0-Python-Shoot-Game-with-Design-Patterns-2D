__author__ = 'Ricardo'

class Error(Exception):
     def __init__(self, arg):
        # Set some exception infomation
        self.msg = arg