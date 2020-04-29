from mainlist import getData
from check import *
from codeforcesApi.CodeforcesParser import CodeforcesSemiApi as CSA

class MyA2OJ:
    User = None
    Profile = None
    def __init__(self):
        pass

    def assignName(self,handle):
        try:
            self.User=CSA(handle)
            self.Profile=self.User()
            return True
        except:
            self.User=None
            self.Profile=None
            return False

    def current(self):
        if self.User is not None:
            return check(getData,self.User)#return a json file with link
        else:
            return None
            
    def fetch(self,json):
        pass #current progress given problem

    def __repr__():
        pass #anything

    def __call__():
        pass #return something important maybe boolean maybe tags

    def refresh():
        pass #update User
    ### These are after addition of SQL so Later
    def skip():
        pass #to be able to mark a question done when not done 
    def search():
        pass #search editorial of json file google

    def Add():
        pass #add a new question or set of questions with priority
    def skipped():
        pass #This is set of questions which is skipped and sorted based on difficult
        # in reverse or based on recently skipped should be better
        
    
        
    #check(getData("ladder.html"))
