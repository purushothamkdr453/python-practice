#-- help is used for getting the documentation details for
#--- functions, classes, modules, keywords
#--- if you run help with out passing any object then it opens interactive cli utility

#help() #-- commented to avoid opening cli Utility

#-- passing print function as argument to help function

help(print)

#-- help can also be used to get the documentation details about
#-- userdefined functions and classes

class Helper():
    def __init__(self):
        ''' returns init function'''
    def printhelp(self):
        ''' returns print help function'''
        print("hello")

help(Helper)
help(Helper.printhelp)

